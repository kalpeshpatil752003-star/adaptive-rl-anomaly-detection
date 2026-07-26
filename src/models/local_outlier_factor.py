"""
Local Outlier Factor (LOF) anomaly detection model.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from sklearn.neighbors import LocalOutlierFactor

from src.config.local_outlier_factor_config import LocalOutlierFactorConfig
from src.models.base_model import BaseAnomalyModel
from src.utils.logger import get_logger

logger = get_logger(__name__)


class LocalOutlierFactorModel(BaseAnomalyModel):
    """
    Wrapper around sklearn's Local Outlier Factor.

    The wrapper provides a unified interface for all anomaly
    detection models in the framework.

    Predictions
    ----------
    0 -> Normal
    1 -> Anomaly
    """

    def __init__(
        self,
        config: LocalOutlierFactorConfig,
    ) -> None:
        super().__init__()

        self.config = config

        self.model = LocalOutlierFactor(
            n_neighbors=config.n_neighbors,
            algorithm=config.algorithm,
            leaf_size=config.leaf_size,
            metric=config.metric,
            p=config.p,
            contamination=config.contamination,
            novelty=config.novelty,
            n_jobs=config.n_jobs,
        )

        logger.info("Local Outlier Factor initialized.")

    def fit(
        self,
        X,
    ) -> None:
        """
        Train the LOF model.
        """

        X = self._validate_input(X)

        logger.info("Training Local Outlier Factor...")

        self.model.fit(X)

        self.is_fitted = True

        logger.info("Training completed.")

    def predict(
        self,
        X,
    ) -> np.ndarray:
        """
        Predict anomalies.

        Returns
        -------
        ndarray

        0 -> Normal

        1 -> Anomaly
        """

        self._check_is_fitted()

        X = self._validate_input(X)

        predictions = self.model.predict(X)

        predictions = np.where(
            predictions == -1,
            1,
            0,
        )

        return predictions

    def anomaly_score(
        self,
        X,
    ) -> np.ndarray:
        """
        Compute anomaly scores.

        Larger score means more anomalous.
        """

        self._check_is_fitted()

        X = self._validate_input(X)

        scores = -self.model.decision_function(X)

        return scores

    def save(
        self,
        filepath: str | Path,
    ) -> None:
        """
        Save trained model.
        """

        super().save(filepath)

        logger.info(
            "Local Outlier Factor saved -> %s",
            filepath,
        )

    @classmethod
    def load(
        cls,
        filepath: str | Path,
    ) -> "LocalOutlierFactorModel":
        """
        Load a previously saved model.
        """

        model = super().load(filepath)

        if not isinstance(model, cls):
            raise TypeError(
                f"Expected {cls.__name__}, "
                f"got {type(model).__name__}."
            )

        logger.info(
            "Local Outlier Factor loaded <- %s",
            filepath,
        )

        return model