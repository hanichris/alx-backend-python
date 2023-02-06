#!/usr/bin/env python3
"""Module containing an asynchronous coroutine.

Captures the basic of the asyncio module.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Make a random delay between 0 and `max_delay` and return it."""
    num = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(num)
    return num
