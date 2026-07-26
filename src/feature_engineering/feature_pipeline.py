"""
End-to-end feature engineering pipeline.
"""

from __future__ import annotations

from typing import Optional

import pandas as pd

from src.preprocessing.cleaner import DataCleaner
from src.preprocessing.encoder import DataEncoder
from src.preprocessing.scaler import DataScaler

from src.feature_engineering.correlation_analysis import (
    CorrelationAnalyzer,
)
from src.feature_engineering.feature_selector import (
    FeatureSelector,
)
from src.feature_engineering.dimensionality_reduction import (
    DimensionalityReducer,
)

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class FeaturePipeline:
    """
    Complete preprocessing + feature engineering pipeline.
    """

    def __init__(
        self,
        cleaner: Optional[DataCleaner] = None,
        encoder: Optional[DataEncoder] = None,
        scaler: Optional[DataScaler] = None,
        correlation: Optional[CorrelationAnalyzer] = None,
        selector: Optional[FeatureSelector] = None,
        reducer: Optional[DimensionalityReducer] = None,
    ) -> None:

        self.cleaner = cleaner or DataCleaner()
        self.encoder = encoder or DataEncoder()
        self.scaler = scaler or DataScaler()

        self.correlation = correlation
        self.selector = selector
        self.reducer = reducer

    def fit_transform(
        self,
        dataframe: pd.DataFrame,
        target=None,
    ) -> pd.DataFrame:
        """
        Execute the complete pipeline.
        """

        with Timer("Feature Pipeline"):

            dataframe = self.cleaner.clean(dataframe)

            dataframe = self.encoder.fit_transform(dataframe)

            dataframe = self.scaler.fit_transform(dataframe)

            if self.correlation is not None:
                dataframe = self.correlation.fit_transform(
                    dataframe
                )

            if self.selector is not None:
                dataframe = self.selector.fit_transform(
                    dataframe,
                    target,
                )

            if self.reducer is not None:
                dataframe = self.reducer.fit_transform(
                    dataframe
                )

        logger.info(
            f"Pipeline completed. Final shape: {dataframe.shape}"
        )

        return dataframe