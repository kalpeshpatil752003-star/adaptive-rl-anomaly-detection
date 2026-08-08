"""
src/evaluation/metrics.py

Reusable evaluation module for binary anomaly detection models.

This module provides a standardized way to compute, store, and report
classification metrics for anomaly detection experiments across all
models in the framework (Isolation Forest, Local Outlier Factor,
One-Class SVM, AutoEncoder, RL Ensemble, and future experiments).

Prediction convention:
    0 -> Normal
    1 -> Anomaly

Anomaly score convention:
    Higher score -> more anomalous
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

logger = logging.getLogger(__name__)


@dataclass
class EvaluationResult:
    """
    Container for the results of a single evaluation run.

    Attributes:
        model_name: Identifier of the model that produced these results.
        accuracy: Overall classification accuracy.
        precision: Precision score (positive class = anomaly = 1).
        recall: Recall score (positive class = anomaly = 1).
        f1: F1 score (positive class = anomaly = 1).
        roc_auc: Area under the ROC curve. None if it could not be computed.
        pr_auc: Area under the Precision-Recall curve (average precision).
            None if it could not be computed.
        true_positive_rate: TPR (sensitivity / recall).
        true_negative_rate: TNR (specificity).
        false_positive_rate: FPR.
        false_negative_rate: FNR.
        confusion_matrix: 2x2 numpy array [[TN, FP], [FN, TP]].
        classification_report_dict: sklearn classification report as a dict.
        n_samples: Total number of samples evaluated.
        n_anomalies: Number of true anomaly samples.
        n_normal: Number of true normal samples.
        notes: Free-text notes, e.g. warnings about degenerate cases.
    """

    model_name: str
    accuracy: float
    precision: float
    recall: float
    f1: float
    roc_auc: Optional[float]
    pr_auc: Optional[float]
    true_positive_rate: float
    true_negative_rate: float
    false_positive_rate: float
    false_negative_rate: float
    confusion_matrix: np.ndarray
    classification_report_dict: Dict[str, Any]
    n_samples: int
    n_anomalies: int
    n_normal: int
    notes: list = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the evaluation result into a flat dictionary.

        The confusion matrix is expanded into its four constituent
        counts (tn, fp, fn, tp) so the result can be serialized
        cleanly (e.g. to JSON or a DataFrame row).

        Returns:
            Dictionary representation of the evaluation result.
        """
        tn, fp, fn, tp = self.confusion_matrix.ravel()
        return {
            "model_name": self.model_name,
            "accuracy": self.accuracy,
            "precision": self.precision,
            "recall": self.recall,
            "f1": self.f1,
            "roc_auc": self.roc_auc,
            "pr_auc": self.pr_auc,
            "true_positive_rate": self.true_positive_rate,
            "true_negative_rate": self.true_negative_rate,
            "false_positive_rate": self.false_positive_rate,
            "false_negative_rate": self.false_negative_rate,
            "true_negatives": int(tn),
            "false_positives": int(fp),
            "false_negatives": int(fn),
            "true_positives": int(tp),
            "n_samples": self.n_samples,
            "n_anomalies": self.n_anomalies,
            "n_normal": self.n_normal,
            "notes": "; ".join(self.notes) if self.notes else "",
        }

    def to_dataframe(self) -> pd.DataFrame:
        """
        Convert the evaluation result into a single-row pandas DataFrame.

        Returns:
            A DataFrame with one row summarizing this evaluation result.
        """
        return pd.DataFrame([self.to_dict()])

    def summary(self) -> str:
        """
        Produce a human-readable, pretty console summary of the result.

        Returns:
            A formatted multi-line string suitable for printing.
        """
        roc_auc_str = f"{self.roc_auc:.4f}" if self.roc_auc is not None else "N/A"
        pr_auc_str = f"{self.pr_auc:.4f}" if self.pr_auc is not None else "N/A"
        tn, fp, fn, tp = self.confusion_matrix.ravel()

        lines = [
            "=" * 60,
            f"Evaluation Summary: {self.model_name}",
            "=" * 60,
            f"Samples          : {self.n_samples} "
            f"(Normal: {self.n_normal}, Anomaly: {self.n_anomalies})",
            "-" * 60,
            f"Accuracy         : {self.accuracy:.4f}",
            f"Precision        : {self.precision:.4f}",
            f"Recall           : {self.recall:.4f}",
            f"F1 Score         : {self.f1:.4f}",
            f"ROC-AUC          : {roc_auc_str}",
            f"PR-AUC           : {pr_auc_str}",
            "-" * 60,
            f"True Positive Rate  (TPR) : {self.true_positive_rate:.4f}",
            f"True Negative Rate  (TNR) : {self.true_negative_rate:.4f}",
            f"False Positive Rate (FPR) : {self.false_positive_rate:.4f}",
            f"False Negative Rate (FNR) : {self.false_negative_rate:.4f}",
            "-" * 60,
            "Confusion Matrix:",
            f"    TN: {int(tn):<8} FP: {int(fp):<8}",
            f"    FN: {int(fn):<8} TP: {int(tp):<8}",
            "=" * 60,
        ]

        if self.notes:
            lines.append("Notes:")
            for note in self.notes:
                lines.append(f"  - {note}")
            lines.append("=" * 60)

        return "\n".join(lines)


