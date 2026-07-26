"""
Base classes for all anomaly detection models.

This module defines the abstract interface that every anomaly detection
model in the framework must implement.

Author: Kalpesh Patil
Project:
Adaptive Multi-Paradigm Network Anomaly Detection:
Fusion of Unsupervised Models via Reinforcement Learning
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Optional
import logging

import joblib
import numpy as np
import pandas as pd


@dataclass(slots=True)
class ModelMetadata:
    """
    Stores metadata describing a trained model.
    """

    model_name: str
    model_version: str = "1.0.0"
    training_timestamp: Optional[str] = None
    training_time_seconds: Optional[float] = None
    n_features: Optional[int] = None
    random_state: Optional[int] = None
    additional_info: dict[str, Any] = field(default_factory=dict)


class BaseAnomalyModel(ABC):
    """
    Abstract base class for all anomaly detection models.

    Every anomaly detection model must inherit from this class and
    implement the required abstract methods.

    Standard prediction convention:

        predict():
            0 -> Normal
            1 -> Anomaly

        anomaly_score():
            Higher score = More anomalous
    """

    def __init__(
        self,
        model_name: str,
        random_state: Optional[int] = None,
    ) -> None:
        self.model_name = model_name
        self.random_state = random_state

        self._is_fitted: bool = False
        self._model: Any = None

        self.metadata = ModelMetadata(
            model_name=model_name,
            random_state=random_state,
        )
        self.logger = logging.getLogger(self.model_name)

    # ------------------------------------------------------------------
    # Abstract API
    # ------------------------------------------------------------------

    @abstractmethod
    def fit(self, X: pd.DataFrame | np.ndarray) -> "BaseAnomalyModel":
        """
        Train the anomaly detection model.

        Parameters
        ----------
        X : pd.DataFrame | np.ndarray
            Training feature matrix.

        Returns
        -------
        BaseAnomalyModel
            The trained model.
        """

    @abstractmethod
    def predict(self, X: pd.DataFrame | np.ndarray) -> np.ndarray:
        """
        Predict anomalies.

        Returns
        -------
        np.ndarray

            Binary predictions.

            0 = Normal
            1 = Anomaly
        """

    @abstractmethod
    def anomaly_score(self, X: pd.DataFrame | np.ndarray) -> np.ndarray:
        """
        Compute anomaly scores.

        Higher score always indicates a more anomalous sample.
        """

    # ------------------------------------------------------------------
    # Public utility methods
    # ------------------------------------------------------------------

    @property
    def is_fitted(self) -> bool:
        """
        Indicates whether the model has been trained.
        """
        return self._is_fitted

    def save(self, filepath: str | Path) -> None:
        """
        Save the model to disk.

        Parameters
        ----------
        filepath : str | Path
            Destination path.
        """
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        joblib.dump(self, filepath)

    @classmethod
    def load(cls, filepath: str | Path) -> Any:
        """
        Load a previously saved model.

        Parameters
        ----------
        filepath : str | Path
            Saved model path.

        Returns
        -------
        BaseAnomalyModel
        """
        return joblib.load(filepath)

    # ------------------------------------------------------------------
    # Protected helper methods
    # ------------------------------------------------------------------

    def _validate_input(
        self,
        X: pd.DataFrame | np.ndarray,
    ) -> np.ndarray:
        """
        Validate the input feature matrix.

        Parameters
        ----------
        X : pd.DataFrame | np.ndarray
            Feature matrix.

        Returns
        -------
        np.ndarray
            Validated NumPy array.
        """

        # Accept pandas DataFrame
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()

        # Accept NumPy arrays
        elif not isinstance(X, np.ndarray):
            raise TypeError(
                "Input must be a pandas DataFrame or NumPy ndarray."
            )

        if X.ndim != 2:
            raise ValueError(
                "Input array must be two-dimensional."
            )

        if X.shape[0] == 0:
            raise ValueError(
                "Input array cannot be empty."
            )

        if X.shape[1] == 0:
            raise ValueError(
                "Input array must contain at least one feature."
            )

        return X

    def _check_is_fitted(self) -> None:
        """
        Ensure the model has already been trained.
        """

        if not self._is_fitted:
            raise RuntimeError(
                f"{self.model_name} has not been fitted yet."
            )

    def _set_fitted(
        self,
        n_features: int,
        training_time: Optional[float] = None,
    ) -> None:
        """
        Mark model as trained and update metadata.
        """

        self._is_fitted = True

        self.metadata.training_timestamp = (
            datetime.now().isoformat(timespec="seconds")
        )

        self.metadata.n_features = n_features
        self.metadata.training_time_seconds = training_time

    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"model_name='{self.model_name}', "
            f"is_fitted={self._is_fitted})"
        )