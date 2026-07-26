"""
Dataset splitting utilities.
"""

from __future__ import annotations

from typing import Optional

import pandas as pd
from sklearn.model_selection import train_test_split

from src.config.config import config
from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DataSplitter:
    """
    Split datasets into train, validation, and test sets.
    """

    def __init__(
        self,
        train_size: float = 0.70,
        validation_size: float = 0.15,
        test_size: float = 0.15,
        random_state: Optional[int] = None,
    ) -> None:

        total = train_size + validation_size + test_size

        if abs(total - 1.0) > 1e-6:
            raise ValueError(
                "train_size + validation_size + test_size must equal 1.0"
            )

        self.train_size = train_size
        self.validation_size = validation_size
        self.test_size = test_size
        self.random_state = (
            random_state
            if random_state is not None
            else config.training.random_seed
        )

    def split(
        self,
        dataframe: pd.DataFrame,
        target_column: str | None = None,
        stratify: bool = False,
    ):
        """
        Split a dataframe into train, validation, and test sets.
        """

        with Timer("Dataset Splitting"):

            stratify_values = None

            if (
                stratify
                and target_column is not None
                and target_column in dataframe.columns
            ):
                stratify_values = dataframe[target_column]

            train_df, temp_df = train_test_split(
                dataframe,
                train_size=self.train_size,
                random_state=self.random_state,
                shuffle=True,
                stratify=stratify_values,
            )

            validation_ratio = (
                self.validation_size
                / (self.validation_size + self.test_size)
            )

            temp_stratify = None

            if stratify_values is not None:
                temp_stratify = temp_df[target_column]

            validation_df, test_df = train_test_split(
                temp_df,
                train_size=validation_ratio,
                random_state=self.random_state,
                shuffle=True,
                stratify=temp_stratify,
            )

        logger.info(
            f"Train={len(train_df)} | "
            f"Validation={len(validation_df)} | "
            f"Test={len(test_df)}"
        )

        return (
            train_df.reset_index(drop=True),
            validation_df.reset_index(drop=True),
            test_df.reset_index(drop=True),
        )