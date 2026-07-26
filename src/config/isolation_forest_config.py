"""
Configuration for Isolation Forest.
"""

from dataclasses import dataclass
from typing import Literal


@dataclass(slots=True)
class IsolationForestConfig:
    """
    Configuration parameters for Isolation Forest.
    """

    n_estimators: int = 200

    contamination: float | Literal["auto"] = 0.05

    max_samples: int | float | Literal["auto"] = "auto"

    max_features: float = 1.0

    bootstrap: bool = False

    random_state: int = 42

    n_jobs: int = -1

    verbose: int = 0