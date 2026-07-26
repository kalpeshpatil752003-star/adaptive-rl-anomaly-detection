"""
Feature scaling utilities.
"""

from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DataScaler:
    """
    Scale numerical features using different scaling strategies.

    Supported scalers
    -----------------
    - standard : StandardScaler
    - minmax   : MinMaxScaler
    - robust   : RobustScaler

    Notes
    -----
    The target column is automatically excluded from scaling.
    """

    SUPPORTED_SCALERS = {
        "standard": StandardScaler,
        "minmax": MinMaxScaler,
        "robust": RobustScaler,
    }

    def __init__(
        self,
        method: str = "standard",
        target_column: str | None = None,
    ) -> None:
        """
        Parameters
        ----------
        method : str
            Scaling method.

        target_column : str | None
            Target column to exclude from scaling.
        """

        method = method.lower()

        if method not in self.SUPPORTED_SCALERS:
            raise ValueError(
                f"Unsupported scaler '{method}'. "
                f"Choose from {list(self.SUPPORTED_SCALERS.keys())}"
            )

        self.method = method
        self.target_column = target_column
        self.scaler = self.SUPPORTED_SCALERS[method]()

        self.numeric_columns: list[str] = []

    def fit(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """
        Fit the scaler on numerical feature columns.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataframe.
        """

        numeric_columns = dataframe.select_dtypes(
            include="number"
        ).columns.tolist()

        if (
            self.target_column is not None
            and self.target_column in numeric_columns
        ):
            numeric_columns.remove(self.target_column)

        self.numeric_columns = numeric_columns

        self.scaler.fit(
            dataframe[self.numeric_columns]
        )

        logger.info(
            f"Scaler ({self.method}) fitted on "
            f"{len(self.numeric_columns)} feature columns."
        )

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Scale numerical feature columns.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataframe.

        Returns
        -------
        pd.DataFrame
            Scaled dataframe.
        """

        if not self.numeric_columns:
            raise RuntimeError(
                "Scaler has not been fitted."
            )

        dataframe = dataframe.copy()

        with Timer("Scaling Dataset"):

            dataframe[self.numeric_columns] = (
                self.scaler.transform(
                    dataframe[self.numeric_columns]
                )
            )

        logger.info("Scaling completed.")

        return dataframe

    def fit_transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Fit and transform dataframe.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataframe.

        Returns
        -------
        pd.DataFrame
            Scaled dataframe.
        """

        self.fit(dataframe)

        return self.transform(dataframe)

    def inverse_transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Reverse scaling on feature columns.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Scaled dataframe.

        Returns
        -------
        pd.DataFrame
            Original-scale dataframe.
        """

        if not self.numeric_columns:
            raise RuntimeError(
                "Scaler has not been fitted."
            )

        dataframe = dataframe.copy()

        dataframe[self.numeric_columns] = (
            self.scaler.inverse_transform(
                dataframe[self.numeric_columns]
            )
        )

        return dataframe

    def __repr__(self) -> str:
        """
        String representation.
        """

        return (
            f"{self.__class__.__name__}("
            f"method='{self.method}', "
            f"target_column={self.target_column}, "
            f"features={len(self.numeric_columns)})"
        )