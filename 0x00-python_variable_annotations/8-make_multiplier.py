#!/usr/bin/env python3
"""Type-annotated function that returns a callable function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the argument.

    Args:
        multiplier (float): argument to multiply a float.
    Return:
        func
    """
    def inner_func(num: float) -> float:
        """Multiply a float with multiplier."""
        return multiplier * num
    return inner_func
