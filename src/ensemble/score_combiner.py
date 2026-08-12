"""
Score combination utilities for anomaly detection ensembles.
"""

from __future__ import annotations

from typing import Mapping

import numpy as np


class ScoreCombiner:
    """
    Normalize and combine anomaly scores from multiple detectors.

    The combiner is intentionally independent of any specific model.
    It can therefore be reused by both static and RL-based ensembles.

    Supported models:
        - if
        - lof
        - svm
        - ae

    Supported normalization methods:
        - raw
        - minmax
        - percentile
    """

    MODEL_NAMES = ("if", "lof", "svm", "ae")
    NORMALIZATIONS = ("raw", "minmax", "percentile")

    def __init__(
        self,
        weights: Mapping[str, float],
        normalization: str = "minmax",
    ) -> None:

        self.weights = dict(weights)
        self.normalization = normalization

        self._validate_weights()
        self._validate_normalization()

        # Parameters learned from development/validation data.
        self._min_values: dict[str, float] = {}
        self._max_values: dict[str, float] = {}
        self._sorted_scores: dict[str, np.ndarray] = {}

        self.is_fitted = False

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def _validate_weights(self) -> None:
        """Validate ensemble weights."""

        if set(self.weights.keys()) != set(self.MODEL_NAMES):
            raise ValueError(
                "Weights must contain exactly these model names: "
                f"{self.MODEL_NAMES}. Got: {tuple(self.weights.keys())}"
            )

        for model_name, weight in self.weights.items():
            if not np.isfinite(weight):
                raise ValueError(
                    f"Weight for '{model_name}' must be finite, got {weight}."
                )

            if weight < 0.0:
                raise ValueError(
                    f"Weight for '{model_name}' must be non-negative, "
                    f"got {weight}."
                )

        total = float(sum(self.weights.values()))

        if not np.isclose(total, 1.0, atol=1e-6):
            raise ValueError(
                f"Ensemble weights must sum to 1.0, got {total:.8f}."
            )

    def _validate_normalization(self) -> None:
        """Validate normalization strategy."""

        if self.normalization not in self.NORMALIZATIONS:
            raise ValueError(
                f"Unsupported normalization '{self.normalization}'. "
                f"Expected one of {self.NORMALIZATIONS}."
            )

    @classmethod
    def _validate_scores(
        cls,
        scores: Mapping[str, np.ndarray],
    ) -> int:
        """Validate score arrays and return the number of samples."""

        if set(scores.keys()) != set(cls.MODEL_NAMES):
            raise ValueError(
                "Scores must contain exactly these model names: "
                f"{cls.MODEL_NAMES}. Got: {tuple(scores.keys())}"
            )

        arrays = {}

        for model_name in cls.MODEL_NAMES:
            values = np.asarray(scores[model_name])

            if values.ndim != 1:
                raise ValueError(
                    f"Scores for '{model_name}' must be 1-dimensional, "
                    f"got shape {values.shape}."
                )

            if not np.issubdtype(values.dtype, np.number):
                raise ValueError(
                    f"Scores for '{model_name}' must be numeric."
                )

            if not np.all(np.isfinite(values)):
                raise ValueError(
                    f"Scores for '{model_name}' contain NaN or Inf."
                )

            arrays[model_name] = values

        lengths = {
            model_name: len(values)
            for model_name, values in arrays.items()
        }

        if len(set(lengths.values())) != 1:
            raise ValueError(
                f"All score arrays must have the same length. "
                f"Got: {lengths}"
            )

        return next(iter(lengths.values()))

    # ------------------------------------------------------------------
    # Fitting normalization parameters
    # ------------------------------------------------------------------

    def fit(
        self,
        scores: Mapping[str, np.ndarray],
    ) -> "ScoreCombiner":
        """
        Fit normalization parameters using development/validation scores.

        IMPORTANT:
            This should be fitted on development/validation data,
            not the final test set.

        Args:
            scores:
                Dictionary containing score arrays for all four models.

        Returns:
            Self.
        """

        self._validate_scores(scores)

        for model_name in self.MODEL_NAMES:
            values = np.asarray(scores[model_name], dtype=np.float64)

            if self.normalization == "minmax":
                self._min_values[model_name] = float(np.min(values))
                self._max_values[model_name] = float(np.max(values))

            elif self.normalization == "percentile":
                self._sorted_scores[model_name] = np.sort(values)

        self.is_fitted = True

        return self

    # ------------------------------------------------------------------
    # Normalization
    # ------------------------------------------------------------------

    @staticmethod
    def _minmax_transform(
        values: np.ndarray,
        minimum: float,
        maximum: float,
    ) -> np.ndarray:
        """Apply min-max normalization."""

        denominator = maximum - minimum

        if np.isclose(denominator, 0.0):
            return np.zeros_like(values, dtype=np.float64)

        return (values - minimum) / denominator

    @staticmethod
    def _percentile_transform(
        values: np.ndarray,
        reference_sorted: np.ndarray,
    ) -> np.ndarray:
        """
        Convert values to empirical percentile scores in [0, 1].
        """

        if len(reference_sorted) == 0:
            return np.zeros_like(values, dtype=np.float64)

        positions = np.searchsorted(
            reference_sorted,
            values,
            side="right",
        )

        return positions / len(reference_sorted)

    def _normalize(
        self,
        model_name: str,
        values: np.ndarray,
    ) -> np.ndarray:
        """Normalize one model's scores."""

        values = np.asarray(values, dtype=np.float64)

        if self.normalization == "raw":
            return values

        if not self.is_fitted:
            raise RuntimeError(
                "ScoreCombiner must be fitted before using "
                f"normalization='{self.normalization}'."
            )

        if self.normalization == "minmax":
            return self._minmax_transform(
                values,
                self._min_values[model_name],
                self._max_values[model_name],
            )

        if self.normalization == "percentile":
            return self._percentile_transform(
                values,
                self._sorted_scores[model_name],
            )

        raise RuntimeError(
            f"Unsupported normalization: {self.normalization}"
        )

    # ------------------------------------------------------------------
    # Combination
    # ------------------------------------------------------------------

    def transform(
        self,
        scores: Mapping[str, np.ndarray],
    ) -> dict[str, np.ndarray]:
        """
        Normalize all model scores.

        Returns:
            Dictionary containing normalized scores.
        """

        self._validate_scores(scores)

        normalized = {}

        for model_name in self.MODEL_NAMES:
            normalized[model_name] = self._normalize(
                model_name,
                scores[model_name],
            )

        return normalized

    def combine(
        self,
        scores: Mapping[str, np.ndarray],
    ) -> np.ndarray:
        """
        Combine detector scores using configured weights.

        Returns:
            One-dimensional combined anomaly score.
        """

        normalized = self.transform(scores)

        combined = np.zeros(
            len(normalized["if"]),
            dtype=np.float64,
        )

        for model_name in self.MODEL_NAMES:
            combined += (
                self.weights[model_name]
                * normalized[model_name]
            )

        return combined

    def get_normalized_scores(
        self,
        scores: Mapping[str, np.ndarray],
    ) -> dict[str, np.ndarray]:
        """Public alias for transform()."""

        return self.transform(scores)

    def get_weights(self) -> dict[str, float]:
        """Return a copy of the configured weights."""

        return dict(self.weights)