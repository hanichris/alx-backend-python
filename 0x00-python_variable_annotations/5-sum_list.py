#!/usr/bin/env python3
"""Type-annotated sum_list function to sum a list of floats."""
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum a list of floats and return result.

    Args:
        input_list (list[float]): list of floats.
    Return:
        float: cumulative sum of input.
    """
    if input_list is None:
        return 0
    return reduce(lambda x, y: x + y, input_list)
