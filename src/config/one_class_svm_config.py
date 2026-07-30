"""
Configuration for the One-Class SVM anomaly detection model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class OneClassSVMConfig:
    """
    Configuration for One-Class SVM.
    """

    kernel: str = "rbf"

    degree: int = 3

    gamma: str | float = "scale"

    coef0: float = 0.0

    tol: float = 1e-3

    nu: float = 0.05

    shrinking: bool = True

    cache_size: int = 200

    verbose: bool = False

    max_iter: int = -1

    random_state: int = 42

    max_training_samples: int = 50000