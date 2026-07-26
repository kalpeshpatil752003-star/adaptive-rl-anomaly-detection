"""
Dimensionality reduction utilities.
"""

from __future__ import annotations

import pandas as pd

from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DimensionalityReducer:
    """
    Generic dimensionality reduction interface.
    """

    SUPPORTED_METHODS = (
        "pca",
        "incremental_pca",
    )

    def __init__(
        self,
        method: str = "pca",
        n_components: float | int = 0.95,
        batch_size: int = 512,
    ) -> None:

        if method not in self.SUPPORTED_METHODS:
            raise ValueError(
                f"Unsupported method '{method}'."
            )

        self.method = method

        if method == "pca":

            self.reducer = PCA(
                n_components=n_components
            )

        else:

            self.reducer = IncrementalPCA(
                n_components=n_components,
                batch_size=batch_size,
            )

    def fit(
        self,
        dataframe: pd.DataFrame,
    ) -> None:

        with Timer(f"Training {self.method}"):

            self.reducer.fit(dataframe)

        logger.info("Reducer fitted.")

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        transformed = self.reducer.transform(dataframe)

        columns = [
            f"PC{i+1}"
            for i in range(transformed.shape[1])
        ]

        return pd.DataFrame(
            transformed,
            columns=columns,
            index=dataframe.index,
        )

    def fit_transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        self.fit(dataframe)

        return self.transform(dataframe)

    @property
    def explained_variance(self):

        return self.reducer.explained_variance_ratio_