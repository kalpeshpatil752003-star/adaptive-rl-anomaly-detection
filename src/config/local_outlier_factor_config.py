"""
Configuration for the Local Outlier Factor anomaly detection model.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(slots=True)
class LocalOutlierFactorConfig:
    """
    Configuration for sklearn.neighbors.LocalOutlierFactor.

    Parameters
    ----------
    n_neighbors : int
        Number of neighbors used to compute the local density.

    algorithm : {"auto", "ball_tree", "kd_tree", "brute"}
        Neighbor search algorithm.

    leaf_size : int
        Leaf size passed to BallTree or KDTree.

    metric : str
        Distance metric.

    p : int
        Power parameter for the Minkowski metric.

    contamination : float | {"auto"}
        Expected proportion of anomalies.

    novelty : bool
        Enables prediction on unseen data.
        Must remain True for deployment and inference.

    n_jobs : int
        Number of CPU cores used.
        -1 means use all available cores.
    """

    n_neighbors: int = 20

    algorithm: Literal[
        "auto",
        "ball_tree",
        "kd_tree",
        "brute",
    ] = "auto"

    leaf_size: int = 30

    metric: str = "minkowski"

    p: int = 2

    contamination: float | Literal["auto"] = 0.05

    novelty: bool = True


    random_state: int = 42

    n_jobs: int = -1

    max_training_samples: int = 100000

