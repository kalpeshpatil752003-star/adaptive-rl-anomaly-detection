"""
src/models/autoencoder.py

PyTorch AutoEncoder anomaly detection model.

Integrates with the framework's BaseAnomalyModel interface
(src.models.base_model.BaseAnomalyModel), the shared logger, and the
shared model persistence convention (joblib), exactly like
IsolationForestModel, LocalOutlierFactorModel, and OneClassSVMModel.

Training methodology
---------------------
fit(X) expects X to be KNOWN-NORMAL traffic only. Selecting normal-only
rows (e.g. y_train == 0) is the caller's/notebook's responsibility;
this model does not have access to labels and must not be handed a
mixed normal+attack matrix. Internally, the normal-only X is split into
a training subset and a held-out normal validation subset
(config.validation_split). The validation subset is used for early
stopping and, after training, to calibrate the anomaly threshold from
its reconstruction-error distribution. This avoids calibrating the
threshold on data that could already contain anomalies.

Prediction convention
----------------------
0 -> Normal
1 -> Anomaly

Anomaly score convention
--------------------------
Higher reconstruction error -> more anomalous
"""

from __future__ import annotations

import time
from copy import deepcopy
from pathlib import Path
from typing import Optional

import joblib
import numpy as np
import torch
from torch import Tensor, nn, optim
from torch.utils.data import DataLoader, TensorDataset

from src.config.autoencoder_config import AutoEncoderConfig
from src.models.base_model import BaseAnomalyModel
from src.utils.logger import get_logger

logger = get_logger(__name__)

_ACTIVATIONS = {
    "relu": nn.ReLU,
    "leaky_relu": nn.LeakyReLU,
    "tanh": nn.Tanh,
}


class _AutoEncoderNetwork(nn.Module):
    """
    Fully connected encoder/decoder network derived entirely from
    AutoEncoderConfig, so architecture is never hardcoded in training
    logic.
    """

    def __init__(self, config: AutoEncoderConfig) -> None:
        """
        Build the encoder and decoder from the given configuration.

        Args:
            config: Validated AutoEncoderConfig instance.
        """
        super().__init__()
        self.config = config

        self.encoder = self._build_stack(
            layer_sizes=config.encoder_layer_sizes,
            activation=config.activation,
            dropout=config.dropout,
            activate_final_layer=False,
        )
        self.decoder = self._build_stack(
            layer_sizes=config.decoder_layer_sizes,
            activation=config.activation,
            dropout=config.dropout,
            activate_final_layer=False,
        )

    @staticmethod
    def _create_activation(activation: str) -> nn.Module:
        """
        Instantiate the configured activation module.

        Args:
            activation: One of "relu", "leaky_relu", "tanh".

        Returns:
            A new activation module instance.

        Raises:
            ValueError: If activation is not recognized.
        """
        if activation not in _ACTIVATIONS:
            raise ValueError(f"Unsupported activation function: {activation}")
        return _ACTIVATIONS[activation]()

    def _build_stack(
        self,
        layer_sizes: list,
        activation: str,
        dropout: float,
        activate_final_layer: bool,
    ) -> nn.Sequential:
        """
        Build a Linear -> Activation -> Dropout stack.

        The final Linear layer is left without activation/dropout
        (activate_final_layer=False) so that both the latent
        bottleneck and the reconstructed output remain unconstrained
        linear projections, consistent with pre-scaled input features.

        Args:
            layer_sizes: Consecutive layer widths.
            activation: Activation function name.
            dropout: Dropout probability (0.0 disables dropout).
            activate_final_layer: Whether to apply activation/dropout
                after the last Linear layer.

        Returns:
            An nn.Sequential module implementing the stack.
        """
        layers: list = []
        n_layers = len(layer_sizes) - 1

        for index in range(n_layers):
            in_size, out_size = layer_sizes[index], layer_sizes[index + 1]
            layers.append(nn.Linear(in_size, out_size))

            is_last = index == n_layers - 1
            if not is_last or activate_final_layer:
                layers.append(self._create_activation(activation))
                if dropout > 0.0:
                    layers.append(nn.Dropout(dropout))

        return nn.Sequential(*layers)

    def encode(self, X: Tensor) -> Tensor:
        """Encode input samples into their latent representation."""
        return self.encoder(X)

    def decode(self, latent: Tensor) -> Tensor:
        """Decode a latent representation back into feature space."""
        return self.decoder(latent)

    def forward(self, X: Tensor) -> Tensor:
        """Reconstruct input samples via encode -> decode."""
        return self.decode(self.encode(X))


