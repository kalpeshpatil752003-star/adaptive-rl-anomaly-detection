"""
src/rl/reward.py

Reward computation module for the Adaptive RL Network Anomaly Detection
project.

Implements the experimentally-selected R1 reward function (master handoff
sections 22-25 / RL_Experiment_Summary sections 13-14):

    TP = +1
    TN = +1
    FP = -1
    FN = -1

R1 was chosen over R2 (FN=-2) and R3 (FN=-3) because it produced the
highest mean/total reward on the reference confusion matrix -- it was NOT
an arbitrary "penalize false negatives heavily" choice (master handoff
section 23).

Binary label convention (must match master handoff section 4):
    0 = BENIGN / Normal
    1 = Attack / Anomaly

This module ONLY computes reward from already-binary (y_true, y_pred)
pairs. It does not threshold ensemble scores into predictions and does not
run models -- that belongs to score_combiner / environment.py.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple

import numpy as np


@dataclass(frozen=True)
class RewardScheme:
    """A single (TP, TN, FP, FN) reward assignment."""

    tp: float
    tn: float
    fp: float
    fn: float
    name: str = ""


# ---------------------------------------------------------------------------
# All three experimentally-compared schemes are kept here for reference and
# for regression-testing the selection (section 23), but FINAL_REWARD_SCHEME
# is the only one that should be used by environment.py / trainer.py.
# Changing FINAL_REWARD_SCHEME requires updating the experiment log and
# getting confirmation -- see master handoff section 32.
# ---------------------------------------------------------------------------

R1_BALANCED = RewardScheme(tp=1.0, tn=1.0, fp=-1.0, fn=-1.0, name="R1_balanced")
R2_ATTACK_SENSITIVE = RewardScheme(tp=1.0, tn=1.0, fp=-1.0, fn=-2.0, name="R2_attack_sensitive")
R3_STRONG_ATTACK_SENSITIVE = RewardScheme(
    tp=1.0, tn=1.0, fp=-1.0, fn=-3.0, name="R3_strong_attack_sensitive"
)

FINAL_REWARD_SCHEME: RewardScheme = R1_BALANCED


class ConfusionCounts(NamedTuple):
    tp: int
    tn: int
    fp: int
    fn: int


def _validate_binary(labels: np.ndarray, arg_name: str) -> np.ndarray:
    if labels.size == 0:
        raise ValueError(f"{arg_name} must be non-empty")
    if not np.all(np.isfinite(labels)):
        raise ValueError(f"{arg_name} contains NaN/inf values")
    unique = np.unique(labels)
    if not np.all(np.isin(unique, [0, 1])):
        raise ValueError(f"{arg_name} must contain only 0/1 values, got unique={unique}")
    return labels.astype(np.int64)


def compute_reward(
    y_true,
    y_pred,
    scheme: RewardScheme = FINAL_REWARD_SCHEME,
) -> np.ndarray:
    """
    Compute the per-sample reward for a batch of (y_true, y_pred).

    Parameters
    ----------
    y_true : array-like of {0, 1}, ground truth (0=benign, 1=attack).
    y_pred : array-like of {0, 1}, ensemble prediction after thresholding.
    scheme : RewardScheme, defaults to the frozen R1 scheme. Only pass a
        different scheme for controlled comparison/benchmarking (e.g.
        reproducing section 23) -- production training must use R1.

    Returns
    -------
    np.ndarray of float32 rewards, shape matching y_true/y_pred.
    """
    y_true = _validate_binary(np.asarray(y_true), "y_true")
    y_pred = _validate_binary(np.asarray(y_pred), "y_pred")
    if y_true.shape != y_pred.shape:
        raise ValueError(f"y_true shape {y_true.shape} != y_pred shape {y_pred.shape}")

    reward = np.empty(y_true.shape, dtype=np.float32)

    tp_mask = (y_true == 1) & (y_pred == 1)
    tn_mask = (y_true == 0) & (y_pred == 0)
    fp_mask = (y_true == 0) & (y_pred == 1)
    fn_mask = (y_true == 1) & (y_pred == 0)

    reward[tp_mask] = scheme.tp
    reward[tn_mask] = scheme.tn
    reward[fp_mask] = scheme.fp
    reward[fn_mask] = scheme.fn

    return reward


def compute_reward_scalar(
    y_true: int,
    y_pred: int,
    scheme: RewardScheme = FINAL_REWARD_SCHEME,
) -> float:
    """
    Single-sample convenience wrapper for step-wise use inside the RL
    environment loop (one traffic flow -> one prediction -> one reward).
    """
    if y_true not in (0, 1):
        raise ValueError(f"y_true must be 0 or 1, got {y_true}")
    if y_pred not in (0, 1):
        raise ValueError(f"y_pred must be 0 or 1, got {y_pred}")

    if y_true == 1 and y_pred == 1:
        return scheme.tp
    if y_true == 0 and y_pred == 0:
        return scheme.tn
    if y_true == 0 and y_pred == 1:
        return scheme.fp
    return scheme.fn  # y_true == 1 and y_pred == 0


def confusion_counts(y_true, y_pred) -> ConfusionCounts:
    """Return TP/TN/FP/FN counts for a batch of (y_true, y_pred)."""
    y_true = _validate_binary(np.asarray(y_true), "y_true")
    y_pred = _validate_binary(np.asarray(y_pred), "y_pred")
    if y_true.shape != y_pred.shape:
        raise ValueError(f"y_true shape {y_true.shape} != y_pred shape {y_pred.shape}")

    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    return ConfusionCounts(tp=tp, tn=tn, fp=fp, fn=fn)


def reward_summary(
    y_true,
    y_pred,
    scheme: RewardScheme = FINAL_REWARD_SCHEME,
) -> dict:
    """
    Summarize reward + confusion counts for a batch, in the same format used
    to report the reward experiment (master handoff section 23):
    mean_reward, total_reward, and the underlying TP/TN/FP/FN counts.
    """
    reward = compute_reward(y_true, y_pred, scheme=scheme)
    counts = confusion_counts(y_true, y_pred)
    return {
        "scheme": scheme.name,
        "mean_reward": float(reward.mean()),
        "total_reward": float(reward.sum()),
        "n_samples": int(reward.size),
        "tp": counts.tp,
        "tn": counts.tn,
        "fp": counts.fp,
        "fn": counts.fn,
    }