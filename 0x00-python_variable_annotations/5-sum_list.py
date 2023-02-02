#!/usr/bin/env python
"""Type-annotated sum_list function to sum a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum a list of floats and return result.

    Args:
        input_list (list[float]): list of floats.
    Return:
        float: cumulative sum of input.
    """
    accumulator = 0.0
    for num in input_list:
        accumulator += num
    return accumulator
