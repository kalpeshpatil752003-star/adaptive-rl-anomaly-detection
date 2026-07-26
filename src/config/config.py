"""
Central configuration module for the Adaptive Reinforcement Learning
Ensemble-based Network Anomaly Detection framework.

This module defines all framework-wide configuration values in a
centralized, strongly typed, and immutable manner.

Author:
    Kalpesh Patil

Python:
    3.12
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import torch


# =============================================================================
# PATH CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class PathConfig:
    """
    Defines all filesystem paths used throughout the framework.
    """

    project_root: Path = Path(__file__).resolve().parents[2]

    dataset_dir: Path = field(init=False)
    raw_data_dir: Path = field(init=False)
    processed_data_dir: Path = field(init=False)
    external_data_dir: Path = field(init=False)

    checkpoint_dir: Path = field(init=False)
    log_dir: Path = field(init=False)
    output_dir: Path = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "dataset_dir", self.project_root / "datasets")
        object.__setattr__(self, "raw_data_dir", self.dataset_dir / "raw")
        object.__setattr__(self, "processed_data_dir", self.dataset_dir / "processed")
        object.__setattr__(self, "external_data_dir", self.dataset_dir / "external")

        object.__setattr__(self, "checkpoint_dir", self.project_root / "checkpoints")
        object.__setattr__(self, "log_dir", self.project_root / "logs")
        object.__setattr__(self, "output_dir", self.project_root / "outputs")


# =============================================================================
# DATASET CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class DatasetConfig:
    """
    Dataset-related configuration.
    """

    dataset_name: str = "CICIDS2017"

    file_extension: str = ".csv"

    target_column: str = "Label"

    shuffle: bool = True


# =============================================================================
# TRAINING CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class TrainingConfig:
    """
    Hyperparameters used across the framework.
    """

    random_seed: int = 42

    test_size: float = 0.20

    validation_size: float = 0.10

    batch_size: int = 128

    num_workers: int = 4

    learning_rate: float = 1e-3

    epochs: int = 100

    device: str = (
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )


# =============================================================================
# LOGGING CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class LoggingConfig:
    """
    Logging-related settings.
    """

    logger_name: str = "AdaptiveRL"

    log_level: str = "INFO"

    log_filename: str = "framework.log"

    console_logging: bool = True

    file_logging: bool = True


# =============================================================================
# EVALUATION CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class EvaluationConfig:
    """
    Metrics used throughout experiments.
    """

    metrics: tuple[str, ...] = (
        "accuracy",
        "precision",
        "recall",
        "f1",
        "roc_auc",
        "confusion_matrix",
    )


# =============================================================================
# ROOT CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class FrameworkConfig:
    """
    Root configuration object.

    Every module should import this object instead of creating its own
    configuration values.
    """

    paths: PathConfig = field(default_factory=PathConfig)

    dataset: DatasetConfig = field(default_factory=DatasetConfig)

    training: TrainingConfig = field(default_factory=TrainingConfig)

    logging: LoggingConfig = field(default_factory=LoggingConfig)

    evaluation: EvaluationConfig = field(default_factory=EvaluationConfig)


config = FrameworkConfig()