#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Chain the `wait_random` coroutine.

    Args:
        n (int): number of times to call `wait_random` coroutine.
        max_delay (int): wait time to pass to coroutine.
    Return:
        List[float]: list of all the `n` delay times.
    """
    res = []
    for i in range(n):
        res.append(await wait_random(max_delay))
    return res
