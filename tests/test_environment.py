"""
Small standalone test/demo for src/rl/environment.py.

Covers, roughly in order:
  - hand-checkable ensemble score / prediction / reward math on manually
    constructed states (so the arithmetic is verifiable by eye, not just
    "didn't crash")
  - ensemble_predict() vectorized batch scoring, including consistency
    with AnomalyEnsembleEnv.step() run sequentially over the same data
  - episode mechanics: reset()/step()/done, shuffle determinism via seed,
    natural order under shuffle=False, episode_length shorter AND longer
    than the dataset (wrap-around)
  - input validation at every boundary
  - run_episode() convenience driver
  - an integration pass using real S3StateBuilder output (state.py +
    action.py + environment.py + reward.py wired together end to end)

Run with:
    python tests/test_environment.py
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.rl.state import STATE_DIM, S3StateBuilder, TRAFFIC_FEATURE_NAMES
from src.rl.action import ActionProjector, ACTION_DIM, validate_weights
from src.rl.environment import AnomalyEnsembleEnv, StepResult, ensemble_predict
from src.rl.reward import compute_reward_scalar, FINAL_REWARD_SCHEME


def make_state_row(scores4, traffic5=None):
    """Build one valid, self-consistent 14-dim S3 row from 4 detector
    scores -- disagreement stats [4:9] are derived from scores4 so the row
    matches what S3StateBuilder would actually produce, even though
    environment.py itself only reads columns [0:4]."""
    scores4 = np.asarray(scores4, dtype=np.float32)
    disagreement = np.array(
        [
            scores4.mean(),
            scores4.std(),
            scores4.min(),
            scores4.max(),
            scores4.max() - scores4.min(),
        ],
        dtype=np.float32,
    )
    traffic5 = (
        np.zeros(5, dtype=np.float32) if traffic5 is None else np.asarray(traffic5, dtype=np.float32)
    )
    return np.concatenate([scores4, disagreement, traffic5]).astype(np.float32)


def onehot_projector_weights(index: int):
    """A raw_action that relu_normalize projects to an EXACT one-hot weight
    vector (no softmax fuzziness), for hand-checkable arithmetic."""
    raw = np.zeros(ACTION_DIM, dtype=np.float32)
    raw[index] = 1.0
    return raw


def main():
    relu_projector = ActionProjector(method="relu_normalize")
    softmax_projector = ActionProjector(method="softmax")

    # --- 1. Hand-checkable ensemble score / prediction / reward -----------
    # Row: IF=0.9, LOF=0.1, OCSVM=0.9, AE=0.9 ; y_true=1 (attack)
    states = np.stack([make_state_row([0.9, 0.1, 0.9, 0.9])])
    y_true = np.array([1])

    env = AnomalyEnsembleEnv(
        states=states, y_true=y_true, threshold=0.5,
        action_projector=relu_projector, episode_length=1, shuffle=False, seed=0,
    )
    state = env.reset()
    np.testing.assert_allclose(state, states[0])

    # All weight on IF (score 0.9) -> ensemble_score=0.9 >= 0.5 -> pred=1 -> TP -> reward=+1
    result = env.step(onehot_projector_weights(0))
    assert abs(result.info["ensemble_score"] - 0.9) < 1e-6, result.info["ensemble_score"]
    assert result.info["y_pred"] == 1
    assert result.reward == 1.0
    assert result.done is True
    assert result.next_state is None
    print(f"[OK] all-weight-on-IF (score 0.9) -> ensemble_score=0.9, pred=1, "
          f"reward={result.reward} (TP)")

    # --- 2. Same state, all weight on LOF (score 0.1) -> pred=0 -> FN -> reward=-1
    env2 = AnomalyEnsembleEnv(
        states=states, y_true=y_true, threshold=0.5,
        action_projector=relu_projector, episode_length=1, shuffle=False, seed=0,
    )
    env2.reset()
    result2 = env2.step(onehot_projector_weights(1))
    assert abs(result2.info["ensemble_score"] - 0.1) < 1e-6
    assert result2.info["y_pred"] == 0
    assert result2.reward == -1.0
    print(f"[OK] all-weight-on-LOF (score 0.1) -> ensemble_score=0.1, pred=0, "
          f"reward={result2.reward} (FN)")

    # --- 3. Manual reward cross-check against reward.py directly ----------
    manual_reward = compute_reward_scalar(
        y_true=int(y_true[0]), y_pred=result.info["y_pred"], scheme=FINAL_REWARD_SCHEME
    )
    assert manual_reward == result.reward
    print("[OK] environment reward matches reward.compute_reward_scalar() independently")

    # --- 4. ensemble_predict() vectorized batch scoring --------------------
    rng = np.random.default_rng(0)
    n = 500
    scores_batch = rng.uniform(0.0, 1.0, size=(n, 4)).astype(np.float32)
    batch_states = np.stack([make_state_row(s) for s in scores_batch])
    fixed_weights = np.array([0.1, 0.2, 0.3, 0.4], dtype=np.float32)

    ens_scores, y_pred = ensemble_predict(batch_states, fixed_weights, threshold=0.5)
    expected_scores = scores_batch @ fixed_weights
    np.testing.assert_allclose(ens_scores, expected_scores, atol=1e-5)
    np.testing.assert_array_equal(y_pred, (expected_scores >= 0.5).astype(int))
    print(f"[OK] ensemble_predict() with single weight vector matches manual dot product "
          f"({n} rows)")

    # --- 5. ensemble_predict() with per-row weight matrix ------------------
    per_row_weights = rng.dirichlet(alpha=np.ones(4), size=n).astype(np.float32)
    ens_scores2, y_pred2 = ensemble_predict(batch_states, per_row_weights, threshold=0.5)
    expected_scores2 = np.sum(scores_batch * per_row_weights, axis=1)
    np.testing.assert_allclose(ens_scores2, expected_scores2, atol=1e-5)
    print("[OK] ensemble_predict() with per-row weight matrix matches manual computation")

    # --- 6. ensemble_predict() rejects invalid weight shapes/values --------
    try:
        ensemble_predict(batch_states, np.array([0.5, 0.5, 0.5]))  # wrong length
        raise AssertionError("Expected ValueError for wrong-length weights")
    except ValueError:
        print("[OK] ensemble_predict() rejects wrong-length weight vector")

    try:
        ensemble_predict(batch_states, np.zeros((n - 1, ACTION_DIM)) + 0.25)  # wrong row count
        raise AssertionError("Expected ValueError for mismatched per-row weight count")
    except ValueError:
        print("[OK] ensemble_predict() rejects per-row weights with mismatched row count")

    try:
        ensemble_predict(batch_states, np.array([0.5, 0.5, 0.5, -0.5]))  # invalid (negative)
        raise AssertionError("Expected ValueError for invalid (negative) weights")
    except ValueError:
        print("[OK] ensemble_predict() rejects invalid (non-simplex) weights")

    # --- 7. step()-vs-ensemble_predict consistency over a full sequential pass --
    y_true_batch = (scores_batch.mean(axis=1) > 0.5).astype(int)
    seq_env = AnomalyEnsembleEnv(
        states=batch_states, y_true=y_true_batch, threshold=0.5,
        action_projector=relu_projector, episode_length=n, shuffle=False, seed=0,
    )
    seq_env.reset()
    raw_fixed = np.array([0.1, 0.2, 0.3, 0.4], dtype=np.float32)  # already-normalized -> relu_normalize passes through unchanged
    step_scores = []
    step_preds = []
    for _ in range(n):
        result = seq_env.step(raw_fixed)
        step_scores.append(result.info["ensemble_score"])
        step_preds.append(result.info["y_pred"])
        if result.done:
            break
    np.testing.assert_allclose(step_scores, ens_scores, atol=1e-5)
    np.testing.assert_array_equal(step_preds, y_pred)
    print("[OK] sequential env.step() scores/predictions match ensemble_predict() batch output "
          "exactly, same weights, same order")

    # --- 8. reset() shuffle determinism: same seed -> identical index order --
    env_a = AnomalyEnsembleEnv(states=batch_states, y_true=y_true_batch, seed=77, episode_length=50)
    env_b = AnomalyEnsembleEnv(states=batch_states, y_true=y_true_batch, seed=77, episode_length=50)
    env_a.reset()
    env_b.reset()
    idx_a = [env_a.step(raw_fixed).info["index"] for _ in range(50)]
    idx_b = [env_b.step(raw_fixed).info["index"] for _ in range(50)]
    assert idx_a == idx_b
    print("[OK] same seed -> identical shuffled iteration order across two env instances")

    # --- 9. shuffle=False preserves natural (0, 1, 2, ...) order -----------
    env_natural = AnomalyEnsembleEnv(
        states=batch_states, y_true=y_true_batch, shuffle=False, episode_length=20
    )
    env_natural.reset()
    natural_idx = [env_natural.step(raw_fixed).info["index"] for _ in range(20)]
    assert natural_idx == list(range(20))
    print("[OK] shuffle=False iterates samples in natural 0..n-1 order")

    # --- 10. episode_length shorter than dataset: done fires exactly there --
    short_env = AnomalyEnsembleEnv(
        states=batch_states, y_true=y_true_batch, shuffle=False, episode_length=10
    )
    short_env.reset()
    dones = []
    for _ in range(10):
        result = short_env.step(raw_fixed)
        dones.append(result.done)
    assert dones == [False] * 9 + [True]
    assert result.next_state is None
    print("[OK] episode_length=10 -> done fires exactly on the 10th step, next_state=None")

    # --- 11. episode_length longer than dataset: wraps via modulo ----------
    wrap_env = AnomalyEnsembleEnv(
        states=batch_states[:5], y_true=y_true_batch[:5], shuffle=False, episode_length=12
    )
    wrap_env.reset()
    wrap_idx = [wrap_env.step(raw_fixed).info["index"] for _ in range(12)]
    assert wrap_idx == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1]
    print(f"[OK] episode_length (12) > n_samples (5) wraps around via modulo -> {wrap_idx}")

    # --- 12. step() before reset() raises -----------------------------------
    fresh_env = AnomalyEnsembleEnv(states=batch_states, y_true=y_true_batch)
    try:
        fresh_env.step(raw_fixed)
        raise AssertionError("Expected RuntimeError calling step() before reset()")
    except RuntimeError:
        print("[OK] step() before reset() raises RuntimeError")

    # --- 13. constructor input validation -----------------------------------
    try:
        AnomalyEnsembleEnv(states=np.zeros((10, 13)), y_true=np.zeros(10))  # wrong state dim
        raise AssertionError("Expected ValueError for wrong state dimension")
    except ValueError:
        print("[OK] constructor rejects states with wrong STATE_DIM")

    try:
        AnomalyEnsembleEnv(states=batch_states, y_true=np.array([0, 1, 2] * (n // 3)))  # non-binary
        raise AssertionError("Expected ValueError for non-binary y_true")
    except ValueError:
        print("[OK] constructor rejects non-binary y_true")

    try:
        AnomalyEnsembleEnv(states=batch_states, y_true=np.zeros(n - 1))  # length mismatch
        raise AssertionError("Expected ValueError for mismatched states/y_true length")
    except ValueError:
        print("[OK] constructor rejects mismatched states/y_true length")

    try:
        AnomalyEnsembleEnv(states=batch_states, y_true=y_true_batch, episode_length=0)
        raise AssertionError("Expected ValueError for non-positive episode_length")
    except ValueError:
        print("[OK] constructor rejects non-positive episode_length")

    # --- 14. run_episode() convenience driver -------------------------------
    const_agent = lambda state: onehot_projector_weights(3)  # always all-weight-on-AE
    driver_env = AnomalyEnsembleEnv(
        states=batch_states, y_true=y_true_batch, threshold=0.5,
        action_projector=relu_projector, episode_length=40, shuffle=False, seed=5,
    )
    summary = driver_env.run_episode(const_agent)
    assert summary["n_steps"] == 40
    assert len(summary["steps"]) == 40
    expected_total = sum(
        compute_reward_scalar(int(y_true_batch[i]), int(scores_batch[i, 3] >= 0.5))
        for i in range(40)
    )
    assert abs(summary["total_reward"] - expected_total) < 1e-6
    assert abs(summary["mean_reward"] - expected_total / 40) < 1e-6
    print(f"[OK] run_episode() with constant AE-only agent -> total_reward={summary['total_reward']}, "
          f"matches independently-recomputed expectation")

    # --- 15. StepResult field sanity ----------------------------------------
    assert isinstance(summary["steps"][0], dict)
    assert set(summary["steps"][0].keys()) == {"index", "ensemble_score", "weights", "y_true", "y_pred"}
    print("[OK] StepResult.info carries the expected fields (index, ensemble_score, weights, "
          "y_true, y_pred)")

    # --- 16. Integration: real S3StateBuilder -> environment end to end ----
    val_scores = {
        "isolation_forest": rng.normal(0.4, 0.07, 3000).clip(0.3, 0.75),
        "lof": rng.normal(0.4, 80.0, 3000),
        "ocsvm": rng.normal(-33.0, 20.0, 3000),
        "autoencoder": rng.normal(0.15, 8.8, 3000).clip(0.0001, None),
    }
    builder = S3StateBuilder().fit_normalizers(val_scores)

    n_new = 400
    new_scores = {
        "isolation_forest": rng.normal(0.4, 0.07, n_new).clip(0.3, 0.75),
        "lof": rng.normal(0.4, 80.0, n_new),
        "ocsvm": rng.normal(-33.0, 20.0, n_new),
        "autoencoder": rng.normal(0.15, 8.8, n_new).clip(0.0001, None),
    }
    traffic_df = pd.DataFrame(
        {name: rng.exponential(300.0, n_new) for name in TRAFFIC_FEATURE_NAMES}
    )
    real_states = builder.build(new_scores, traffic_df)
    real_y_true = (rng.uniform(size=n_new) > 0.8).astype(int)

    integration_env = AnomalyEnsembleEnv(
        states=real_states, y_true=real_y_true, threshold=0.5,
        action_projector=softmax_projector, episode_length=n_new, shuffle=True, seed=3,
    )
    state = integration_env.reset()
    assert state.shape == (STATE_DIM,)
    total_reward = 0.0
    steps = 0
    while True:
        # simple deterministic "agent": mild logit favoring the AE column,
        # since AE was the strongest individual detector in the project's
        # own baselines (master handoff section 8) -- just exercising the
        # full pipeline here, not claiming this is a trained policy.
        raw_action = np.array([0.0, 0.0, 0.0, 1.0], dtype=np.float32)
        result = integration_env.step(raw_action)
        validate_weights(result.info["weights"])
        total_reward += result.reward
        steps += 1
        if result.done:
            break
        state = result.next_state
    assert steps == n_new
    print(f"[OK] full S3StateBuilder -> AnomalyEnsembleEnv integration pass: "
          f"{steps} steps, total_reward={total_reward:.1f}, all weights valid")

    print("\nAll environment.py checks passed.")


if __name__ == "__main__":
    main()