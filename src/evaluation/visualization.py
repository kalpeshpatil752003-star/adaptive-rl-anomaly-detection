"""
src/evaluation/visualization.py

Publication-quality plotting utilities for anomaly detection evaluation
and benchmarking results.

All functions use matplotlib only (no seaborn) and return matplotlib
Figure objects rather than displaying them directly, so callers
(notebooks, reports, dashboards) retain full control over rendering
and saving.

This module is designed to be reused by every model in the framework
(Isolation Forest, Local Outlier Factor, One-Class SVM, AutoEncoder,
RL Ensemble, and future experiments), consuming the EvaluationResult
and BenchmarkResult objects produced by metrics.py and benchmark.py.
"""

from __future__ import annotations

import logging
from typing import List, Optional, Sequence

import matplotlib.figure
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import (
    auc,
    precision_recall_curve,
    roc_curve,
)

logger = logging.getLogger(__name__)

# Default figure sizing and styling constants, kept centralized so all
# plots share a consistent, publication-ready appearance.
_DEFAULT_FIGSIZE = (8, 6)
_DEFAULT_DPI = 120
_GRID_KWARGS = {"alpha": 0.3, "linestyle": "--"}


def _new_figure(
    figsize: Sequence[float] = _DEFAULT_FIGSIZE,
) -> matplotlib.figure.Figure:
    """
    Create a new matplotlib Figure/Axes pair with consistent styling.

    Args:
        figsize: Width and height of the figure in inches.

    Returns:
        A new matplotlib Figure instance.
    """
    fig, _ = plt.subplots(figsize=figsize, dpi=_DEFAULT_DPI)
    return fig


def plot_confusion_matrix(
    confusion_matrix: np.ndarray,
    model_name: str = "Model",
    class_names: Optional[Sequence[str]] = None,
    cmap: str = "Blues",
) -> matplotlib.figure.Figure:
    """
    Plot a confusion matrix as an annotated heatmap.

    Args:
        confusion_matrix: A 2x2 array in the form [[TN, FP], [FN, TP]],
            as produced by EvaluationResult.confusion_matrix.
        model_name: Name of the model, used in the plot title.
        class_names: Labels for the two classes. Defaults to
            ["Normal", "Anomaly"].
        cmap: Matplotlib colormap name used for the heatmap.

    Returns:
        A matplotlib Figure containing the confusion matrix plot.
    """
    if class_names is None:
        class_names = ["Normal", "Anomaly"]

    cm = np.asarray(confusion_matrix)
    logger.info("Plotting confusion matrix for '%s'.", model_name)

    fig, ax = plt.subplots(figsize=(6, 5.5), dpi=_DEFAULT_DPI)
    im = ax.imshow(cm, cmap=cmap, interpolation="nearest")

    ax.set_title(f"Confusion Matrix — {model_name}", fontsize=13, fontweight="bold")
    ax.set_xlabel("Predicted Label", fontsize=11)
    ax.set_ylabel("True Label", fontsize=11)
    ax.set_xticks(np.arange(len(class_names)))
    ax.set_yticks(np.arange(len(class_names)))
    ax.set_xticklabels(class_names)
    ax.set_yticklabels(class_names)

    threshold = cm.max() / 2.0 if cm.max() > 0 else 0.5
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            value = cm[i, j]
            text_color = "white" if value > threshold else "black"
            ax.text(
                j,
                i,
                f"{value}",
                ha="center",
                va="center",
                color=text_color,
                fontsize=12,
                fontweight="bold",
            )

    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="Count")
    fig.tight_layout()
    return fig


