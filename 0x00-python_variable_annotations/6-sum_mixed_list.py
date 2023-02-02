#!/usr/bin/env python3
"""Type-annotated function that takes a list of ints and floats."""
from functools import reduce
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Compute the sum of a mix of integers and floats.

    Args:
        mxd_list (list[int | float]): list of ints and floats.
    Return:
        float: sum of the entries in the list.
    """
    return reduce(lambda x, y: x + y, mxd_lst)
