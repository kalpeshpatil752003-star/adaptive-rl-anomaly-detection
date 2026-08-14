"""
src/rl/state.py

State construction module for the Adaptive RL Network Anomaly Detection
project.

Implements the experimentally-selected S3 state representation
(14 dimensions, see MASTER HANDOFF PROMPT sections 14-16 / 25 and
RL_Experiment_Summary section 7-8):

    [0:4]   Percentile-normalized anomaly scores
            IF, LOF, OCSVM, AutoEncoder  (fixed order)
    [4:9]   Disagreement statistics over those 4 normalized scores
            score_mean, score_std, score_min, score_max, score_range
    [9:14]  Five mutual-information-selected traffic-context features
            Average Packet Size, Packet Length Variance, Packet Length Std,
            Packet Length Mean, Avg Bwd Segment Size

This module ONLY builds the state vector. It intentionally does NOT:
    - train or load anomaly detectors
    - compute rewards or actions
    - touch the final test set
    - hardcode any filesystem paths

The S3 definition is frozen. Do not change model order, disagreement
statistics, or traffic feature selection here without updating the
experiment log and getting confirmation (see MASTER HANDOFF section 32,
"data-leakage / do-not-change" rules).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Frozen design constants. See experiment sections 10 (normalization),
# 14-16 (state), of the master handoff. DO NOT EDIT casually.
# ---------------------------------------------------------------------------

MODEL_ORDER: tuple = ("isolation_forest", "lof", "ocsvm", "autoencoder")

DISAGREEMENT_STAT_NAMES: tuple = (
    "score_mean",
    "score_std",
    "score_min",
    "score_max",
    "score_range",
)

# Mutual-information-selected traffic features (chosen on development data
# only -- see master handoff section 14 / summary section 7).
TRAFFIC_FEATURE_NAMES: tuple = (
    "Average Packet Size",
    "Packet Length Variance",
    "Packet Length Std",
    "Packet Length Mean",
    "Avg Bwd Segment Size",
)

STATE_FEATURE_NAMES: tuple = (
    tuple(f"{m}_score_pct" for m in MODEL_ORDER)
    + DISAGREEMENT_STAT_NAMES
    + TRAFFIC_FEATURE_NAMES
)

STATE_DIM = len(STATE_FEATURE_NAMES)
assert STATE_DIM == 14, "S3 state definition has drifted from the frozen 14-d spec"


class PercentileNormalizer:
    """
    Rank/percentile normalizer for a single detector's raw anomaly scores.

    Percentile normalization was experimentally selected over min-max
    normalization (master handoff section 10: percentile beat min-max on
    F1/ROC-AUC/PR-AUC for the equal-weight ensemble). It maps a raw score to
    the percentile rank it would occupy within a fixed reference
    distribution, putting every detector on a comparable [0, 1] scale
    regardless of native range (e.g. LOF scores spanning thousands vs. IF
    scores below 1).

    The reference distribution must come from validation/development data,
    never from the final test set (master handoff section 32).
    """

    def __init__(self) -> None:
        self._reference_sorted: np.ndarray | None = None

    def fit(self, reference_scores: np.ndarray) -> "PercentileNormalizer":
        reference_scores = np.asarray(reference_scores, dtype=np.float64).ravel()
        if reference_scores.size == 0:
            raise ValueError("reference_scores must be non-empty")
        if not np.all(np.isfinite(reference_scores)):
            raise ValueError("reference_scores contains NaN/inf values")
        self._reference_sorted = np.sort(reference_scores)
        return self

    @property
    def is_fitted(self) -> bool:
        return self._reference_sorted is not None

    def transform(self, raw_scores: np.ndarray) -> np.ndarray:
        if not self.is_fitted:
            raise RuntimeError("PercentileNormalizer must be fit() before transform()")
        raw_scores = np.asarray(raw_scores, dtype=np.float64)
        ref = self._reference_sorted
        ranks = np.searchsorted(ref, raw_scores, side="right")
        pct = ranks / len(ref)
        return np.clip(pct, 0.0, 1.0)

    def fit_transform(self, reference_scores: np.ndarray) -> np.ndarray:
        return self.fit(reference_scores).transform(reference_scores)

    def get_reference(self) -> np.ndarray:
        """Return the fitted, sorted reference array (for persistence)."""
        if not self.is_fitted:
            raise RuntimeError("PercentileNormalizer is not fitted")
        return self._reference_sorted.copy()

    def set_reference(self, sorted_reference: np.ndarray) -> "PercentileNormalizer":
        """Restore a previously-fitted, sorted reference array."""
        sorted_reference = np.asarray(sorted_reference, dtype=np.float64)
        if sorted_reference.ndim != 1 or sorted_reference.size == 0:
            raise ValueError("sorted_reference must be a non-empty 1D array")
        self._reference_sorted = sorted_reference
        return self


@dataclass
class StateBuilderConfig:
    """Configuration for S3StateBuilder. Defaults match the frozen S3 spec."""

    model_order: Sequence[str] = MODEL_ORDER
    traffic_feature_names: Sequence[str] = TRAFFIC_FEATURE_NAMES
    disagreement_stat_names: Sequence[str] = DISAGREEMENT_STAT_NAMES


class S3StateBuilder:
    """
    Builds the frozen 14-dimensional S3 state for the RL ensemble agent.

    This class holds one PercentileNormalizer per detector. Normalizers must
    be fit once on validation/development scores (never on the final test
    set), after which `build()` can be called repeatedly -- including
    per-step inside the eventual RL environment -- to produce state vectors
    for new batches of raw scores + traffic features.

    Example
    -------
    >>> builder = S3StateBuilder()
    >>> builder.fit_normalizers({
    ...     "isolation_forest": val_if_scores,
    ...     "lof": val_lof_scores,
    ...     "ocsvm": val_ocsvm_scores,
    ...     "autoencoder": val_ae_scores,
    ... })
    >>> state = builder.build(
    ...     raw_scores={
    ...         "isolation_forest": if_scores,
    ...         "lof": lof_scores,
    ...         "ocsvm": ocsvm_scores,
    ...         "autoencoder": ae_scores,
    ...     },
    ...     traffic_features=traffic_df,
    ... )
    >>> state.shape
    (n_samples, 14)
    """

    feature_names: tuple = STATE_FEATURE_NAMES
    state_dim: int = STATE_DIM

    def __init__(self, config: StateBuilderConfig | None = None) -> None:
        self.config = config or StateBuilderConfig()
        self._normalizers: dict = {
            name: PercentileNormalizer() for name in self.config.model_order
        }

    # -- fitting --------------------------------------------------------

    def fit_normalizers(self, reference_scores: Mapping[str, np.ndarray]) -> "S3StateBuilder":
        """Fit percentile normalizers on validation/development scores only."""
        self._validate_model_keys(reference_scores, arg_name="reference_scores")
        for name in self.config.model_order:
            self._normalizers[name].fit(np.asarray(reference_scores[name]))
        return self

    @property
    def is_fitted(self) -> bool:
        return all(n.is_fitted for n in self._normalizers.values())

    # -- persistence ------------------------------------------------------

    def get_normalizer_state(self) -> dict:
        """Return a picklable dict of fitted reference arrays, keyed by model
        name. Caller decides how/where to persist it (e.g. via joblib.dump
        to evaluation_results/rl_states/normalizers.joblib) -- this module
        does not hardcode any path."""
        return {name: n.get_reference() for name, n in self._normalizers.items()}

    def load_normalizer_state(self, state: Mapping[str, np.ndarray]) -> "S3StateBuilder":
        """Restore normalizers from a dict produced by get_normalizer_state()."""
        self._validate_model_keys(state, arg_name="state")
        for name in self.config.model_order:
            self._normalizers[name].set_reference(state[name])
        return self

    # -- building ---------------------------------------------------------

    def build(
        self,
        raw_scores: Mapping[str, np.ndarray],
        traffic_features: pd.DataFrame,
    ) -> np.ndarray:
        """
        Construct the S3 state matrix.

        Parameters
        ----------
        raw_scores : mapping of model_name -> 1D array of raw anomaly
            scores (one entry per sample) for each name in MODEL_ORDER.
        traffic_features : DataFrame containing at least the columns in
            TRAFFIC_FEATURE_NAMES, with rows aligned 1:1 to raw_scores.

        Returns
        -------
        np.ndarray of shape (n_samples, 14), dtype float32, column order
        given by S3StateBuilder.feature_names / STATE_FEATURE_NAMES.
        """
        if not self.is_fitted:
            raise RuntimeError(
                "S3StateBuilder normalizers are not fitted. Call "
                "fit_normalizers() with validation/development scores first."
            )
        self._validate_model_keys(raw_scores, arg_name="raw_scores")
        self._validate_traffic_features(traffic_features)

        n_samples = self._infer_n_samples(raw_scores)
        if len(traffic_features) != n_samples:
            raise ValueError(
                f"traffic_features has {len(traffic_features)} rows but "
                f"raw_scores implies {n_samples} samples"
            )

        # 1) percentile-normalized scores, in fixed model order -> (n, 4)
        normalized = np.column_stack(
            [
                self._normalizers[name].transform(np.asarray(raw_scores[name]))
                for name in self.config.model_order
            ]
        )

        # 2) disagreement statistics over the 4 normalized scores -> (n, 5)
        score_min = normalized.min(axis=1)
        score_max = normalized.max(axis=1)
        disagreement = np.column_stack(
            [
                normalized.mean(axis=1),
                normalized.std(axis=1),
                score_min,
                score_max,
                score_max - score_min,
            ]
        )

        # 3) traffic context, in fixed feature order -> (n, 5)
        traffic = traffic_features.loc[:, list(self.config.traffic_feature_names)].to_numpy(
            dtype=np.float64
        )

        state = np.concatenate([normalized, disagreement, traffic], axis=1).astype(np.float32)
        self._validate_output_shape(state, n_samples)
        return state

    def build_as_frame(
        self,
        raw_scores: Mapping[str, np.ndarray],
        traffic_features: pd.DataFrame,
    ) -> pd.DataFrame:
        """Same as build(), but returns a labeled DataFrame for inspection/debugging."""
        state = self.build(raw_scores, traffic_features)
        return pd.DataFrame(state, columns=self.feature_names)

    # -- validation helpers -------------------------------------------------

    def _validate_model_keys(self, mapping: Mapping[str, np.ndarray], arg_name: str) -> None:
        missing = [m for m in self.config.model_order if m not in mapping]
        if missing:
            raise KeyError(f"{arg_name} is missing required model(s): {missing}")

    def _validate_traffic_features(self, traffic_features: pd.DataFrame) -> None:
        if not isinstance(traffic_features, pd.DataFrame):
            raise TypeError("traffic_features must be a pandas DataFrame")
        missing = [
            c for c in self.config.traffic_feature_names if c not in traffic_features.columns
        ]
        if missing:
            raise KeyError(f"traffic_features is missing required column(s): {missing}")

    def _infer_n_samples(self, raw_scores: Mapping[str, np.ndarray]) -> int:
        lengths = {name: len(np.asarray(raw_scores[name])) for name in self.config.model_order}
        if len(set(lengths.values())) != 1:
            raise ValueError(f"raw_scores arrays have mismatched lengths: {lengths}")
        return next(iter(lengths.values()))

    def _validate_output_shape(self, state: np.ndarray, n_samples: int) -> None:
        expected = (n_samples, self.state_dim)
        if state.shape != expected:
            raise AssertionError(f"Built state has shape {state.shape}, expected {expected}")