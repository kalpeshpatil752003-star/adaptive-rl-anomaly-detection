"""
Small standalone test/demo for src/rl/reward.py.

Includes a regression test that reconstructs the EXACT reference confusion
matrix reported in master handoff section 23 (TP=19203, TN=159224,
FP=8381, FN=14856, total=201664 -- matching the state_s3.npy row count in
section 16) and checks that R1's mean/total reward match the documented
values (mean_reward=0.769547, total_reward=155190).

Run with:
    python tests/test_reward.py
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.rl.reward import (
    compute_reward,
    compute_reward_scalar,
    confusion_counts,
    reward_summary,
    R1_BALANCED,
    R2_ATTACK_SENSITIVE,
    R3_STRONG_ATTACK_SENSITIVE,
    FINAL_REWARD_SCHEME,
)


def build_reference_labels():
    """Construct y_true/y_pred that reproduce the exact section-23 reference
    confusion matrix: TP=19203, TN=159224, FP=8381, FN=14856."""
    TP, TN, FP, FN = 19203, 159224, 8381, 14856

    y_true = np.concatenate([
        np.ones(TP, dtype=int),   # TP: true=1
        np.zeros(TN, dtype=int),  # TN: true=0
        np.zeros(FP, dtype=int),  # FP: true=0
        np.ones(FN, dtype=int),   # FN: true=1
    ])
    y_pred = np.concatenate([
        np.ones(TP, dtype=int),   # TP: pred=1
        np.zeros(TN, dtype=int),  # TN: pred=0
        np.ones(FP, dtype=int),   # FP: pred=1
        np.zeros(FN, dtype=int),  # FN: pred=0
    ])
    return y_true, y_pred


def main():
    # 1. Frozen scheme sanity.
    assert FINAL_REWARD_SCHEME is R1_BALANCED
    assert (R1_BALANCED.tp, R1_BALANCED.tn, R1_BALANCED.fp, R1_BALANCED.fn) == (1.0, 1.0, -1.0, -1.0)
    assert (R2_ATTACK_SENSITIVE.tp, R2_ATTACK_SENSITIVE.tn, R2_ATTACK_SENSITIVE.fp, R2_ATTACK_SENSITIVE.fn) == (1.0, 1.0, -1.0, -2.0)
    assert (R3_STRONG_ATTACK_SENSITIVE.tp, R3_STRONG_ATTACK_SENSITIVE.tn, R3_STRONG_ATTACK_SENSITIVE.fp, R3_STRONG_ATTACK_SENSITIVE.fn) == (1.0, 1.0, -1.0, -3.0)
    print("[OK] R1/R2/R3 reward schemes match the documented section-22 definitions")

    # 2. Basic per-sample reward on a tiny hand-checkable example.
    y_true = np.array([1, 0, 0, 1])
    y_pred = np.array([1, 0, 1, 0])  # TP, TN, FP, FN
    reward = compute_reward(y_true, y_pred)
    np.testing.assert_array_equal(reward, [1.0, 1.0, -1.0, -1.0])
    print(f"[OK] compute_reward on TP/TN/FP/FN example -> {reward}")

    # 3. Scalar convenience wrapper matches batch computation.
    for yt, yp, expected in [(1, 1, 1.0), (0, 0, 1.0), (0, 1, -1.0), (1, 0, -1.0)]:
        got = compute_reward_scalar(yt, yp)
        assert got == expected, (yt, yp, got, expected)
    print("[OK] compute_reward_scalar matches batch compute_reward for all 4 outcomes")

    # 4. confusion_counts on the tiny example.
    counts = confusion_counts(y_true, y_pred)
    assert counts == (1, 1, 1, 1), counts
    print(f"[OK] confusion_counts -> {counts}")

    # --- reference-matrix regression test (ties back to section 23) ------
    ref_y_true, ref_y_pred = build_reference_labels()
    assert len(ref_y_true) == 201664, "reference sample count should match state_s3.npy (section 16)"

    ref_counts = confusion_counts(ref_y_true, ref_y_pred)
    assert ref_counts == (19203, 159224, 8381, 14856), ref_counts
    print(f"[OK] reconstructed reference confusion matrix -> {ref_counts}")

    summary_r1 = reward_summary(ref_y_true, ref_y_pred, scheme=R1_BALANCED)
    print(f"[OK] R1 summary -> mean_reward={summary_r1['mean_reward']:.6f}, "
          f"total_reward={summary_r1['total_reward']:.0f}")
    assert abs(summary_r1["mean_reward"] - 0.769547) < 1e-5, summary_r1["mean_reward"]
    assert summary_r1["total_reward"] == 155190.0, summary_r1["total_reward"]
    print("[OK] R1 mean/total reward match master handoff section 23 EXACTLY")

    # 5. R2/R3 summaries, checked against the documented comparison too.
    summary_r2 = reward_summary(ref_y_true, ref_y_pred, scheme=R2_ATTACK_SENSITIVE)
    summary_r3 = reward_summary(ref_y_true, ref_y_pred, scheme=R3_STRONG_ATTACK_SENSITIVE)
    print(f"[OK] R2 summary -> mean_reward={summary_r2['mean_reward']:.6f}, "
          f"total_reward={summary_r2['total_reward']:.0f}")
    print(f"[OK] R3 summary -> mean_reward={summary_r3['mean_reward']:.6f}, "
          f"total_reward={summary_r3['total_reward']:.0f}")
    assert abs(summary_r2["mean_reward"] - 0.695880) < 1e-5, summary_r2["mean_reward"]
    assert abs(summary_r3["mean_reward"] - 0.622213) < 1e-5, summary_r3["mean_reward"]
    assert summary_r2["total_reward"] == 140334.0, summary_r2["total_reward"]
    assert summary_r3["total_reward"] == 125478.0, summary_r3["total_reward"]
    print("[OK] R2/R3 mean/total reward also match master handoff section 23 EXACTLY")

    # 6. R1 must have the highest mean reward among the three (justifies selection).
    assert summary_r1["mean_reward"] > summary_r2["mean_reward"] > summary_r3["mean_reward"]
    print("[OK] R1 > R2 > R3 in mean reward, consistent with R1 being selected")

    # --- input validation ---------------------------------------------------
    # 7. Non-binary labels raise.
    try:
        compute_reward(np.array([0, 1, 2]), np.array([0, 1, 1]))
        raise AssertionError("Expected ValueError for non-binary y_true")
    except ValueError:
        print("[OK] compute_reward rejects non-binary y_true")

    # 8. Mismatched shapes raise.
    try:
        compute_reward(np.array([0, 1, 1]), np.array([0, 1]))
        raise AssertionError("Expected ValueError for mismatched shapes")
    except ValueError:
        print("[OK] compute_reward rejects mismatched y_true/y_pred shapes")

    # 9. Empty input raises.
    try:
        compute_reward(np.array([]), np.array([]))
        raise AssertionError("Expected ValueError for empty input")
    except ValueError:
        print("[OK] compute_reward rejects empty input")

    # 10. Scalar wrapper rejects invalid labels.
    try:
        compute_reward_scalar(2, 1)
        raise AssertionError("Expected ValueError for invalid scalar y_true")
    except ValueError:
        print("[OK] compute_reward_scalar rejects invalid scalar labels")

    print("\nAll reward.py checks passed.")


if __name__ == "__main__":
    main()