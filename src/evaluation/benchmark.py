"""
src/evaluation/benchmark.py

Reusable performance benchmarking module for anomaly detection models.

This module measures training time, prediction time, and scoring time
for any model implementing the framework's standard interface
(fit(), predict(), anomaly_score()). It is model-agnostic and is
intended to be reused by every model in the framework (Isolation
Forest, LOF, One-Class SVM, AutoEncoder, RL Ensemble, and future
experiments).
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Protocol, runtime_checkable

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


@runtime_checkable
class BenchmarkableModel(Protocol):
    """
    Structural protocol describing the minimal interface a model must
    expose to be benchmarked by this module.

    Any model implementing fit(), predict(), and anomaly_score() with
    these signatures satisfies this protocol, regardless of its
    concrete base class.
    """

    def fit(self, X: np.ndarray, y: Optional[np.ndarray] = None) -> Any:
        ...

    def predict(self, X: np.ndarray) -> np.ndarray:
        ...

    def anomaly_score(self, X: np.ndarray) -> np.ndarray:
        ...


@dataclass
class BenchmarkResult:
    """
    Container for the timing results of a single model benchmark run.

    Attributes:
        model_name: Identifier of the benchmarked model.
        training_time_seconds: Wall-clock time spent in fit().
        prediction_time_seconds: Wall-clock time spent in predict().
        scoring_time_seconds: Wall-clock time spent in anomaly_score().
        n_train_samples: Number of samples used for training.
        n_predict_samples: Number of samples used for prediction/scoring.
        training_throughput_samples_per_sec: Training samples processed
            per second. None if training time is zero or unavailable.
        prediction_throughput_samples_per_sec: Prediction samples
            processed per second. None if prediction time is zero or
            unavailable.
        scoring_throughput_samples_per_sec: Scoring samples processed
            per second. None if scoring time is zero or unavailable.
        notes: Free-text notes, e.g. warnings about degenerate cases.
    """

    model_name: str
    training_time_seconds: float
    prediction_time_seconds: float
    scoring_time_seconds: float
    n_train_samples: int
    n_predict_samples: int
    training_throughput_samples_per_sec: Optional[float]
    prediction_throughput_samples_per_sec: Optional[float]
    scoring_throughput_samples_per_sec: Optional[float]
    notes: list = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the benchmark result into a flat dictionary.

        Returns:
            Dictionary representation of the benchmark result.
        """
        return {
            "model_name": self.model_name,
            "training_time_seconds": self.training_time_seconds,
            "prediction_time_seconds": self.prediction_time_seconds,
            "scoring_time_seconds": self.scoring_time_seconds,
            "n_train_samples": self.n_train_samples,
            "n_predict_samples": self.n_predict_samples,
            "training_throughput_samples_per_sec": (
                self.training_throughput_samples_per_sec
            ),
            "prediction_throughput_samples_per_sec": (
                self.prediction_throughput_samples_per_sec
            ),
            "scoring_throughput_samples_per_sec": (
                self.scoring_throughput_samples_per_sec
            ),
            "notes": "; ".join(self.notes) if self.notes else "",
        }

    def to_dataframe(self) -> pd.DataFrame:
        """
        Convert the benchmark result into a single-row pandas DataFrame.

        Returns:
            A DataFrame with one row summarizing this benchmark result.
        """
        return pd.DataFrame([self.to_dict()])

    def summary(self) -> str:
        """
        Produce a human-readable, pretty console summary of the result.

        Returns:
            A formatted multi-line string suitable for printing.
        """

        def _fmt_rate(rate: Optional[float]) -> str:
            return f"{rate:.2f} samples/sec" if rate is not None else "N/A"

        lines = [
            "=" * 60,
            f"Benchmark Summary: {self.model_name}",
            "=" * 60,
            f"Train samples    : {self.n_train_samples}",
            f"Predict samples  : {self.n_predict_samples}",
            "-" * 60,
            f"Training time    : {self.training_time_seconds:.6f} s "
            f"({_fmt_rate(self.training_throughput_samples_per_sec)})",
            f"Prediction time  : {self.prediction_time_seconds:.6f} s "
            f"({_fmt_rate(self.prediction_throughput_samples_per_sec)})",
            f"Scoring time     : {self.scoring_time_seconds:.6f} s "
            f"({_fmt_rate(self.scoring_throughput_samples_per_sec)})",
            "=" * 60,
        ]

        if self.notes:
            lines.append("Notes:")
            for note in self.notes:
                lines.append(f"  - {note}")
            lines.append("=" * 60)

        return "\n".join(lines)


