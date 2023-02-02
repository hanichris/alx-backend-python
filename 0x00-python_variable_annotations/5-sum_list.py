#!/usr/bin/env python
"""Type-annotated sum_list function to sum a list of floats."""
from functools import reduce
from typing import Iterable


def sum_list(input_list: Iterable[float]) -> float:
    """Sum a list of floats and return result.

    Args:
        input_list (list[float]): list of floats.
    Return:
        float: cumulative sum of input.
    """
    return reduce(lambda x, y: x + y, input_list)
