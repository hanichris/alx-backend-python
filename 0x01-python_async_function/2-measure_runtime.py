#!/usr/bin/env python3
"""Measure the time taken by an asynchronous function to complete.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Compute the time taken by `wait_n` to complete.

    Args:
        n (int): number of times to execute `wait_random` coroutine.
        max_delay (int): wait time to pass to the coroutine.
    Return:
        float: time elapsed in executing the asynchronous function.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start
    return end / n
