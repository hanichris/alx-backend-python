#!/usr/bin/env python3
"""Type-annotated string concatenation function."""


def concat(str1: str, str2: str) -> str:
    """Create a concatenated string from the given parameters.

    Args:
        str1 (string): first argument.
        str2 (string): second argument.
    Return:
        str1 + str2 (string)
    """
    return f'{str1}{str2}'
