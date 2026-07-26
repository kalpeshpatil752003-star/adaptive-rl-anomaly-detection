"""
Data cleaning utilities for the Adaptive RL Ensemble Framework.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.config.config import config
from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DataCleaner:
    """
    Performs basic data cleaning operations.
    """

    def __init__(self, target_column: str | None = None) -> None:
        self.target_column = target_column or config.dataset.target_column

    def remove_duplicates(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Remove duplicate rows.
        """

        with Timer("Removing Duplicates"):

            before = len(dataframe)

            dataframe = dataframe.drop_duplicates()

            removed = before - len(dataframe)

            logger.info(f"Removed {removed} duplicate rows.")

        return dataframe

    def replace_infinities(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Replace positive and negative infinity with NaN.
        """

        with Timer("Replacing Infinite Values"):

            dataframe = dataframe.replace(
                [np.inf, -np.inf],
                np.nan,
            )

        return dataframe

    def remove_missing(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Remove rows containing missing values.
        """

        with Timer("Removing Missing Values"):

            before = len(dataframe)

            dataframe = dataframe.dropna()

            removed = before - len(dataframe)

            logger.info(f"Removed {removed} rows containing missing values.")

        return dataframe

    def remove_constant_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove columns containing only one unique value.
        """

        with Timer("Removing Constant Columns"):

            constant_columns = [
                column
                for column in dataframe.columns
                if dataframe[column].nunique() <= 1
            ]

            dataframe = dataframe.drop(
                columns=constant_columns
            )

            logger.info(
                f"Removed {len(constant_columns)} constant columns."
            )

        return dataframe

    def clean(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Complete cleaning pipeline.
        """

        dataframe = self.replace_infinities(dataframe)

        dataframe = self.remove_duplicates(dataframe)

        dataframe = self.remove_missing(dataframe)

        dataframe = self.remove_constant_columns(dataframe)

        logger.info(
            f"Cleaning completed. Final shape: {dataframe.shape}"
        )

        return dataframe