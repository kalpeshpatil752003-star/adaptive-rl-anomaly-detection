"""
One-Class SVM anomaly detection model.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from sklearn.svm import OneClassSVM

from src.config.one_class_svm_config import OneClassSVMConfig
from src.models.base_model import BaseAnomalyModel
from src.utils.logger import get_logger

logger = get_logger(__name__)


class OneClassSVMModel(BaseAnomalyModel):
    """
    Wrapper around sklearn's One-Class SVM.

    The wrapper provides a unified interface for all anomaly
    detection models in the framework.

    Predictions
    ----------
    0 -> Normal
    1 -> Anomaly
    """

    def __init__(
        self,
        config: OneClassSVMConfig,
    ) -> None:
        super().__init__(
            model_name="OneClassSVM",
            random_state=config.random_state,
        )

        self.config = config

        self._model = OneClassSVM(
            kernel=config.kernel,
            degree=config.degree,
            gamma=config.gamma,
            coef0=config.coef0,
            tol=config.tol,
            nu=config.nu,
            shrinking=config.shrinking,
            cache_size=config.cache_size,
            verbose=config.verbose,
            max_iter=config.max_iter,
        )

        logger.info("One-Class SVM initialized.")

    def fit(self, X: np.ndarray, y: np.ndarray | None = None)-> "OneClassSVMModel":
        """
        Train the One-Class SVM model.
        """

        X = self._validate_input(X)

        if len(X) > self.config.max_training_samples:
            logger.warning(
                "Dataset contains %d samples. "
                "Sampling %d rows for One-Class SVM training.",
                len(X),
                self.config.max_training_samples,
            )

            rng = np.random.default_rng(self.config.random_state)

            indices = rng.choice(
                len(X),
                self.config.max_training_samples,
                replace=False,
            )

            X = X[indices]

        logger.info("Training One-Class SVM...")

        self._model.fit(X, y)
        self.training_samples = X.shape[0]
        self.training_features = X.shape[1]
        logger.info(
            "Training samples: %d | Features: %d",
            self.training_samples,
            self.training_features,
        )

        self._set_fitted(True)

        logger.info("One-Class SVM training completed successfully.")
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
    def estimator(self) -> OneClassSVM:
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
            "One-Class SVM saved -> %s",
            filepath,
        )

    @classmethod
    def load(
        cls,
        filepath: str | Path,
    ) -> "OneClassSVMModel":
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
            "One-Class SVM loaded <- %s",
            filepath,
        )

        return model

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"kernel={self.config.kernel}, "
            f"nu={self.config.nu}, "
            f"gamma={self.config.gamma})"
        )