"""
Feature selection utilities.
"""

from __future__ import annotations

from typing import Optional

import pandas as pd

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import mutual_info_classif

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class FeatureSelector:
    """
    Generic feature selection interface.
    """

    SUPPORTED_METHODS = (
        "variance",
        "mutual_info",
        "anova",
        "random_forest",
        "extra_trees",
    )

    def __init__(
        self,
        method: str = "variance",
        k: int = 20,
        threshold: float = 0.0,
        random_state: int = 42,
    ) -> None:

        if method not in self.SUPPORTED_METHODS:
            raise ValueError(
                f"Unsupported method '{method}'. "
                f"Choose from {self.SUPPORTED_METHODS}"
            )

        self.method = method
        self.k = k
        self.threshold = threshold
        self.random_state = random_state

        self.selected_features: list[str] = []

    def fit(
        self,
        X: pd.DataFrame,
        y: Optional[pd.Series] = None,
    ) -> None:

        with Timer(f"Feature Selection ({self.method})"):

            if self.method == "variance":

                selector = VarianceThreshold(
                    threshold=self.threshold
                )

                selector.fit(X)

                self.selected_features = (
                    X.columns[
                        selector.get_support()
                    ].tolist()
                )

            elif self.method == "mutual_info":

                if y is None:
                    raise ValueError(
                        "Target values are required."
                    )

                selector = SelectKBest(
                    score_func=mutual_info_classif,
                    k=min(self.k, X.shape[1]),
                )

                selector.fit(X, y)

                self.selected_features = (
                    X.columns[
                        selector.get_support()
                    ].tolist()
                )

            elif self.method == "anova":

                if y is None:
                    raise ValueError(
                        "Target values are required."
                    )

                selector = SelectKBest(
                    score_func=f_classif,
                    k=min(self.k, X.shape[1]),
                )

                selector.fit(X, y)

                self.selected_features = (
                    X.columns[
                        selector.get_support()
                    ].tolist()
                )

            elif self.method == "random_forest":

                if y is None:
                    raise ValueError(
                        "Target values are required."
                    )

                model = RandomForestClassifier(
                    n_estimators=200,
                    random_state=self.random_state,
                    n_jobs=-1,
                )

                model.fit(X, y)

                importance = pd.Series(
                    model.feature_importances_,
                    index=X.columns,
                )

                self.selected_features = (
                    importance
                    .sort_values(ascending=False)
                    .head(min(self.k, X.shape[1]))
                    .index
                    .tolist()
                )

            elif self.method == "extra_trees":

                if y is None:
                    raise ValueError(
                        "Target values are required."
                    )

                model = ExtraTreesClassifier(
                    n_estimators=200,
                    random_state=self.random_state,
                    n_jobs=-1,
                )

                model.fit(X, y)

                importance = pd.Series(
                    model.feature_importances_,
                    index=X.columns,
                )

                self.selected_features = (
                    importance
                    .sort_values(ascending=False)
                    .head(min(self.k, X.shape[1]))
                    .index
                    .tolist()
                )

        logger.info(
            f"Selected {len(self.selected_features)} features."
        )

    def transform(
        self,
        X: pd.DataFrame,
    ) -> pd.DataFrame:

        return X[self.selected_features].copy()

    def fit_transform(
        self,
        X: pd.DataFrame,
        y: Optional[pd.Series] = None,
    ) -> pd.DataFrame:

        self.fit(X, y)

        return self.transform(X)