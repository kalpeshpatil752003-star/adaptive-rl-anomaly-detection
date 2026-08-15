"""
Small standalone test/demo for src/rl/agent.py (PPO).

Run with:
    python tests/test_agent.py
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.rl.state import STATE_DIM
from src.rl.action import ActionProjector, ACTION_DIM, validate_weights
from src.rl.environment import AnomalyEnsembleEnv
from src.rl.agent import PPOAgent, PPOConfig, RolloutBuffer


def make_synthetic_states_and_labels(n: int, seed: int = 0):
    rng = np.random.default_rng(seed)
    scores = rng.uniform(0.0, 1.0, size=(n, 4)).astype(np.float32)
    disagreement = np.column_stack(
        [
            scores.mean(axis=1),
            scores.std(axis=1),
            scores.min(axis=1),
            scores.max(axis=1),
            scores.max(axis=1) - scores.min(axis=1),
        ]
    ).astype(np.float32)
    traffic = rng.exponential(scale=200.0, size=(n, 5)).astype(np.float32)
    states = np.concatenate([scores, disagreement, traffic], axis=1)
    y_true = (scores.mean(axis=1) + rng.normal(0, 0.15, size=n) > 0.5).astype(int)
    return states, y_true


def main():
    n_samples = 2000
    states, y_true = make_synthetic_states_and_labels(n_samples)
    assert states.shape == (n_samples, STATE_DIM)
    print(f"[OK] synthetic dataset: states {states.shape}, attack rate {y_true.mean():.3f}")

    env = AnomalyEnsembleEnv(
        states=states, y_true=y_true, threshold=0.5,
        action_projector=ActionProjector(method="softmax"),
        episode_length=500, shuffle=True, seed=42,
    )

    config = PPOConfig(rollout_steps=256, batch_size=64, n_epochs=4)
    agent = PPOAgent(config)

    # 1. select_action shape/range contract (both explore modes).
    s0 = env.reset()
    a_explore = agent.select_action(s0, explore=True)
    a_deterministic = agent.select_action(s0, explore=False)
    assert a_explore.shape == (ACTION_DIM,)
    assert a_deterministic.shape == (ACTION_DIM,)
    print(f"[OK] select_action shapes correct (explore={a_explore.shape}, "
          f"deterministic={a_deterministic.shape})")

    # 2. Raw actions project into valid A3 weights.
    projector = ActionProjector(method="softmax")
    weights = projector.project(a_explore)
    validate_weights(weights)
    print(f"[OK] agent output projects to valid A3 weights -> {weights} "
          f"(sum={weights.sum():.6f})")

    # 3. agent.step() returns (action, log_prob, value) usable for buffer.add().
    action, log_prob, value = agent.step(s0)
    assert action.shape == (ACTION_DIM,)
    assert isinstance(log_prob, float) and isinstance(value, float)
    print(f"[OK] agent.step() -> action shape {action.shape}, "
          f"log_prob={log_prob:.4f}, value={value:.4f}")

    # 4. Full rollout collection into a fixed-capacity RolloutBuffer.
    buffer = RolloutBuffer(
        buffer_size=config.rollout_steps,
        state_dim=STATE_DIM,
        action_dim=ACTION_DIM,
        gamma=config.gamma,
        gae_lambda=config.gae_lambda,
    )
    state = env.reset()
    last_done = False
    for _ in range(config.rollout_steps):
        action, log_prob, value = agent.step(state)
        result = env.step(action)
        buffer.add(state, action, log_prob, result.reward, value, result.done)
        last_done = result.done
        state = env.reset() if result.done else result.next_state
    assert len(buffer) == config.rollout_steps
    print(f"[OK] rollout collection filled buffer -> size={len(buffer)}")

    # 5. RolloutBuffer enforces fixed capacity.
    try:
        buffer.add(state, action, log_prob, 0.0, value, False)
        raise AssertionError("Expected RuntimeError adding beyond buffer_size")
    except RuntimeError:
        print("[OK] RolloutBuffer rejects add() beyond buffer_size")

    # 6. GAE bootstrap + get_batches() contract.
    last_value = agent.get_value(state)
    buffer.compute_returns_and_advantages(last_value, last_done)
    assert buffer.advantages.shape == (config.rollout_steps,)
    assert buffer.returns.shape == (config.rollout_steps,)
    assert np.all(np.isfinite(buffer.advantages))
    assert np.all(np.isfinite(buffer.returns))
    print("[OK] compute_returns_and_advantages() produced finite advantages/returns")

    batches = list(buffer.get_batches(config.batch_size, rng=np.random.default_rng(1)))
    total_batched = sum(len(b["states"]) for b in batches)
    assert total_batched == config.rollout_steps
    for b in batches:
        assert b["states"].shape[1] == STATE_DIM
        assert b["actions"].shape[1] == ACTION_DIM
    print(f"[OK] get_batches() covers full rollout across {len(batches)} minibatches")

    # 7. get_batches() rejects batch_size larger than collected size.
    small_buffer = RolloutBuffer(buffer_size=10)
    for i in range(5):
        small_buffer.add(state, action, log_prob, 0.0, value, False)
    try:
        list(small_buffer.get_batches(batch_size=8))
        raise AssertionError("Expected ValueError: batch_size exceeds rollout size")
    except ValueError:
        print("[OK] get_batches() rejects batch_size exceeding collected rollout size")

    # 8. train_step() runs and returns finite losses.
    losses = agent.train_step(buffer)
    assert np.isfinite(losses["policy_loss"])
    assert np.isfinite(losses["value_loss"])
    assert np.isfinite(losses["entropy"])
    print(f"[OK] train_step() -> policy_loss={losses['policy_loss']:.4f}, "
          f"value_loss={losses['value_loss']:.4f}, entropy={losses['entropy']:.4f}")

    # 9. Multiple train_step() calls increment total_updates.
    buffer.reset()
    for _ in range(config.rollout_steps):
        a, lp, v = agent.step(state)
        result = env.step(a)
        buffer.add(state, a, lp, result.reward, v, result.done)
        state = env.reset() if result.done else result.next_state
    buffer.compute_returns_and_advantages(agent.get_value(state), result.done)
    losses2 = agent.train_step(buffer)
    assert losses2["total_updates"] == losses["total_updates"] + 1
    print(f"[OK] total_updates increments across train_step() calls "
          f"({losses['total_updates']} -> {losses2['total_updates']})")

    # 10. state_dict/load_state_dict round-trip reproduces identical deterministic actions.
    saved = agent.state_dict()
    fresh_agent = PPOAgent(config)
    fresh_agent.load_state_dict(saved)
    eval_state = env.reset()
    a1 = agent.select_action(eval_state, explore=False)
    a2 = fresh_agent.select_action(eval_state, explore=False)
    np.testing.assert_allclose(a1, a2, atol=1e-6)
    print("[OK] state_dict()/load_state_dict() round-trip reproduces identical actions")

    print("\nAll agent.py checks passed.")


if __name__ == "__main__":
    main()