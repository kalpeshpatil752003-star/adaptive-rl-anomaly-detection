"""
Dataset loading utilities for the Adaptive RL Ensemble Framework.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.config.config import config
from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DataLoader:
    """
    Loads one or multiple CSV datasets.
    """

    def __init__(self, data_directory: Path | None = None) -> None:
        self.data_directory = data_directory or config.paths.raw_data_dir

    def load_csv(self, filename: str) -> pd.DataFrame:
        """
        Load a single CSV file.

        Parameters
        ----------
        filename : str
            CSV filename.

        Returns
        -------
        pd.DataFrame
        """

        file_path = self.data_directory / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Dataset not found: {file_path}")

        with Timer(f"Loading {filename}"):

            logger.info(f"Reading {file_path}")

            dataframe = pd.read_csv(file_path)

            logger.info(
                f"Loaded {filename} | Shape={dataframe.shape}"
            )

        return dataframe

    def load_multiple(self, filenames: list[str]) -> pd.DataFrame:
        """
        Load multiple CSV files and concatenate them.

        Parameters
        ----------
        filenames : list[str]

        Returns
        -------
        pd.DataFrame
        """

        dataframes = [self.load_csv(file) for file in filenames]

        combined = pd.concat(
            dataframes,
            ignore_index=True,
        )

        logger.info(
            f"Combined dataset shape={combined.shape}"
        )

        return combined

    @staticmethod
    def dataset_summary(dataframe: pd.DataFrame) -> None:
        """
        Print dataset summary.
        """

        logger.info(f"Rows: {len(dataframe)}")
        logger.info(f"Columns: {len(dataframe.columns)}")
        logger.info(f"Memory Usage: {dataframe.memory_usage(deep=True).sum()/1024**2:.2f} MB")