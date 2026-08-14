"""
Small standalone test/demo for src/rl/state.py.

Uses synthetic data shaped like the ranges reported in the master handoff
(section 10) since the actual trained-model scores / CICIDS2017 features
were not part of this handoff bundle. Once the real repo (trained_models/,
evaluation_results/) is available, swap the synthetic generators below for
real val/test score + feature loads and re-run.

Run with:
    python tests/test_state.py
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.rl.state import S3StateBuilder, STATE_DIM, STATE_FEATURE_NAMES, TRAFFIC_FEATURE_NAMES


def make_synthetic_scores(n: int, low: float, high: float, mean: float, std: float, seed: int):
    rng = np.random.default_rng(seed)
    scores = rng.normal(loc=mean, scale=std, size=n)
    return np.clip(scores, low, high)


def make_synthetic_dataset(n_val: int = 5000, n_new: int = 1000):
    # Ranges pulled from master handoff section 10 (validation score ranges).
    val_scores = {
        "isolation_forest": make_synthetic_scores(n_val, 0.31999, 0.74434, 0.38066, 0.07008, 1),
        "lof": make_synthetic_scores(n_val, -2.29467, 8985.52774, 0.43467, 79.92338, 2),
        "ocsvm": make_synthetic_scores(n_val, -73.46681, 100.20541, -33.47075, 20.52621, 3),
        "autoencoder": make_synthetic_scores(n_val, 0.000068, 2874.155029, 0.146533, 8.841113, 4),
    }
    new_scores = {
        "isolation_forest": make_synthetic_scores(n_new, 0.31999, 0.74434, 0.38066, 0.07008, 11),
        "lof": make_synthetic_scores(n_new, -2.29467, 8985.52774, 0.43467, 79.92338, 12),
        "ocsvm": make_synthetic_scores(n_new, -73.46681, 100.20541, -33.47075, 20.52621, 13),
        "autoencoder": make_synthetic_scores(n_new, 0.000068, 2874.155029, 0.146533, 8.841113, 14),
    }
    rng = np.random.default_rng(99)
    traffic_df = pd.DataFrame(
        {name: rng.exponential(scale=500.0, size=n_new) for name in TRAFFIC_FEATURE_NAMES}
    )
    return val_scores, new_scores, traffic_df


def main():
    val_scores, new_scores, traffic_df = make_synthetic_dataset()

    builder = S3StateBuilder()

    # 1. Must refuse to build before fitting.
    try:
        builder.build(new_scores, traffic_df)
        raise AssertionError("Expected RuntimeError before fit_normalizers()")
    except RuntimeError:
        print("[OK] build() correctly refuses to run before fit_normalizers()")

    # 2. Fit on validation-only reference scores.
    builder.fit_normalizers(val_scores)
    assert builder.is_fitted
    print("[OK] normalizers fitted on validation scores")

    # 3. Build state on a new batch.
    state = builder.build(new_scores, traffic_df)
    assert state.shape == (1000, STATE_DIM), state.shape
    assert state.dtype == np.float32
    print(f"[OK] state shape = {state.shape}, dtype = {state.dtype}")

    # 4. Normalized score columns [0:4] must lie in [0, 1].
    assert np.all(state[:, :4] >= 0.0) and np.all(state[:, :4] <= 1.0)
    print("[OK] normalized score columns are within [0, 1]")

    # 5. Disagreement columns [4:9] must be internally consistent.
    score_cols = state[:, :4]
    mean_col, std_col, min_col, max_col, range_col = (
        state[:, 4], state[:, 5], state[:, 6], state[:, 7], state[:, 8]
    )
    np.testing.assert_allclose(mean_col, score_cols.mean(axis=1), rtol=1e-5)
    np.testing.assert_allclose(min_col, score_cols.min(axis=1), rtol=1e-5)
    np.testing.assert_allclose(max_col, score_cols.max(axis=1), rtol=1e-5)
    np.testing.assert_allclose(range_col, max_col - min_col, rtol=1e-5)
    assert np.all(range_col >= 0)
    print("[OK] disagreement statistics are internally consistent")

    # 6. Traffic columns [9:14] must match input traffic_df exactly.
    np.testing.assert_allclose(
        state[:, 9:14], traffic_df[list(TRAFFIC_FEATURE_NAMES)].to_numpy(), rtol=1e-5
    )
    print("[OK] traffic-context columns pass through unchanged")

    # 7. Labeled frame helper.
    frame = builder.build_as_frame(new_scores, traffic_df)
    assert list(frame.columns) == list(STATE_FEATURE_NAMES)
    print("[OK] build_as_frame() returns correctly labeled columns:")
    print(frame.head(3).to_string())

    # 8. Mismatched-length inputs must raise.
    bad_scores = dict(new_scores)
    bad_scores["lof"] = bad_scores["lof"][:-1]
    try:
        builder.build(bad_scores, traffic_df)
        raise AssertionError("Expected ValueError on mismatched lengths")
    except ValueError:
        print("[OK] build() correctly rejects mismatched-length raw_scores")

    # 9. Missing traffic column must raise.
    bad_traffic = traffic_df.drop(columns=[TRAFFIC_FEATURE_NAMES[0]])
    try:
        builder.build(new_scores, bad_traffic)
        raise AssertionError("Expected KeyError on missing traffic column")
    except KeyError:
        print("[OK] build() correctly rejects traffic_features missing a required column")

    # 10. Persistence round-trip (no hardcoded path -- caller supplies dict/location).
    saved_state = builder.get_normalizer_state()
    reloaded = S3StateBuilder().load_normalizer_state(saved_state)
    state_reloaded = reloaded.build(new_scores, traffic_df)
    np.testing.assert_allclose(state, state_reloaded)
    print("[OK] normalizer persistence round-trip reproduces identical state")

    print("\nAll state.py checks passed.")


if __name__ == "__main__":
    main()