# Exercise 15_04 - Decorator for Async Functions
# Given this

import asyncio
from functools import wraps
from typing import Callable, Literal

UnitType = Literal["h", "m", "s"]


# Extend this decorator to support async functions.


def time_it(
    _func: Callable | None = None,
    *,
    unit: UnitType = "s",
    decimals: int = 4,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # with log_execution_time(func, unit, decimals):
            return func(*args, **kwargs)

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            # with log_execution_time(func, unit, decimals):
            return await func(*args, **kwargs)

        return async_wrapper if asyncio.iscoroutinefunction(func) else wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)