class ModelBenchmark:
    """
    Benchmarks training, prediction, and scoring performance for any
    model implementing the framework's standard interface.

    A model is considered benchmarkable if it exposes:
        fit(X, y=None)
        predict(X)
        anomaly_score(X)
    """

    def __init__(self, n_repeats: int = 1) -> None:
        """
        Initialize the ModelBenchmark.

        Args:
            n_repeats: Number of times to repeat the predict() and
                anomaly_score() calls, with the average time reported.
                Repeating helps smooth out timing noise for fast
                models. Training is always measured once, since
                repeated fit() calls would refit the model and could
                mutate its internal state. Must be >= 1.

        Raises:
            ValueError: If n_repeats is less than 1.
        """
        if n_repeats < 1:
            raise ValueError("n_repeats must be >= 1.")
        self.n_repeats = n_repeats
        logger.debug("ModelBenchmark initialized with n_repeats=%d", n_repeats)

    def run(
        self,
        model: BenchmarkableModel,
        X_train: np.ndarray,
        X_test: np.ndarray,
        y_train: Optional[np.ndarray] = None,
        model_name: str = "UnnamedModel",
    ) -> BenchmarkResult:
        """
        Run a full benchmark cycle: fit, predict, and score.

        Args:
            model: A model instance implementing fit(), predict(), and
                anomaly_score().
            X_train: Training feature matrix.
            X_test: Feature matrix used for prediction and scoring
                timing.
            y_train: Optional training labels, passed through to
                fit() if the model accepts them.
            model_name: Identifier used to label this benchmark result.

        Returns:
            A BenchmarkResult populated with timing measurements.

        Raises:
            ValueError: If X_train or X_test is empty.
            TypeError: If the model does not implement the required
                fit()/predict()/anomaly_score() interface.
        """
        if not isinstance(model, BenchmarkableModel):
            raise TypeError(
                f"Model '{model_name}' does not implement the required "
                "fit()/predict()/anomaly_score() interface."
            )

        n_train_samples = int(np.asarray(X_train).shape[0])
        n_predict_samples = int(np.asarray(X_test).shape[0])

        if n_train_samples == 0:
            raise ValueError("X_train must not be empty.")
        if n_predict_samples == 0:
            raise ValueError("X_test must not be empty.")

        notes: list = []

        logger.info(
            "Benchmarking model '%s': train_samples=%d, predict_samples=%d, "
            "n_repeats=%d",
            model_name,
            n_train_samples,
            n_predict_samples,
            self.n_repeats,
        )

        training_time = self._time_call(
            model.fit, X_train, y_train, repeats=1
        )

        prediction_time = self._time_call(
            model.predict, X_test, repeats=self.n_repeats
        )

        scoring_time = self._time_call(
            model.anomaly_score, X_test, repeats=self.n_repeats
        )

        training_throughput = self._safe_throughput(
            n_train_samples, training_time, "training", notes
        )
        prediction_throughput = self._safe_throughput(
            n_predict_samples, prediction_time, "prediction", notes
        )
        scoring_throughput = self._safe_throughput(
            n_predict_samples, scoring_time, "scoring", notes
        )

        result = BenchmarkResult(
            model_name=model_name,
            training_time_seconds=training_time,
            prediction_time_seconds=prediction_time,
            scoring_time_seconds=scoring_time,
            n_train_samples=n_train_samples,
            n_predict_samples=n_predict_samples,
            training_throughput_samples_per_sec=training_throughput,
            prediction_throughput_samples_per_sec=prediction_throughput,
            scoring_throughput_samples_per_sec=scoring_throughput,
            notes=notes,
        )

        logger.info(
            "Benchmark complete for '%s': train=%.6fs, predict=%.6fs, "
            "score=%.6fs",
            model_name,
            training_time,
            prediction_time,
            scoring_time,
        )

        return result

    @staticmethod
    def _time_call(
        func: Any,
        *args: Any,
        repeats: int = 1,
    ) -> float:
        """
        Time repeated calls to a function and return the average
        elapsed wall-clock time in seconds.

        For fit(), args may include y_train, which some models ignore.
        None values are filtered out before the call so that models
        with an optional or absent y parameter are not passed None
        explicitly unless they accept it.

        Args:
            func: Callable to time (e.g. model.fit, model.predict).
            *args: Positional arguments to pass to the callable.
            repeats: Number of times to repeat the call. The average
                time across repeats is returned.

        Returns:
            Average elapsed time in seconds across all repeats.
        """
        call_args = tuple(a for a in args if a is not None) if len(
            args
        ) > 1 else args

        total_elapsed = 0.0
        for _ in range(repeats):
            start = time.perf_counter()
            func(*call_args)
            end = time.perf_counter()
            total_elapsed += end - start

        return total_elapsed / repeats

    @staticmethod
    def _safe_throughput(
        n_samples: int,
        elapsed_seconds: float,
        stage_name: str,
        notes: list,
    ) -> Optional[float]:
        """
        Safely compute a throughput rate (samples per second), guarding
        against division by zero for extremely fast operations.

        Args:
            n_samples: Number of samples processed in this stage.
            elapsed_seconds: Time taken to process the samples.
            stage_name: Name of the stage (for logging/notes purposes).
            notes: Mutable list that warning notes are appended to.

        Returns:
            Throughput in samples per second, or None if it could not
            be computed.
        """
        if elapsed_seconds <= 0.0:
            note = (
                f"{stage_name.capitalize()} throughput not computed: "
                "elapsed time was zero or negative (likely too fast to "
                "measure reliably)."
            )
            logger.warning(note)
            notes.append(note)
            return None

        return float(n_samples / elapsed_seconds)

    def compare(self, results: List[BenchmarkResult]) -> pd.DataFrame:
        """
        Combine multiple BenchmarkResult objects into a comparison table.

        Args:
            results: A list of BenchmarkResult instances.

        Returns:
            A pandas DataFrame with one row per model, suitable for
            side-by-side comparison of timing metrics, sorted by
            training time ascending.

        Raises:
            ValueError: If results is empty.
        """
        if not results:
            raise ValueError("results must contain at least one BenchmarkResult.")

        rows = [r.to_dict() for r in results]
        df = pd.DataFrame(rows)
        df = df.sort_values(
            by="training_time_seconds", ascending=True
        ).reset_index(drop=True)
        logger.info("Built benchmark comparison table for %d model(s).", len(results))
        return df