class MetricsEvaluator:
    """
    Computes standardized evaluation metrics for binary anomaly detection.

    This evaluator is model-agnostic: it operates purely on arrays of
    ground-truth labels, predicted labels, and (optionally) continuous
    anomaly scores. It is intended to be reused by every model in the
    framework (Isolation Forest, LOF, One-Class SVM, AutoEncoder,
    RL Ensemble, and future experiments).

    Label convention:
        0 -> Normal
        1 -> Anomaly (positive class)

    Anomaly score convention:
        Higher score -> more anomalous
    """

    POSITIVE_LABEL = 1
    NEGATIVE_LABEL = 0

    def __init__(self, zero_division: int = 0) -> None:
        """
        Initialize the MetricsEvaluator.

        Args:
            zero_division: Value to return for precision/recall/F1 when
                a metric is undefined due to a zero denominator
                (passed through to sklearn). Defaults to 0.
        """
        self.zero_division = zero_division
        logger.debug(
            "MetricsEvaluator initialized with zero_division=%s", zero_division
        )

    def evaluate(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        anomaly_scores: Optional[np.ndarray] = None,
        model_name: str = "UnnamedModel",
    ) -> EvaluationResult:
        """
        Compute the full suite of evaluation metrics.

        Args:
            y_true: Ground-truth binary labels (0 = normal, 1 = anomaly).
            y_pred: Predicted binary labels (0 = normal, 1 = anomaly).
            anomaly_scores: Optional continuous anomaly scores, where a
                higher value indicates a more anomalous sample. Required
                for ROC-AUC and PR-AUC computation.
            model_name: Identifier used to label this evaluation result.

        Returns:
            An EvaluationResult populated with all computed metrics.

        Raises:
            ValueError: If y_true and y_pred have mismatched shapes, or
                if either array is empty.
        """
        y_true = np.asarray(y_true).ravel()
        y_pred = np.asarray(y_pred).ravel()

        if y_true.shape[0] == 0 or y_pred.shape[0] == 0:
            raise ValueError("y_true and y_pred must not be empty.")
        if y_true.shape[0] != y_pred.shape[0]:
            raise ValueError(
                f"Shape mismatch: y_true has {y_true.shape[0]} samples, "
                f"y_pred has {y_pred.shape[0]} samples."
            )

        notes: list = []
        n_samples = int(y_true.shape[0])
        n_anomalies = int(np.sum(y_true == self.POSITIVE_LABEL))
        n_normal = int(np.sum(y_true == self.NEGATIVE_LABEL))

        logger.info(
            "Evaluating model '%s' on %d samples (normal=%d, anomaly=%d)",
            model_name,
            n_samples,
            n_normal,
            n_anomalies,
        )

        if n_anomalies == 0 or n_normal == 0:
            msg = (
                "y_true contains only a single class "
                f"(n_normal={n_normal}, n_anomalies={n_anomalies}). "
                "Some metrics may be degenerate or undefined."
            )
            logger.warning(msg)
            notes.append(msg)

        accuracy = float(accuracy_score(y_true, y_pred))
        precision = float(
            precision_score(
                y_true,
                y_pred,
                pos_label=self.POSITIVE_LABEL,
                zero_division=self.zero_division,
            )
        )
        recall = float(
            recall_score(
                y_true,
                y_pred,
                pos_label=self.POSITIVE_LABEL,
                zero_division=self.zero_division,
            )
        )
        f1 = float(
            f1_score(
                y_true,
                y_pred,
                pos_label=self.POSITIVE_LABEL,
                zero_division=self.zero_division,
            )
        )

        cm = confusion_matrix(
            y_true, y_pred, labels=[self.NEGATIVE_LABEL, self.POSITIVE_LABEL]
        )
        tn, fp, fn, tp = cm.ravel()

        tpr = float(tp / (tp + fn)) if (tp + fn) > 0 else 0.0
        tnr = float(tn / (tn + fp)) if (tn + fp) > 0 else 0.0
        fpr = float(fp / (fp + tn)) if (fp + tn) > 0 else 0.0
        fnr = float(fn / (fn + tp)) if (fn + tp) > 0 else 0.0

        class_report_dict = classification_report(
            y_true,
            y_pred,
            labels=[self.NEGATIVE_LABEL, self.POSITIVE_LABEL],
            target_names=["Normal", "Anomaly"],
            output_dict=True,
            zero_division=self.zero_division,
        )

        roc_auc = self._safe_roc_auc(y_true, anomaly_scores, notes)
        pr_auc = self._safe_pr_auc(y_true, anomaly_scores, notes)

        result = EvaluationResult(
            model_name=model_name,
            accuracy=accuracy,
            precision=precision,
            recall=recall,
            f1=f1,
            roc_auc=roc_auc,
            pr_auc=pr_auc,
            true_positive_rate=tpr,
            true_negative_rate=tnr,
            false_positive_rate=fpr,
            false_negative_rate=fnr,
            confusion_matrix=cm,
            classification_report_dict=class_report_dict,
            n_samples=n_samples,
            n_anomalies=n_anomalies,
            n_normal=n_normal,
            notes=notes,
        )

        logger.info(
            "Evaluation complete for '%s': accuracy=%.4f, precision=%.4f, "
            "recall=%.4f, f1=%.4f",
            model_name,
            accuracy,
            precision,
            recall,
            f1,
        )

        return result

    def _safe_roc_auc(
        self,
        y_true: np.ndarray,
        anomaly_scores: Optional[np.ndarray],
        notes: list,
    ) -> Optional[float]:
        """
        Safely compute ROC-AUC, handling unavailable scores or edge cases.

        Args:
            y_true: Ground-truth binary labels.
            anomaly_scores: Continuous anomaly scores, or None.
            notes: Mutable list that warning notes are appended to.

        Returns:
            The ROC-AUC score, or None if it could not be computed.
        """
        if anomaly_scores is None:
            note = "ROC-AUC not computed: anomaly_scores not provided."
            logger.warning(note)
            notes.append(note)
            return None

        anomaly_scores = np.asarray(anomaly_scores).ravel()

        if anomaly_scores.shape[0] != y_true.shape[0]:
            note = (
                "ROC-AUC not computed: anomaly_scores length "
                f"({anomaly_scores.shape[0]}) does not match y_true length "
                f"({y_true.shape[0]})."
            )
            logger.warning(note)
            notes.append(note)
            return None

        if len(np.unique(y_true)) < 2:
            note = "ROC-AUC not computed: y_true contains only a single class."
            logger.warning(note)
            notes.append(note)
            return None

        try:
            return float(roc_auc_score(y_true, anomaly_scores))
        except ValueError as exc:
            note = f"ROC-AUC not computed due to an error: {exc}"
            logger.warning(note)
            notes.append(note)
            return None

    def _safe_pr_auc(
        self,
        y_true: np.ndarray,
        anomaly_scores: Optional[np.ndarray],
        notes: list,
    ) -> Optional[float]:
        """
        Safely compute PR-AUC (average precision), handling edge cases.

        Args:
            y_true: Ground-truth binary labels.
            anomaly_scores: Continuous anomaly scores, or None.
            notes: Mutable list that warning notes are appended to.

        Returns:
            The PR-AUC (average precision) score, or None if it could
            not be computed.
        """
        if anomaly_scores is None:
            note = "PR-AUC not computed: anomaly_scores not provided."
            logger.warning(note)
            notes.append(note)
            return None

        anomaly_scores = np.asarray(anomaly_scores).ravel()

        if anomaly_scores.shape[0] != y_true.shape[0]:
            note = (
                "PR-AUC not computed: anomaly_scores length "
                f"({anomaly_scores.shape[0]}) does not match y_true length "
                f"({y_true.shape[0]})."
            )
            logger.warning(note)
            notes.append(note)
            return None

        if len(np.unique(y_true)) < 2:
            note = "PR-AUC not computed: y_true contains only a single class."
            logger.warning(note)
            notes.append(note)
            return None

        try:
            return float(
                average_precision_score(
                    y_true, anomaly_scores, pos_label=self.POSITIVE_LABEL
                )
            )
        except ValueError as exc:
            note = f"PR-AUC not computed due to an error: {exc}"
            logger.warning(note)
            notes.append(note)
            return None

    def compare(self, results: list) -> pd.DataFrame:
        """
        Combine multiple EvaluationResult objects into a comparison table.

        Args:
            results: A list of EvaluationResult instances.

        Returns:
            A pandas DataFrame with one row per model, suitable for
            side-by-side comparison of metrics.

        Raises:
            ValueError: If results is empty.
        """
        if not results:
            raise ValueError("results must contain at least one EvaluationResult.")

        rows = [r.to_dict() for r in results]
        df = pd.DataFrame(rows)
        logger.info("Built comparison table for %d model(s).", len(results))
        return df