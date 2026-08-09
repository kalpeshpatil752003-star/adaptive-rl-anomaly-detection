"""
src/config/autoencoder_config.py

Configuration for the PyTorch-based AutoEncoder anomaly detection model.

Follows the same configuration pattern as IsolationForestConfig,
LocalOutlierFactorConfig, and OneClassSVMConfig: a configuration
dataclass holding all hyperparameters and runtime settings, with
validation performed in __post_init__.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Literal, Optional

logger = logging.getLogger(__name__)

ReconstructionLoss = Literal["mse", "mae"]
ThresholdStrategy = Literal["percentile", "mean_std"]


@dataclass
class AutoEncoderConfig:
    """
    Configuration for the AutoEncoder anomaly detection model.

    The AutoEncoder learns a compressed representation of normal
    network traffic. Anomaly scores are derived from reconstruction
    error, where a higher error indicates a more anomalous sample.

    Attributes:
        input_dim: Number of input features. Must match the
            preprocessed feature matrix (currently 70 for CICIDS2017).
        hidden_dims: Sizes of the encoder's hidden layers, in order
            from input side to bottleneck. The decoder mirrors this
            in reverse. E.g. [64, 32] with latent_dim=16 gives an
            encoder of 70 -> 64 -> 32 -> 16.
        latent_dim: Size of the bottleneck (latent) representation.
        activation: Activation function used between hidden layers.
            One of "relu", "leaky_relu", "tanh".
        dropout: Dropout probability applied after each hidden layer.
            Set to 0.0 to disable dropout.
        batch_size: Mini-batch size used during training and
            inference.
        epochs: Maximum number of training epochs.
        learning_rate: Learning rate for the Adam optimizer.
        weight_decay: L2 regularization coefficient for the Adam
            optimizer.
        reconstruction_loss: Loss function used to measure
            reconstruction error. One of "mse" (mean squared error)
            or "mae" (mean absolute error).
        validation_split: Fraction of the training data held out for
            validation and early stopping. Must be in [0.0, 1.0).
        early_stopping_patience: Number of epochs with no validation
            loss improvement before training stops early. Set to
            None to disable early stopping.
        early_stopping_min_delta: Minimum decrease in validation loss
            to qualify as an improvement for early stopping purposes.
        threshold_strategy: Strategy used to convert continuous
            reconstruction error into a binary prediction. One of
            "percentile" (flag samples whose error exceeds a given
            percentile as anomalous) or "mean_std" (flag samples whose
            error exceeds mean + threshold_std_multiplier * std).
            In both cases the statistic (percentile, mean, std) is
            computed on reconstruction errors from a held-out set of
            known-normal validation samples, NOT from the full
            training set and NOT from data containing anomalies.
            This keeps the threshold methodology defensible: it
            characterizes "how much reconstruction error is normal"
            rather than mislabeling a fixed fraction of normal
            traffic as anomalous by construction.
        threshold_percentile: Percentile (0-100) of normal validation
            reconstruction error used as the anomaly threshold when
            threshold_strategy="percentile". E.g. 95.0 sets the
            threshold at the 95th percentile of reconstruction error
            observed on known-normal validation samples; test samples
            with error above this threshold are flagged as anomalous.
        threshold_std_multiplier: Multiplier applied to the standard
            deviation of normal validation reconstruction error when
            threshold_strategy="mean_std" (threshold = mean + k * std,
            computed on known-normal validation samples).
        device: Compute device to use. One of "cuda", "cpu", or
            "auto" (use CUDA if available, otherwise CPU).
        random_seed: Seed used for reproducible weight initialization,
            batching, and any stochastic training behavior.
        num_workers: Number of subprocess workers used by the PyTorch
            DataLoader.
        checkpoint_dir: Directory where intermediate model checkpoints
            are written. None disables checkpointing.
        checkpoint_every_n_epochs: Frequency, in epochs, at which a
            checkpoint is saved when checkpoint_dir is set.
        gradient_clip_norm: Maximum gradient norm used for gradient
            clipping. None disables gradient clipping.
        log_every_n_epochs: Frequency, in epochs, at which training
            progress is logged.
    """

    input_dim: int
    hidden_dims: list[int] = field(default_factory=lambda: [64, 32])
    latent_dim: int = 16
    activation: Literal["relu", "leaky_relu", "tanh"] = "relu"
    dropout: float = 0.0

    batch_size: int = 512
    epochs: int = 50
    learning_rate: float = 1e-3
    weight_decay: float = 0.0
    reconstruction_loss: ReconstructionLoss = "mse"

    validation_split: float = 0.1
    early_stopping_patience: Optional[int] = 5
    early_stopping_min_delta: float = 1e-4

    threshold_strategy: ThresholdStrategy = "percentile"
    threshold_percentile: float = 95.0
    threshold_std_multiplier: float = 3.0

    device: Literal["cuda", "cpu", "auto"] = "auto"
    random_seed: int = 42
    num_workers: int = 0

    checkpoint_dir: Optional[str] = None
    checkpoint_every_n_epochs: int = 5
    gradient_clip_norm: Optional[float] = None
    log_every_n_epochs: int = 1

    def __post_init__(self) -> None:
        """
        Validate configuration values for internal consistency.

        Raises:
            ValueError: If any configuration value is out of its
                valid range or otherwise inconsistent.
        """
        if self.input_dim <= 0:
            raise ValueError(f"input_dim must be positive, got {self.input_dim}.")

        if not self.hidden_dims:
            raise ValueError("hidden_dims must contain at least one layer size.")
        if any(dim <= 0 for dim in self.hidden_dims):
            raise ValueError(
                f"All hidden_dims must be positive, got {self.hidden_dims}."
            )

        if self.latent_dim <= 0:
            raise ValueError(
                f"latent_dim must be positive, got {self.latent_dim}."
            )

        if not 0.0 <= self.dropout < 1.0:
            raise ValueError(f"dropout must be in [0.0, 1.0), got {self.dropout}.")

        if self.batch_size <= 0:
            raise ValueError(
                f"batch_size must be positive, got {self.batch_size}."
            )
        if self.epochs <= 0:
            raise ValueError(f"epochs must be positive, got {self.epochs}.")
        if self.learning_rate <= 0.0:
            raise ValueError(
                f"learning_rate must be positive, got {self.learning_rate}."
            )
        if self.weight_decay < 0.0:
            raise ValueError(
                f"weight_decay must be non-negative, got {self.weight_decay}."
            )

        if not 0.0 <= self.validation_split < 1.0:
            raise ValueError(
                "validation_split must be in [0.0, 1.0), got "
                f"{self.validation_split}."
            )

        if (
            self.early_stopping_patience is not None
            and self.early_stopping_patience <= 0
        ):
            raise ValueError(
                "early_stopping_patience must be positive or None, got "
                f"{self.early_stopping_patience}."
            )
        if self.early_stopping_min_delta < 0.0:
            raise ValueError(
                "early_stopping_min_delta must be non-negative, got "
                f"{self.early_stopping_min_delta}."
            )

        if not 0.0 <= self.threshold_percentile <= 100.0:
            raise ValueError(
                "threshold_percentile must be in [0.0, 100.0], got "
                f"{self.threshold_percentile}."
            )
        if self.threshold_std_multiplier <= 0.0:
            raise ValueError(
                "threshold_std_multiplier must be positive, got "
                f"{self.threshold_std_multiplier}."
            )

        if self.device not in ("cuda", "cpu", "auto"):
            raise ValueError(
                f"device must be one of 'cuda', 'cpu', 'auto', got {self.device}."
            )

        if self.num_workers < 0:
            raise ValueError(
                f"num_workers must be non-negative, got {self.num_workers}."
            )
        if self.checkpoint_every_n_epochs <= 0:
            raise ValueError(
                "checkpoint_every_n_epochs must be positive, got "
                f"{self.checkpoint_every_n_epochs}."
            )
        if (
            self.gradient_clip_norm is not None
            and self.gradient_clip_norm <= 0.0
        ):
            raise ValueError(
                "gradient_clip_norm must be positive or None, got "
                f"{self.gradient_clip_norm}."
            )
        if self.log_every_n_epochs <= 0:
            raise ValueError(
                "log_every_n_epochs must be positive, got "
                f"{self.log_every_n_epochs}."
            )

        logger.debug(
            "AutoEncoderConfig validated: input_dim=%d, hidden_dims=%s, "
            "latent_dim=%d, batch_size=%d, epochs=%d, device=%s",
            self.input_dim,
            self.hidden_dims,
            self.latent_dim,
            self.batch_size,
            self.epochs,
            self.device,
        )

    @property
    def encoder_layer_sizes(self) -> list[int]:
        """
        Full sequence of encoder layer sizes from input to bottleneck.

        Returns:
            [input_dim, *hidden_dims, latent_dim]
        """
        return [self.input_dim, *self.hidden_dims, self.latent_dim]

    @property
    def decoder_layer_sizes(self) -> list[int]:
        """
        Full sequence of decoder layer sizes from bottleneck to output.

        Returns:
            [latent_dim, *reversed(hidden_dims), input_dim]
        """
        return [self.latent_dim, *reversed(self.hidden_dims), self.input_dim]