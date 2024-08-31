# Exercise 100 - Decorator for Async Functions
# Given the following `time_it` decorator, extend it to support async functions.
# NOTE: To run the unit tests for this exercise, you need to install the following:
# $ pip install pytest pytest-asyncio

import asyncio
from functools import wraps
import timeit
from typing import Callable, Any


def time_it(
    _func: Callable | None = None,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start = timeit.default_timer()
            result = func(*args, **kwargs)
            end = timeit.default_timer()
            print(f"Time taken for {func.__name__}: {end - start:.4f} seconds")
            return result

        @wraps(func)
        async def async_wrapper(*args, **kwargs) -> Any:
            start = timeit.default_timer()
            result = await func(*args, **kwargs)
            end = timeit.default_timer()
            print(f"Time taken for {func.__name__}: {end - start:.4f} seconds")
            return result

        return async_wrapper if asyncio.iscoroutinefunction(func) else wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)
