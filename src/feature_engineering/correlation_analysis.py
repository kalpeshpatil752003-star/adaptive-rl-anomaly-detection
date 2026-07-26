"""
Correlation analysis utilities.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class CorrelationAnalyzer:
    """
    Remove highly correlated numerical features.
    """

    def __init__(self, threshold: float = 0.95) -> None:
        self.threshold = threshold
        self.removed_features: list[str] = []

    def fit(self, dataframe: pd.DataFrame) -> None:
        """
        Identify highly correlated columns.
        """

        numeric_df = dataframe.select_dtypes(include="number")

        correlation_matrix = numeric_df.corr().abs()

        upper_triangle = correlation_matrix.where(
            np.triu(
                np.ones(correlation_matrix.shape),
                k=1,
            ).astype(bool)
        )

        self.removed_features = [
            column
            for column in upper_triangle.columns
            if any(upper_triangle[column] > self.threshold)
        ]

        logger.info(
            f"Identified {len(self.removed_features)} correlated features."
        )

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove correlated columns.
        """

        dataframe = dataframe.copy()

        with Timer("Correlation Analysis"):

            dataframe = dataframe.drop(
                columns=self.removed_features,
                errors="ignore",
            )

        logger.info(
            f"Remaining features: {dataframe.shape[1]}"
        )

        return dataframe

    def fit_transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        self.fit(dataframe)

        return self.transform(dataframe)