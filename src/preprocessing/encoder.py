"""
Feature and target encoding utilities.
"""

from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import LabelEncoder

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DataEncoder:
    """
    Encodes categorical features and (optionally) the target column.
    """

    def __init__(self, target_column: str | None = None) -> None:
        self.target_column = target_column

        self.target_encoder = LabelEncoder()
        self.feature_encoders: dict[str, LabelEncoder] = {}

    def fit(self, dataframe: pd.DataFrame) -> None:
        """
        Fit encoders on the dataframe.
        """

        categorical_columns = dataframe.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        if self.target_column in categorical_columns:
            categorical_columns.remove(self.target_column)

        for column in categorical_columns:
            encoder = LabelEncoder()
            encoder.fit(dataframe[column].astype(str))
            self.feature_encoders[column] = encoder

        if (
            self.target_column is not None
            and self.target_column in dataframe.columns
        ):
            self.target_encoder.fit(
                dataframe[self.target_column].astype(str)
            )

    def transform(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Transform dataframe using fitted encoders.
        """

        dataframe = dataframe.copy()

        with Timer("Encoding Dataset"):

            for column, encoder in self.feature_encoders.items():
                dataframe[column] = encoder.transform(
                    dataframe[column].astype(str)
                )

            if (
                self.target_column is not None
                and self.target_column in dataframe.columns
            ):
                dataframe[self.target_column] = (
                    self.target_encoder.transform(
                        dataframe[self.target_column].astype(str)
                    )
                )

        logger.info("Encoding completed.")

        return dataframe

    def fit_transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Fit and transform dataframe.
        """

        self.fit(dataframe)

        return self.transform(dataframe)

    def inverse_target(self, values):
        """
        Decode encoded target labels.
        """

        if self.target_column is None:
            raise ValueError("Target encoder was not initialized.")

        return self.target_encoder.inverse_transform(values)