#!/usr/bin/env python3
"""Module defining an async generator."""
import asyncio
import random


async def async_generator():
    """Coroutine that loops 10 times waiting asynchronously.

    During each loop, the coroutine waits asynchronously for
    1 second, after which it yields a random number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