def plot_roc_curve(
    y_true: np.ndarray,
    anomaly_scores: np.ndarray,
    model_name: str = "Model",
) -> matplotlib.figure.Figure:
    """
    Plot a Receiver Operating Characteristic (ROC) curve.

    Args:
        y_true: Ground-truth binary labels (0 = normal, 1 = anomaly).
        anomaly_scores: Continuous anomaly scores, higher = more
            anomalous.
        model_name: Name of the model, used in the plot title and
            legend.

    Returns:
        A matplotlib Figure containing the ROC curve plot.

    Raises:
        ValueError: If y_true contains fewer than two classes.
    """
    y_true = np.asarray(y_true).ravel()
    anomaly_scores = np.asarray(anomaly_scores).ravel()

    if len(np.unique(y_true)) < 2:
        raise ValueError(
            "Cannot plot ROC curve: y_true contains only a single class."
        )

    logger.info("Plotting ROC curve for '%s'.", model_name)

    fpr, tpr, _ = roc_curve(y_true, anomaly_scores)
    roc_auc = auc(fpr, tpr)

    fig, ax = plt.subplots(figsize=_DEFAULT_FIGSIZE, dpi=_DEFAULT_DPI)
    ax.plot(
        fpr,
        tpr,
        color="#1f77b4",
        linewidth=2.0,
        label=f"{model_name} (AUC = {roc_auc:.4f})",
    )
    ax.plot(
        [0, 1],
        [0, 1],
        color="grey",
        linewidth=1.0,
        linestyle="--",
        label="Random Classifier",
    )

    ax.set_title(f"ROC Curve — {model_name}", fontsize=13, fontweight="bold")
    ax.set_xlabel("False Positive Rate", fontsize=11)
    ax.set_ylabel("True Positive Rate", fontsize=11)
    ax.set_xlim([-0.01, 1.01])
    ax.set_ylim([-0.01, 1.01])
    ax.grid(True, **_GRID_KWARGS)
    ax.legend(loc="lower right", fontsize=10)

    fig.tight_layout()
    return fig


def plot_precision_recall_curve(
    y_true: np.ndarray,
    anomaly_scores: np.ndarray,
    model_name: str = "Model",
) -> matplotlib.figure.Figure:
    """
    Plot a Precision-Recall curve.

    Args:
        y_true: Ground-truth binary labels (0 = normal, 1 = anomaly).
        anomaly_scores: Continuous anomaly scores, higher = more
            anomalous.
        model_name: Name of the model, used in the plot title and
            legend.

    Returns:
        A matplotlib Figure containing the precision-recall curve plot.

    Raises:
        ValueError: If y_true contains fewer than two classes.
    """
    y_true = np.asarray(y_true).ravel()
    anomaly_scores = np.asarray(anomaly_scores).ravel()

    if len(np.unique(y_true)) < 2:
        raise ValueError(
            "Cannot plot Precision-Recall curve: y_true contains only a "
            "single class."
        )

    logger.info("Plotting Precision-Recall curve for '%s'.", model_name)

    precision, recall, _ = precision_recall_curve(y_true, anomaly_scores)
    pr_auc = auc(recall, precision)
    baseline = float(np.mean(y_true == 1))

    fig, ax = plt.subplots(figsize=_DEFAULT_FIGSIZE, dpi=_DEFAULT_DPI)
    ax.plot(
        recall,
        precision,
        color="#d62728",
        linewidth=2.0,
        label=f"{model_name} (AUC = {pr_auc:.4f})",
    )
    ax.axhline(
        y=baseline,
        color="grey",
        linewidth=1.0,
        linestyle="--",
        label=f"Baseline (positive rate = {baseline:.4f})",
    )

    ax.set_title(
        f"Precision-Recall Curve — {model_name}", fontsize=13, fontweight="bold"
    )
    ax.set_xlabel("Recall", fontsize=11)
    ax.set_ylabel("Precision", fontsize=11)
    ax.set_xlim([-0.01, 1.01])
    ax.set_ylim([-0.01, 1.01])
    ax.grid(True, **_GRID_KWARGS)
    ax.legend(loc="lower left", fontsize=10)

    fig.tight_layout()
    return fig


