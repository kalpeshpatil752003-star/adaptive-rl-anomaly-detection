"""
src/rl/action.py

Action construction module for the Adaptive RL Network Anomaly Detection
project.

Implements the experimentally-selected A3 action design (master handoff
sections 17-21 / RL_Experiment_Summary sections 9-12):

    action = [w_IF, w_LOF, w_OCSVM, w_AE]
    subject to: all w_i >= 0, sum(w_i) = 1

Detector order is NOT redefined here. It is imported directly from
src/rl/state.py's MODEL_ORDER, which is the single source of truth, since
the RL agent's state score columns [0:4] and this module's action weight
columns are positionally aligned to the same four detectors:

    ┌───────┬───────────┐
    │ Index │ Detector  │
    ├───────┼───────────┤
    │ 0     │ IF        │
    │ 1     │ LOF       │
    │ 2     │ OCSVM     │
    │ 3     │ AE        │
    └───────┴───────────┘

This module ONLY converts raw agent output into a valid action (weight
vector). It does not run models, combine scores, or compute reward -- that
is environment.py / score_combiner's job.
"""

from __future__ import annotations

from typing import Mapping

import numpy as np

from .state import MODEL_ORDER  # single source of truth for detector order

# ---------------------------------------------------------------------------
# Frozen design constant. Re-exported under the name used in the action
# experiments for readability. MUST stay identical to state.MODEL_ORDER --
# do not redefine this tuple independently anywhere in the project.
# ---------------------------------------------------------------------------
DETECTOR_NAMES: tuple = MODEL_ORDER

assert DETECTOR_NAMES == ("isolation_forest", "lof", "ocsvm", "autoencoder"), (
    "action.py DETECTOR_NAMES has drifted from the frozen state.py MODEL_ORDER"
)

ACTION_DIM = len(DETECTOR_NAMES)  # 4

_WEIGHT_SUM_TOLERANCE = 1e-5


class ActionProjector:
    """
    Projects raw RL agent output into a valid A3 action: a length-4 vector
    of non-negative detector weights summing to 1, in DETECTOR_NAMES order.

    Two projection methods are supported:

    - "softmax" (default): raw_action is treated as unconstrained logits.
      Numerically stable (max-subtracted) exp/sum. Always yields strictly
      positive weights and is differentiable end-to-end, which suits
      continuous-control actors (DDPG/TD3/SAC) that emit unconstrained
      logits directly -- no separate clipping/fallback logic needed.

    - "relu_normalize": raw_action is treated as already weight-like.
      Negative values are clipped to 0, then the vector is renormalized to
      sum to 1. If every value clips to 0 (all raw inputs <= 0), falls back
      to a uniform 1/4 weight vector so the output is always a valid point
      on the simplex -- never NaN, never all-zero.

    Both methods accept a single action (shape (4,)) or a batch of actions
    (shape (batch, 4)); projection is applied along the last axis.
    """

    def __init__(self, method: str = "softmax") -> None:
        if method not in ("softmax", "relu_normalize"):
            raise ValueError(f"Unknown projection method: {method!r}")
        self.method = method

    def project(self, raw_action) -> np.ndarray:
        raw_action = np.asarray(raw_action, dtype=np.float64)
        self._validate_raw_shape(raw_action)

        if self.method == "softmax":
            weights = self._softmax(raw_action)
        else:
            weights = self._relu_normalize(raw_action)

        weights = weights.astype(np.float32)
        validate_weights(weights)
        return weights

    # -- projection implementations ----------------------------------------

    @staticmethod
    def _softmax(raw_action: np.ndarray) -> np.ndarray:
        shifted = raw_action - np.max(raw_action, axis=-1, keepdims=True)
        exp = np.exp(shifted)
        return exp / exp.sum(axis=-1, keepdims=True)

    @staticmethod
    def _relu_normalize(raw_action: np.ndarray) -> np.ndarray:
        clipped = np.clip(raw_action, a_min=0.0, a_max=None)
        totals = clipped.sum(axis=-1, keepdims=True)

        # Wherever the row sums to ~0 (all inputs were <= 0), fall back to
        # a uniform weight vector instead of dividing by zero.
        degenerate = np.squeeze(totals, axis=-1) <= _WEIGHT_SUM_TOLERANCE
        uniform = np.full_like(clipped, 1.0 / clipped.shape[-1])

        safe_totals = np.where(totals <= _WEIGHT_SUM_TOLERANCE, 1.0, totals)
        normalized = clipped / safe_totals

        if clipped.ndim == 1:
            return uniform if degenerate else normalized
        return np.where(degenerate[..., None], uniform, normalized)

    # -- validation ----------------------------------------------------------

    def _validate_raw_shape(self, raw_action: np.ndarray) -> None:
        if raw_action.ndim not in (1, 2):
            raise ValueError(
                f"raw_action must be 1D (single action) or 2D (batch), got "
                f"shape {raw_action.shape}"
            )
        if raw_action.shape[-1] != ACTION_DIM:
            raise ValueError(
                f"raw_action last dimension must be {ACTION_DIM} "
                f"(one value per detector: {DETECTOR_NAMES}), got "
                f"shape {raw_action.shape}"
            )
        if not np.all(np.isfinite(raw_action)):
            raise ValueError("raw_action contains NaN/inf values")


def validate_weights(weights: np.ndarray) -> None:
    """
    Validate that `weights` is a legal A3 action: correct shape, all
    non-negative, and each row sums to 1 within tolerance.

    Raises ValueError on violation. Used internally by ActionProjector and
    intended for reuse by environment.py when checking externally-supplied
    or replay-buffer-stored actions.
    """
    weights = np.asarray(weights)
    if weights.shape[-1] != ACTION_DIM:
        raise ValueError(
            f"weights last dimension must be {ACTION_DIM}, got shape {weights.shape}"
        )
    if not np.all(np.isfinite(weights)):
        raise ValueError("weights contains NaN/inf values")
    if np.any(weights < -_WEIGHT_SUM_TOLERANCE):
        raise ValueError(f"weights must be non-negative, got min={weights.min()}")
    sums = weights.sum(axis=-1)
    if not np.allclose(sums, 1.0, atol=_WEIGHT_SUM_TOLERANCE):
        bad = sums[np.abs(sums - 1.0) > _WEIGHT_SUM_TOLERANCE]
        raise ValueError(f"weights must sum to 1 along the last axis, got sums e.g. {bad[:5]}")


def weights_to_dict(weights: np.ndarray) -> Mapping[str, float]:
    """Convert a single (shape (4,)) weight vector into a
    {detector_name: weight} dict, in DETECTOR_NAMES order."""
    weights = np.asarray(weights)
    if weights.ndim != 1 or weights.shape[0] != ACTION_DIM:
        raise ValueError(
            f"weights_to_dict expects a single 1D vector of length {ACTION_DIM}, "
            f"got shape {weights.shape}. For batches, iterate and call per-row."
        )
    return {name: float(w) for name, w in zip(DETECTOR_NAMES, weights)}


def dict_to_weights(weights_dict: Mapping[str, float]) -> np.ndarray:
    """Convert a {detector_name: weight} dict back into the fixed-order
    weight vector expected everywhere else (state.py, environment.py)."""
    missing = [name for name in DETECTOR_NAMES if name not in weights_dict]
    if missing:
        raise KeyError(f"weights_dict is missing required detector(s): {missing}")
    weights = np.array([weights_dict[name] for name in DETECTOR_NAMES], dtype=np.float32)
    validate_weights(weights)
    return weights