#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    res = []
    for i in range(n):
        res.append(await wait_random(max_delay))
    return res
