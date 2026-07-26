"""
Isolation Forest model wrapper for the Adaptive RL Anomaly Detection framework.

Responsibilities
----------------
- Train an Isolation Forest model.
- Produce anomaly scores.
- Produce binary predictions.
- Save/load trained models.
- Provide a common interface for the ensemble.

Author: Adaptive RL Framework
"""

from __future__ import annotations

from pathlib import Path
import time
from typing import Optional

import numpy as np
from sklearn.ensemble import IsolationForest

from src.config.isolation_forest_config import IsolationForestConfig
from src.models.base_model import BaseAnomalyModel
from src.utils.logger import get_logger

logger = get_logger(__name__)


class IsolationForestModel(BaseAnomalyModel):
    """
    Wrapper around sklearn IsolationForest.

    Notes
    -----
    decision_function() and score_samples() return larger values for more
    normal samples. This wrapper inverts score_samples() so larger scores
    consistently indicate more anomalous samples across ensemble models.
    """

    def __init__(
        self,
        config: Optional[IsolationForestConfig] = None,
    ) -> None:
        self.config = config or IsolationForestConfig()
        super().__init__(
            model_name="IsolationForest",
            random_state=self.config.random_state,
        )

        self._model = IsolationForest(
            n_estimators=self.config.n_estimators,
            contamination=self.config.contamination,
            max_samples=self.config.max_samples,
            max_features=self.config.max_features,
            bootstrap=self.config.bootstrap,
            random_state=self.config.random_state,
            n_jobs=self.config.n_jobs,
            verbose=self.config.verbose,
        )

    def fit(self, X: np.ndarray) -> "IsolationForestModel":
        """Train the Isolation Forest and update training metadata."""
        X = self._validate_input(X)

        logger.info("Training Isolation Forest...")
        logger.info("Training samples: %d", len(X))

        start_time = time.perf_counter()
        self._model.fit(X)
        self._set_fitted(
            n_features=X.shape[1],
            training_time=time.perf_counter() - start_time,
        )

        logger.info("Isolation Forest training completed.")
        return self

    def anomaly_score(self, X: np.ndarray) -> np.ndarray:
        """
        Return anomaly scores where larger values indicate more anomalous data.
        """
        self._check_is_fitted()
        X = self._validate_input(X)

        return -self._model.score_samples(X)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict binary anomaly labels: 1 for anomaly and 0 for normal.
        """
        self._check_is_fitted()
        X = self._validate_input(X)

        predictions = self._model.predict(X)
        return np.where(predictions == -1, 1, 0)

    def normalized_scores(self, X: np.ndarray) -> np.ndarray:
        """Normalize anomaly scores to the [0, 1] interval."""
        scores = self.anomaly_score(X)
        minimum = scores.min()
        maximum = scores.max()

        if maximum == minimum:
            return np.zeros_like(scores)

        return (scores - minimum) / (maximum - minimum)

    def save(self, filepath: str | Path) -> None:
        """Persist the wrapper, estimator, configuration, and metadata."""
        super().save(filepath)
        logger.info("Isolation Forest saved -> %s", filepath)

    @classmethod
    def load(cls, filepath: str | Path) -> "IsolationForestModel":
        """Load a previously saved Isolation Forest wrapper."""
        model = super().load(filepath)

        if not isinstance(model, cls):
            raise TypeError(
                f"Expected a saved {cls.__name__}, got {type(model).__name__}."
            )

        logger.info("Isolation Forest loaded <- %s", filepath)
        return model

    @property
    def estimator(self) -> IsolationForest:
        """Return the underlying scikit-learn estimator."""
        return self._model

    def __repr__(self) -> str:
        return (
            "IsolationForestModel("
            f"n_estimators={self.config.n_estimators}, "
            f"contamination={self.config.contamination}, "
            f"is_fitted={self.is_fitted})"
        )
