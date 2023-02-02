#!/usr/bin/env python3
"""Type-annotated function which takes only two arguments.

The two arguments are a string and an int or float. It
returns its result as a tuple.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return the string and square of the int/float in a tuple.

    Args:
        k (str): First element of the tuple.
        v (int | float): Argument to be squared before being returned
                         as the second element of the tuple.
    Return:
        tuple: k, v^2
    """
    return k, v ** 2