class AutoEncoderModel(BaseAnomalyModel):
    """
    AutoEncoder-based anomaly detector conforming to BaseAnomalyModel.

    Args:
        config: Validated AutoEncoderConfig instance controlling
            architecture, training, and thresholding behavior.
    """

    def __init__(self, config: AutoEncoderConfig) -> None:
        super().__init__(
            model_name="AutoEncoder",
            random_state=config.random_seed,
        )

        self.config = config
        self._device = self._resolve_device(config.device)
        self._model = _AutoEncoderNetwork(config).to(self._device)

        self.threshold: Optional[float] = None
        self.training_samples: int = 0
        self.validation_samples: int = 0
        self.training_history: dict = {"train_loss": [], "validation_loss": []}

        logger.info(
            "AutoEncoder initialized | device=%s | input_dim=%d | "
            "hidden_dims=%s | latent_dim=%d",
            self._device,
            config.input_dim,
            config.hidden_dims,
            config.latent_dim,
        )

    # ------------------------------------------------------------------
    # Device
    # ------------------------------------------------------------------

    @staticmethod
    def _resolve_device(device: str) -> torch.device:
        """
        Resolve the configured device setting into a concrete device.

        Args:
            device: One of "cuda", "cpu", "auto".

        Returns:
            The resolved torch.device.

        Raises:
            RuntimeError: If "cuda" is explicitly requested but
                unavailable.
        """
        if device == "auto":
            return torch.device("cuda" if torch.cuda.is_available() else "cpu")

        if device == "cuda" and not torch.cuda.is_available():
            raise RuntimeError(
                "AutoEncoderConfig requested CUDA, but CUDA is not available."
            )

        return torch.device(device)

    @property
    def device(self) -> torch.device:
        """Return the device currently used by the model."""
        return self._device

    @property
    def estimator(self) -> nn.Module:
        """Return the underlying PyTorch AutoEncoder network."""
        return self._model

    # ------------------------------------------------------------------
    # Input preparation
    # ------------------------------------------------------------------

    def _prepare_input(self, X: np.ndarray) -> np.ndarray:
        """
        Validate and convert input data to float32 via the framework's
        shared input validation.

        Args:
            X: Raw feature matrix (array-like or DataFrame).

        Returns:
            A validated, contiguous float32 numpy array.

        Raises:
            ValueError: If the feature count doesn't match
                config.input_dim, or if non-finite values are found.
        """
        X = self._validate_input(X)

        if X.shape[1] != self.config.input_dim:
            raise ValueError(
                "Input feature count does not match AutoEncoder "
                f"configuration: expected {self.config.input_dim}, got "
                f"{X.shape[1]}."
            )

        X = np.asarray(X, dtype=np.float32)

        if not np.isfinite(X).all():
            raise ValueError(
                "Input contains NaN or infinite values. Run the "
                "preprocessing pipeline before using the AutoEncoder."
            )

        return X

    def _create_loader(self, X: np.ndarray, shuffle: bool) -> DataLoader:
        """
        Wrap a feature matrix in a batched DataLoader.

        Args:
            X: Feature matrix to wrap.
            shuffle: Whether to shuffle batches (True for training).

        Returns:
            A configured DataLoader.
        """
        dataset = TensorDataset(torch.from_numpy(X))

        return DataLoader(
            dataset,
            batch_size=self.config.batch_size,
            shuffle=shuffle,
            num_workers=self.config.num_workers,
            pin_memory=(self._device.type == "cuda"),
            persistent_workers=(self.config.num_workers > 0),
            drop_last=False,
        )

    # ------------------------------------------------------------------
    # Loss
    # ------------------------------------------------------------------

    def _loss_function(self, reconstructed: Tensor, original: Tensor) -> Tensor:
        """
        Compute the batch-averaged reconstruction loss.

        Args:
            reconstructed: Reconstructed batch.
            original: Original input batch.

        Returns:
            Scalar loss tensor, per config.reconstruction_loss.
        """
        if self.config.reconstruction_loss == "mse":
            return torch.mean((reconstructed - original) ** 2)
        return torch.mean(torch.abs(reconstructed - original))

    def _sample_reconstruction_errors(
        self, reconstructed: Tensor, original: Tensor
    ) -> Tensor:
        """
        Compute one reconstruction error per sample (not batch-averaged).

        Args:
            reconstructed: Reconstructed batch.
            original: Original input batch.

        Returns:
            1D tensor of shape (batch_size,) with per-sample error.
        """
        if self.config.reconstruction_loss == "mse":
            return torch.mean((reconstructed - original) ** 2, dim=1)
        return torch.mean(torch.abs(reconstructed - original), dim=1)

    def _evaluate_loss(self, loader: DataLoader) -> float:
        """
        Compute the mean reconstruction loss over an entire DataLoader.

        Args:
            loader: DataLoader to evaluate.

        Returns:
            Mean loss, weighted by batch size.

        Raises:
            RuntimeError: If the loader yields no samples.
        """
        self._model.eval()
        total_loss = 0.0
        total_samples = 0

        with torch.no_grad():
            for (batch,) in loader:
                batch = batch.to(self._device, non_blocking=True)
                reconstructed = self._model(batch)
                loss = self._loss_function(reconstructed, batch)

                batch_size = batch.size(0)
                total_loss += loss.item() * batch_size
                total_samples += batch_size

        if total_samples == 0:
            raise RuntimeError("Cannot evaluate AutoEncoder on an empty dataset.")

        return total_loss / total_samples

    # ------------------------------------------------------------------
    # Threshold calibration
    # ------------------------------------------------------------------

    def _calculate_threshold(self, reconstruction_errors: np.ndarray) -> float:
        """
        Calibrate the anomaly threshold from known-normal reconstruction
        errors.

        Args:
            reconstruction_errors: 1D array of reconstruction errors
                computed on known-normal data (validation subset,
                falling back to the training subset only if
                validation_split=0.0).

        Returns:
            The calibrated scalar threshold.

        Raises:
            RuntimeError: If reconstruction_errors is empty.
            ValueError: If config.threshold_strategy is unrecognized.
        """
        if reconstruction_errors.size == 0:
            raise RuntimeError(
                "Cannot calculate anomaly threshold from empty "
                "reconstruction errors."
            )

        if self.config.threshold_strategy == "percentile":
            return float(
                np.percentile(reconstruction_errors, self.config.threshold_percentile)
            )

        if self.config.threshold_strategy == "mean_std":
            mean = float(np.mean(reconstruction_errors))
            std = float(np.std(reconstruction_errors))
            return mean + self.config.threshold_std_multiplier * std

        raise ValueError(
            f"Unsupported threshold strategy: {self.config.threshold_strategy}"
        )

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def fit(self, X: np.ndarray) -> "AutoEncoderModel":
        """
        Train the AutoEncoder on known-normal traffic and calibrate the
        anomaly threshold.

        Args:
            X: Training feature matrix containing ONLY known-normal
                traffic (e.g. X_train[y_train == 0]). The AutoEncoder
                has no access to labels and cannot filter attacks out
                of a mixed matrix itself; supplying mixed data will
                bias both training and threshold calibration.

        Returns:
            self, fitted.

        Raises:
            ValueError: If X's feature dimension doesn't match
                config.input_dim, or contains non-finite values.
        """
        X = self._prepare_input(X)

        if self.config.validation_split > 0.0:
            if len(X) < 2:
                raise ValueError(
                    "At least two samples are required when "
                    "validation_split is greater than zero."
                )

            rng = np.random.default_rng(self.config.random_seed)
            indices = rng.permutation(len(X))

            n_val = max(1, int(len(X) * self.config.validation_split))
            val_indices = indices[:n_val]
            train_indices = indices[n_val:]

            X_val = X[val_indices]
            X_train = X[train_indices]
        else:
            logger.warning(
                "validation_split=0.0. Threshold calibration will fall "
                "back to training reconstruction errors, which is less "
                "defensible methodologically."
            )
            X_train = X
            X_val = None

        self.training_samples = len(X_train)
        self.validation_samples = 0 if X_val is None else len(X_val)

        logger.info(
            "Training AutoEncoder | train_samples=%d | val_samples=%d | "
            "features=%d | batch_size=%d | epochs=%d",
            self.training_samples,
            self.validation_samples,
            X.shape[1],
            self.config.batch_size,
            self.config.epochs,
        )

        torch.manual_seed(self.config.random_seed)
        np.random.seed(self.config.random_seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.config.random_seed)

        train_loader = self._create_loader(X_train, shuffle=True)
        val_loader = (
            None if X_val is None else self._create_loader(X_val, shuffle=False)
        )

        optimizer = optim.Adam(
            self._model.parameters(),
            lr=self.config.learning_rate,
            weight_decay=self.config.weight_decay,
        )

        best_val_loss = float("inf")
        best_state_dict: Optional[dict] = None
        patience_counter = 0

        start_time = time.perf_counter()

        for epoch in range(1, self.config.epochs + 1):
            train_loss = self._run_train_epoch(train_loader, optimizer)
            val_loss = (
                self._evaluate_loss(val_loader) if val_loader is not None else train_loss
            )

            self.training_history["train_loss"].append(float(train_loss))
            self.training_history["validation_loss"].append(float(val_loss))

            if (
                epoch == 1
                or epoch % self.config.log_every_n_epochs == 0
                or epoch == self.config.epochs
            ):
                logger.info(
                    "Epoch %d/%d | train_loss=%.8f | validation_loss=%.8f",
                    epoch,
                    self.config.epochs,
                    train_loss,
                    val_loss,
                )

            if val_loss < best_val_loss - self.config.early_stopping_min_delta:
                best_val_loss = val_loss
                best_state_dict = deepcopy(self._model.state_dict())
                patience_counter = 0
            else:
                patience_counter += 1

            if (
                self.config.checkpoint_dir is not None
                and epoch % self.config.checkpoint_every_n_epochs == 0
            ):
                self._save_checkpoint(epoch, optimizer, val_loss)

            if (
                self.config.early_stopping_patience is not None
                and patience_counter >= self.config.early_stopping_patience
            ):
                logger.info("Early stopping triggered at epoch %d.", epoch)
                break

        if best_state_dict is not None:
            self._model.load_state_dict(best_state_dict)

        training_time = time.perf_counter() - start_time

        self._set_fitted(n_features=X.shape[1], training_time=training_time)

        threshold_source = X_val if X_val is not None else X_train
        threshold_errors = self._calculate_errors(threshold_source)
        self.threshold = self._calculate_threshold(threshold_errors)

        self.metadata.additional_info.update(
            {
                "device": str(self._device),
                "architecture": {
                    "input_dim": self.config.input_dim,
                    "hidden_dims": list(self.config.hidden_dims),
                    "latent_dim": self.config.latent_dim,
                },
                "reconstruction_loss": self.config.reconstruction_loss,
                "threshold_strategy": self.config.threshold_strategy,
                "threshold": self.threshold,
                "training_samples": self.training_samples,
                "validation_samples": self.validation_samples,
            }
        )

        logger.info(
            "AutoEncoder training completed | time=%.2fs | threshold=%.8f",
            training_time,
            self.threshold,
        )

        return self

    def _run_train_epoch(self, loader: DataLoader, optimizer: optim.Optimizer) -> float:
        """
        Run one training epoch.

        Args:
            loader: DataLoader over the training subset.
            optimizer: Optimizer used to update network parameters.

        Returns:
            Mean training loss, weighted by batch size.

        Raises:
            RuntimeError: If the loader yields no samples.
        """
        self._model.train()
        epoch_loss = 0.0
        epoch_samples = 0

        for (batch,) in loader:
            batch = batch.to(self._device, non_blocking=True)

            optimizer.zero_grad(set_to_none=True)
            reconstructed = self._model(batch)
            loss = self._loss_function(reconstructed, batch)
            loss.backward()

            if self.config.gradient_clip_norm is not None:
                nn.utils.clip_grad_norm_(
                    self._model.parameters(), self.config.gradient_clip_norm
                )

            optimizer.step()

            batch_size = batch.size(0)
            epoch_loss += loss.item() * batch_size
            epoch_samples += batch_size

        if epoch_samples == 0:
            raise RuntimeError("AutoEncoder training received no samples.")

        return epoch_loss / epoch_samples

    # ------------------------------------------------------------------
    # Inference
    # ------------------------------------------------------------------

    def _calculate_errors(self, X: np.ndarray) -> np.ndarray:
        """
        Compute per-sample reconstruction error for every row of X.

        Note: this internal helper assumes X has already been prepared
        (validated/cast to float32) by the caller, since it is also
        used during fit() on already-prepared subsets.

        Args:
            X: Prepared feature matrix.

        Returns:
            1D numpy array of per-sample reconstruction errors.
        """
        loader = self._create_loader(X, shuffle=False)
        self._model.eval()

        errors: list = []
        with torch.no_grad():
            for (batch,) in loader:
                batch = batch.to(self._device, non_blocking=True)
                reconstructed = self._model(batch)
                batch_errors = (
                    self._sample_reconstruction_errors(reconstructed, batch)
                    .detach()
                    .cpu()
                    .numpy()
                )
                errors.append(batch_errors)

        if not errors:
            return np.empty(0, dtype=np.float32)

        return np.concatenate(errors)

    def anomaly_score(self, X: np.ndarray) -> np.ndarray:
        """
        Compute per-sample anomaly scores (reconstruction error).

        Args:
            X: Feature matrix, shape (n_samples, input_dim).

        Returns:
            1D numpy array of anomaly scores, higher = more anomalous.

        Raises:
            RuntimeError: If the model has not been fitted yet.
        """
        self._check_is_fitted()
        X = self._prepare_input(X)

        scores = self._calculate_errors(X)

        logger.debug(
            "Computed anomaly scores for %d samples (mean=%.6f, max=%.6f).",
            scores.shape[0],
            float(np.mean(scores)) if scores.size else float("nan"),
            float(np.max(scores)) if scores.size else float("nan"),
        )

        return scores

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict binary anomaly labels using the calibrated threshold.

        Args:
            X: Feature matrix, shape (n_samples, input_dim).

        Returns:
            1D numpy array of predictions: 0 = normal, 1 = anomaly.

        Raises:
            RuntimeError: If the model has not been fitted yet, or the
                threshold has not been calibrated.
        """
        self._check_is_fitted()

        if self.threshold is None:
            raise RuntimeError(
                "AutoEncoder anomaly threshold has not been calculated."
            )

        scores = self.anomaly_score(X)
        predictions = (scores > self.threshold).astype(np.int8)

        logger.debug(
            "Predicted %d/%d samples as anomalous (threshold=%.6f).",
            int(predictions.sum()),
            predictions.shape[0],
            self.threshold,
        )

        return predictions

    # ------------------------------------------------------------------
    # Checkpointing
    # ------------------------------------------------------------------

    def _save_checkpoint(
        self, epoch: int, optimizer: optim.Optimizer, validation_loss: float
    ) -> None:
        """
        Write an intermediate raw PyTorch checkpoint to disk.

        Checkpoints are separate from the framework's save()/load()
        persistence (which uses joblib on the full wrapper); they exist
        purely to allow resuming/inspecting interrupted training runs.

        Args:
            epoch: Current 1-indexed epoch number.
            optimizer: Optimizer whose state should be checkpointed.
            validation_loss: Validation loss at this epoch.
        """
        if self.config.checkpoint_dir is None:
            return

        checkpoint_dir = Path(self.config.checkpoint_dir)
        checkpoint_dir.mkdir(parents=True, exist_ok=True)
        checkpoint_path = checkpoint_dir / f"autoencoder_epoch_{epoch:03d}.pt"

        torch.save(
            {
                "epoch": epoch,
                "model_state_dict": self._model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "validation_loss": validation_loss,
                "threshold": self.threshold,
                "config": self.config,
            },
            checkpoint_path,
        )

        logger.info("AutoEncoder checkpoint saved -> %s", checkpoint_path)

    # ------------------------------------------------------------------
    # Persistence (framework-standard joblib convention)
    # ------------------------------------------------------------------

    def save(self, filepath: str) -> None:
        """
        Save the complete AutoEncoder wrapper using the framework's
        standard joblib persistence convention, matching
        IsolationForestModel / LocalOutlierFactorModel / OneClassSVMModel.

        The underlying PyTorch network is moved to CPU before
        serialization so the saved file is device-independent.

        Args:
            filepath: Destination file path (e.g.
                "trained_models/autoencoder.joblib").

        Raises:
            RuntimeError: If the model has not been fitted yet.
        """
        self._check_is_fitted()

        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        original_device = self._device
        self._model.to(torch.device("cpu"))

        try:
            joblib.dump(self, filepath)
        finally:
            self._device = original_device
            self._model.to(original_device)

        logger.info("AutoEncoder saved -> %s", filepath)

    @classmethod
    def load(cls, filepath: str) -> "AutoEncoderModel":
        """
        Load a previously saved AutoEncoder wrapper.

        Args:
            filepath: Path to a file previously written by save().

        Returns:
            A fitted AutoEncoderModel instance, moved back onto the
            device resolved from its own config (which may differ
            from the device it was saved on).

        Raises:
            TypeError: If the deserialized object is not an
                AutoEncoderModel.
        """
        model = joblib.load(filepath)

        if not isinstance(model, cls):
            raise TypeError(f"Expected {cls.__name__}, got {type(model).__name__}.")

        model._device = model._resolve_device(model.config.device)
        model._model.to(model._device)

        logger.info("AutoEncoder loaded <- %s", filepath)

        return model

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"input_dim={self.config.input_dim}, "
            f"latent_dim={self.config.latent_dim}, "
            f"loss='{self.config.reconstruction_loss}', "
            f"device='{self._device}', "
            f"threshold={self.threshold}, "
            f"is_fitted={self.is_fitted})"
        )