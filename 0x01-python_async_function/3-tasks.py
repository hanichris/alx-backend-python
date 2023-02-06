#!/usr/bin/env python3
"""Create a Task object for a given coroutine."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Wrap a coroutine into a Task object and schedule its execution.

    Args:
        max_delay (int): parameter to pass to the coroutine.
    Return:
        asyncio.Task: Future-like object to run the coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
