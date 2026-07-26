"""
Utility functions for reproducible experiments.
"""

from __future__ import annotations

import os
import random

import numpy as np
import torch


def set_seed(seed: int = 42, deterministic: bool = True) -> None:
    """
    Set random seed for Python, NumPy, and PyTorch.

    Parameters
    ----------
    seed : int
        Random seed value.
    deterministic : bool
        If True, enables deterministic CUDA behavior for reproducibility.
    """

    random.seed(seed)
    np.random.seed(seed)

    os.environ["PYTHONHASHSEED"] = str(seed)

    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    if deterministic:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    else:
        torch.backends.cudnn.deterministic = False
        torch.backends.cudnn.benchmark = True


def seed_worker(worker_id: int) -> None:
    """
    Seed DataLoader workers for reproducibility.

    Parameters
    ----------
    worker_id : int
        Worker ID assigned by PyTorch DataLoader.
    """

    worker_seed = torch.initial_seed() % (2**32)

    np.random.seed(worker_seed)
    random.seed(worker_seed)


def create_generator(seed: int = 42) -> torch.Generator:
    """
    Create a seeded PyTorch Generator.

    Parameters
    ----------
    seed : int
        Random seed.

    Returns
    -------
    torch.Generator
        Seeded generator.
    """

    generator = torch.Generator()
    generator.manual_seed(seed)
    return generator