def plot_anomaly_score_distribution(
    anomaly_scores: np.ndarray,
    y_true: Optional[np.ndarray] = None,
    model_name: str = "Model",
    bins: int = 50,
) -> matplotlib.figure.Figure:
    """
    Plot the distribution of anomaly scores as a histogram.

    If ground-truth labels are provided, normal and anomalous samples
    are overlaid as separate, semi-transparent histograms so their
    separation can be visually assessed.

    Args:
        anomaly_scores: Continuous anomaly scores, higher = more
            anomalous.
        y_true: Optional ground-truth binary labels (0 = normal,
            1 = anomaly). If provided, scores are split by class.
        model_name: Name of the model, used in the plot title.
        bins: Number of histogram bins.

    Returns:
        A matplotlib Figure containing the anomaly score distribution
        plot.
    """
    anomaly_scores = np.asarray(anomaly_scores).ravel()
    logger.info("Plotting anomaly score distribution for '%s'.", model_name)

    fig, ax = plt.subplots(figsize=_DEFAULT_FIGSIZE, dpi=_DEFAULT_DPI)

    if y_true is not None:
        y_true = np.asarray(y_true).ravel()
        normal_scores = anomaly_scores[y_true == 0]
        anomalous_scores = anomaly_scores[y_true == 1]

        if normal_scores.size > 0:
            ax.hist(
                normal_scores,
                bins=bins,
                alpha=0.6,
                color="#2ca02c",
                label="Normal",
                edgecolor="black",
                linewidth=0.3,
            )
        if anomalous_scores.size > 0:
            ax.hist(
                anomalous_scores,
                bins=bins,
                alpha=0.6,
                color="#d62728",
                label="Anomaly",
                edgecolor="black",
                linewidth=0.3,
            )
        ax.legend(loc="upper right", fontsize=10)
    else:
        ax.hist(
            anomaly_scores,
            bins=bins,
            alpha=0.75,
            color="#1f77b4",
            edgecolor="black",
            linewidth=0.3,
        )

    ax.set_title(
        f"Anomaly Score Distribution — {model_name}",
        fontsize=13,
        fontweight="bold",
    )
    ax.set_xlabel("Anomaly Score (higher = more anomalous)", fontsize=11)
    ax.set_ylabel("Frequency", fontsize=11)
    ax.grid(True, axis="y", **_GRID_KWARGS)

    fig.tight_layout()
    return fig


