#!/usr/bin/env python3
"""Type-annotated `floor` function."""


def floor(n: float) -> int:
    """Compute the floor of the float passed as an argument.

    Args:
        n (float): argument whose floor is to be determined.
    Return
        int: floor of the argument.
    """
    return int(n // 1)
