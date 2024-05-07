#!/usr/bin/env python3
"""An asynchronous coroutine that takes an integer argument"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """A max delay function that has default b/n 0 and 10"""

    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
