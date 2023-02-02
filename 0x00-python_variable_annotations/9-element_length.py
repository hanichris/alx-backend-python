#!/usr/bin/env python3
"""Annotate a provided function."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples."""
    return [(i, len(i)) for i in lst]