def _plot_timing_bar_chart(
    model_names: Sequence[str],
    times_seconds: Sequence[float],
    title: str,
    ylabel: str,
    color: str,
) -> matplotlib.figure.Figure:
    """
    Shared helper for rendering a bar chart of per-model timing values.

    Args:
        model_names: Names of the models being compared.
        times_seconds: Timing values in seconds, aligned with
            model_names.
        title: Plot title.
        ylabel: Y-axis label.
        color: Bar color.

    Returns:
        A matplotlib Figure containing the bar chart.
    """
    fig, ax = plt.subplots(
        figsize=(max(_DEFAULT_FIGSIZE[0], 0.9 * len(model_names)), _DEFAULT_FIGSIZE[1]),
        dpi=_DEFAULT_DPI,
    )

    x_positions = np.arange(len(model_names))
    bars = ax.bar(x_positions, times_seconds, color=color, edgecolor="black", linewidth=0.5)

    for bar, value in zip(bars, times_seconds):
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            bar.get_height(),
            f"{value:.4f}s",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_xlabel("Model", fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(model_names, rotation=20, ha="right")
    ax.grid(True, axis="y", **_GRID_KWARGS)

    fig.tight_layout()
    return fig


def plot_training_time(
    model_names: Sequence[str],
    training_times_seconds: Sequence[float],
) -> matplotlib.figure.Figure:
    """
    Plot a bar chart comparing training time across models.

    Args:
        model_names: Names of the benchmarked models.
        training_times_seconds: Training time in seconds for each
            model, aligned with model_names.

    Returns:
        A matplotlib Figure containing the training time comparison
        bar chart.

    Raises:
        ValueError: If model_names and training_times_seconds have
            mismatched lengths, or if either is empty.
    """
    if len(model_names) != len(training_times_seconds):
        raise ValueError(
            "model_names and training_times_seconds must have the same "
            "length."
        )
    if len(model_names) == 0:
        raise ValueError("model_names must not be empty.")

    logger.info("Plotting training time comparison for %d model(s).", len(model_names))

    return _plot_timing_bar_chart(
        model_names,
        training_times_seconds,
        title="Training Time Comparison",
        ylabel="Training Time (seconds)",
        color="#9467bd",
    )


def plot_inference_time(
    model_names: Sequence[str],
    prediction_times_seconds: Sequence[float],
    scoring_times_seconds: Optional[Sequence[float]] = None,
) -> matplotlib.figure.Figure:
    """
    Plot a bar chart comparing inference (prediction and, optionally,
    scoring) time across models.

    If scoring_times_seconds is provided, grouped bars are shown for
    prediction time vs. scoring time per model. Otherwise, a single
    bar per model is shown for prediction time only.

    Args:
        model_names: Names of the benchmarked models.
        prediction_times_seconds: Prediction time in seconds for each
            model, aligned with model_names.
        scoring_times_seconds: Optional anomaly-scoring time in
            seconds for each model, aligned with model_names.

    Returns:
        A matplotlib Figure containing the inference time comparison
        bar chart.

    Raises:
        ValueError: If input sequences have mismatched lengths, or if
            model_names is empty.
    """
    if len(model_names) != len(prediction_times_seconds):
        raise ValueError(
            "model_names and prediction_times_seconds must have the same "
            "length."
        )
    if len(model_names) == 0:
        raise ValueError("model_names must not be empty.")

    logger.info("Plotting inference time comparison for %d model(s).", len(model_names))

    if scoring_times_seconds is None:
        return _plot_timing_bar_chart(
            model_names,
            prediction_times_seconds,
            title="Inference (Prediction) Time Comparison",
            ylabel="Prediction Time (seconds)",
            color="#ff7f0e",
        )

    if len(scoring_times_seconds) != len(model_names):
        raise ValueError(
            "model_names and scoring_times_seconds must have the same "
            "length."
        )

    x_positions = np.arange(len(model_names))
    bar_width = 0.35

    fig, ax = plt.subplots(
        figsize=(max(_DEFAULT_FIGSIZE[0], 0.9 * len(model_names)), _DEFAULT_FIGSIZE[1]),
        dpi=_DEFAULT_DPI,
    )

    ax.bar(
        x_positions - bar_width / 2,
        prediction_times_seconds,
        width=bar_width,
        color="#ff7f0e",
        edgecolor="black",
        linewidth=0.5,
        label="Prediction Time",
    )
    ax.bar(
        x_positions + bar_width / 2,
        scoring_times_seconds,
        width=bar_width,
        color="#17becf",
        edgecolor="black",
        linewidth=0.5,
        label="Scoring Time",
    )

    ax.set_title(
        "Inference Time Comparison (Prediction vs. Scoring)",
        fontsize=13,
        fontweight="bold",
    )
    ax.set_xlabel("Model", fontsize=11)
    ax.set_ylabel("Time (seconds)", fontsize=11)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(model_names, rotation=20, ha="right")
    ax.grid(True, axis="y", **_GRID_KWARGS)
    ax.legend(loc="upper right", fontsize=10)

    fig.tight_layout()
    return fig


def plot_model_comparison(
    model_names: Sequence[str],
    metric_values: Sequence[float],
    metric_name: str = "F1 Score",
    higher_is_better: bool = True,
) -> matplotlib.figure.Figure:
    """
    Plot a bar chart comparing a single evaluation metric across
    multiple models, sorted from best to worst.

    Args:
        model_names: Names of the models being compared.
        metric_values: Metric values for each model, aligned with
            model_names.
        metric_name: Display name of the metric (e.g. "F1 Score",
            "ROC-AUC", "Accuracy"), used in the title and axis label.
        higher_is_better: If True, models are sorted in descending
            order of metric value (best first). If False, ascending
            order is used (e.g. for error-rate style metrics).

    Returns:
        A matplotlib Figure containing the model comparison bar chart.

    Raises:
        ValueError: If model_names and metric_values have mismatched
            lengths, or if either is empty.
    """
    if len(model_names) != len(metric_values):
        raise ValueError(
            "model_names and metric_values must have the same length."
        )
    if len(model_names) == 0:
        raise ValueError("model_names must not be empty.")

    logger.info(
        "Plotting model comparison on metric '%s' for %d model(s).",
        metric_name,
        len(model_names),
    )

    order = np.argsort(metric_values)
    if higher_is_better:
        order = order[::-1]

    sorted_names = [model_names[i] for i in order]
    sorted_values = [metric_values[i] for i in order]

    fig, ax = plt.subplots(
        figsize=(max(_DEFAULT_FIGSIZE[0], 0.9 * len(model_names)), _DEFAULT_FIGSIZE[1]),
        dpi=_DEFAULT_DPI,
    )

    colors = plt.cm.viridis(np.linspace(0.2, 0.85, len(sorted_names)))
    x_positions = np.arange(len(sorted_names))
    bars = ax.bar(
        x_positions,
        sorted_values,
        color=colors,
        edgecolor="black",
        linewidth=0.5,
    )

    for bar, value in zip(bars, sorted_values):
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            bar.get_height(),
            f"{value:.4f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    ax.set_title(
        f"Model Comparison — {metric_name}", fontsize=13, fontweight="bold"
    )
    ax.set_xlabel("Model", fontsize=11)
    ax.set_ylabel(metric_name, fontsize=11)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(sorted_names, rotation=20, ha="right")
    ax.grid(True, axis="y", **_GRID_KWARGS)

    fig.tight_layout()
    return fig