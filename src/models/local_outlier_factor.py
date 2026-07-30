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
        super().__init__(
            model_name="LocalOutlierFactor",
            random_state=config.random_state,
        )

        self.config = config

        self._model = LocalOutlierFactor(
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

    def fit(self, X, y=None):
        """
        Train the LOF model.
        """

        X = self._validate_input(X)
        if len(X) > self.config.max_training_samples:
            logger.warning(
                "Sampling %d rows for Local Outlier Factor training.",
                self.config.max_training_samples,
            )
        
            rng = np.random.default_rng(self.config.random_state)
        
            indices = rng.choice(
                len(X),
                self.config.max_training_samples,
                replace=False,
            )
        
            X = X[indices]

        logger.info("Training Local Outlier Factor...")

        self._model.fit(X, y)
        self.training_samples = X.shape[0]
        self.training_features = X.shape[1]

        self._set_fitted(True)

        logger.info("Training completed.")
        return self

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

        predictions = self._model.predict(X)

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

        scores = -self._model.decision_function(X)

        return scores

    @property
    def estimator(self) -> LocalOutlierFactor:
        """
        Return the underlying sklearn estimator.
        """
        return self._model
        
    

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

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"n_neighbors={self.config.n_neighbors}, "
            f"contamination={self.config.contamination}, "
            f"novelty={self.config.novelty})"
        )