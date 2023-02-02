#!/usr/bin/env python3
"""Annotate the given function."""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The type of the elements of the input were not known."""
    if lst:
        return lst[0]
    else:
        return None
