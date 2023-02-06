#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async.

The asynchronous coroutine should return the list of all the delays
in ascending order by taking advantage of concurrency and NOT the
`sort` functionality.
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Chain the `task_wait_random` coroutine.

    The returned list should be in ascending order without using
    `sort()` functionality.
    Args:
        n (int): number of times to call `task_wait_random` coroutine.
        max_delay (int): wait time to pass to coroutine.
    Return:
        List[float]: list of all the `n` delay times.
    """
    # Create `n` number of tasks.
    coros = [task_wait_random(max_delay) for i in range(n)]
    # Append results as coroutines are completed.
    return [await coro for coro in asyncio.as_completed(coros)]
