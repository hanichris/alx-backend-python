#!/usr/bin/env python3
"""Annotate the function below."""
from typing import Any, Mapping, Optional, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Optional[T] = None
                     ) -> Union[Any, T]:
    """Safely get a value from the dictionary.

    Args:
        dct (dict): Dictionary to get value from.
        key (any): key of the value of interest.
        default (T): Value to return if key isn't found.
    Return:
        Any | T: Value from the dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
