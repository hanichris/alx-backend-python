#!/usr/bin/env python3
"""Using `async` comprehensions instead of loops."""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Build a list using async comprehension."""
    return [i async for i in async_generator()]
