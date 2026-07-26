"""
Statistical feature analysis utilities.
"""

from __future__ import annotations

import pandas as pd

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class StatisticalFeatureAnalyzer:
    """
    Computes descriptive statistics for numerical features.
    """

    def __init__(self) -> None:
        self.summary: pd.DataFrame | None = None

    def analyze(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Generate descriptive statistics.
        """

        with Timer("Statistical Analysis"):

            numeric_df = dataframe.select_dtypes(include="number")

            self.summary = pd.DataFrame({
                "mean": numeric_df.mean(),
                "std": numeric_df.std(),
                "variance": numeric_df.var(),
                "min": numeric_df.min(),
                "max": numeric_df.max(),
                "median": numeric_df.median(),
                "skewness": numeric_df.skew(),
                "kurtosis": numeric_df.kurt(),
                "missing": numeric_df.isna().sum(),
            })

        logger.info(
            f"Computed statistics for {len(self.summary)} features."
        )

        return self.summary

    def top_variance(
        self,
        n: int = 10,
    ) -> pd.DataFrame:

        if self.summary is None:
            raise ValueError(
                "Run analyze() first."
            )

        return self.summary.sort_values(
            by="variance",
            ascending=False,
        ).head(n)