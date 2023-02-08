#!/usr/bin/env python3
"""Measure the time taken by an asynchronous function to complete.

Execute `async_comprehension` four times in parallel and measure
the total time taken to run.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Make 4 concurrent calls of the `async_comprehension` coroutine.

    Measure and return the total time taken to run the coroutine in
    parallel.
    Return:
        float: total time taken.
    """
    start = time.perf_counter()
    coros = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coros)
    end = time.perf_counter() - start
    return end
