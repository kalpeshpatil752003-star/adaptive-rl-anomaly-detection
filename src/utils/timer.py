"""
Utility for measuring execution time.
"""

from __future__ import annotations

import time
from functools import wraps
from typing import Any, Callable

from src.utils.logger import get_logger

logger = get_logger()


class Timer:
    """
    Context manager for measuring execution time.

    Example
    -------
    with Timer("Data Loading"):
        load_data()
    """

    def __init__(self, name: str = "Operation") -> None:
        self.name = name
        self.start_time: float | None = None

    def __enter__(self) -> "Timer":
        self.start_time = time.perf_counter()
        logger.info(f"{self.name} started.")
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        elapsed = time.perf_counter() - self.start_time
        logger.info(f"{self.name} completed in {elapsed:.4f} seconds.")


def time_function(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to measure execution time of a function.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start

        logger.info(
            f"{func.__name__} executed in {elapsed:.4f} seconds."
        )

        return result

    return wrapper