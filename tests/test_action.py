"""
Small standalone test/demo for src/rl/action.py.

Run with:
    python tests/test_action.py
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.rl.action import (
    ActionProjector,
    DETECTOR_NAMES,
    ACTION_DIM,
    validate_weights,
    weights_to_dict,
    dict_to_weights,
)
from src.rl.state import MODEL_ORDER


def check_valid_action(weights: np.ndarray, context: str):
    assert weights.shape[-1] == ACTION_DIM, f"{context}: wrong dim {weights.shape}"
    assert np.all(weights >= 0), f"{context}: negative weight found"
    sums = weights.sum(axis=-1)
    assert np.allclose(sums, 1.0, atol=1e-5), f"{context}: sums={sums}"


def main():
    # 0. Detector order must be identically the same object/tuple as state.py's.
    assert DETECTOR_NAMES == MODEL_ORDER
    assert DETECTOR_NAMES == ("isolation_forest", "lof", "ocsvm", "autoencoder")
    print("[OK] DETECTOR_NAMES matches state.py MODEL_ORDER exactly")

    rng = np.random.default_rng(0)

    # --- softmax projection --------------------------------------------
    softmax_proj = ActionProjector(method="softmax")

    # 1. Single raw action, arbitrary unconstrained logits.
    raw_single = rng.normal(size=4)
    w = softmax_proj.project(raw_single)
    check_valid_action(w, "softmax/single")
    assert w.dtype == np.float32
    print(f"[OK] softmax single action -> {w} (sum={w.sum():.6f})")

    # 2. Batch of raw actions.
    raw_batch = rng.normal(size=(200, 4))
    w_batch = softmax_proj.project(raw_batch)
    check_valid_action(w_batch, "softmax/batch")
    print(f"[OK] softmax batch action -> shape {w_batch.shape}, all valid simplex rows")

    # 3. Extreme logits (numerical stability check) must not produce NaN/inf.
    extreme = np.array([1000.0, -1000.0, 0.0, 500.0])
    w_extreme = softmax_proj.project(extreme)
    check_valid_action(w_extreme, "softmax/extreme")
    assert np.all(np.isfinite(w_extreme))
    print(f"[OK] softmax handles extreme logits without overflow -> {w_extreme}")

    # 4. One detector dominates -> its weight should be close to 1.
    dominant = np.array([-10.0, -10.0, -10.0, 10.0])  # AE index
    w_dom = softmax_proj.project(dominant)
    assert w_dom[3] > 0.99, w_dom
    print(f"[OK] softmax concentrates weight on dominant logit -> {w_dom}")

    # --- relu_normalize projection ---------------------------------------
    relu_proj = ActionProjector(method="relu_normalize")

    # 5. Already-non-negative raw action normalizes proportionally.
    raw_pos = np.array([1.0, 1.0, 2.0, 4.0])
    w_relu = relu_proj.project(raw_pos)
    check_valid_action(w_relu, "relu/positive")
    np.testing.assert_allclose(w_relu, [0.125, 0.125, 0.25, 0.5], atol=1e-5)
    print(f"[OK] relu_normalize proportionally normalizes positive input -> {w_relu}")

    # 6. Mixed positive/negative clips negatives to 0 before normalizing.
    raw_mixed = np.array([-5.0, 0.0, 1.0, 3.0])
    w_mixed = relu_proj.project(raw_mixed)
    check_valid_action(w_mixed, "relu/mixed")
    assert w_mixed[0] == 0.0
    np.testing.assert_allclose(w_mixed[1:], [0.0, 0.25, 0.75], atol=1e-5)
    print(f"[OK] relu_normalize clips negatives before normalizing -> {w_mixed}")

    # 7. All-non-positive input -> uniform fallback, no NaN/divide-by-zero.
    raw_all_neg = np.array([-1.0, -2.0, -0.5, 0.0])
    w_fallback = relu_proj.project(raw_all_neg)
    check_valid_action(w_fallback, "relu/all_non_positive")
    np.testing.assert_allclose(w_fallback, [0.25, 0.25, 0.25, 0.25], atol=1e-5)
    print(f"[OK] relu_normalize falls back to uniform weights when all inputs <= 0 -> {w_fallback}")

    # 8. Batch with a mix of degenerate and normal rows.
    raw_batch2 = np.array([
        [-1.0, -1.0, -1.0, -1.0],   # degenerate -> uniform
        [0.0, 0.0, 0.0, 4.0],       # normal
        [2.0, 2.0, 2.0, 2.0],       # normal, already uniform
    ])
    w_batch2 = relu_proj.project(raw_batch2)
    check_valid_action(w_batch2, "relu/batch_mixed")
    np.testing.assert_allclose(w_batch2[0], [0.25, 0.25, 0.25, 0.25], atol=1e-5)
    np.testing.assert_allclose(w_batch2[1], [0.0, 0.0, 0.0, 1.0], atol=1e-5)
    np.testing.assert_allclose(w_batch2[2], [0.25, 0.25, 0.25, 0.25], atol=1e-5)
    print("[OK] relu_normalize batch correctly mixes fallback and normal rows")

    # --- input validation ---------------------------------------------------
    # 9. Wrong dim raises.
    try:
        softmax_proj.project(np.array([1.0, 2.0, 3.0]))  # only 3 values
        raise AssertionError("Expected ValueError for wrong action dimension")
    except ValueError:
        print("[OK] project() rejects wrong-length raw_action")

    # 10. NaN input raises.
    try:
        softmax_proj.project(np.array([1.0, np.nan, 0.0, 0.0]))
        raise AssertionError("Expected ValueError for NaN input")
    except ValueError:
        print("[OK] project() rejects NaN/inf raw_action")

    # 11. Unknown method raises at construction.
    try:
        ActionProjector(method="dqn_argmax")
        raise AssertionError("Expected ValueError for unknown method")
    except ValueError:
        print("[OK] ActionProjector rejects unknown projection method")

    # --- validate_weights standalone -----------------------------------
    # 12. Manually-built invalid weights are rejected.
    try:
        validate_weights(np.array([0.5, 0.5, 0.5, -0.5]))  # negative
        raise AssertionError("Expected ValueError for negative weight")
    except ValueError:
        print("[OK] validate_weights rejects negative weights")

    try:
        validate_weights(np.array([0.1, 0.1, 0.1, 0.1]))  # sums to 0.4, not 1
        raise AssertionError("Expected ValueError for bad sum")
    except ValueError:
        print("[OK] validate_weights rejects weights that don't sum to 1")

    # --- dict conversions -------------------------------------------------
    # 13. weights_to_dict / dict_to_weights round-trip, in fixed order.
    w = softmax_proj.project(rng.normal(size=4))
    d = weights_to_dict(w)
    assert list(d.keys()) == list(DETECTOR_NAMES)
    w_back = dict_to_weights(d)
    np.testing.assert_allclose(w, w_back, atol=1e-6)
    print(f"[OK] weights_to_dict/dict_to_weights round-trip -> {d}")

    # 14. dict_to_weights rejects a dict missing a detector.
    incomplete = {k: v for k, v in d.items() if k != "lof"}
    try:
        dict_to_weights(incomplete)
        raise AssertionError("Expected KeyError for missing detector key")
    except KeyError:
        print("[OK] dict_to_weights rejects a dict missing a required detector")

    print("\nAll action.py checks passed.")


if __name__ == "__main__":
    main()