import time
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def retry(attempts: int = 3, base_delay: float = 0.25):
    """Retry a function with bounded exponential backoff."""
    if attempts < 1:
        raise ValueError("attempts must be >= 1")

    def decorator(func: Callable[P, R]):
        @wraps(func)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == attempts - 1:
                        raise
                    time.sleep(base_delay * (2**attempt))
            raise RuntimeError("unreachable")

        return wrapped

    return decorator
