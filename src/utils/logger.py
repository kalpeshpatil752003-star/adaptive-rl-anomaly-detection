"""
Centralized logging utility for the Adaptive RL Ensemble Framework.
"""

from __future__ import annotations

import logging
from pathlib import Path

from src.config.config import config


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Create and configure a logger.

    Parameters
    ----------
    name : str | None
        Name of the logger.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    logger_name = name or config.logging.logger_name
    logger = logging.getLogger(logger_name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(getattr(logging, config.logging.log_level.upper()))

    # Create log directory if it doesn't exist
    Path(config.paths.log_dir).mkdir(parents=True, exist_ok=True)

    log_file = Path(config.paths.log_dir) / config.logging.log_filename

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger