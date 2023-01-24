#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random
    n times with the specified max_delay. wait_n should return
    the list of all the delays (float values). The list of the
    delays should be in ascending order without using sort()
    because of concurrency."""
    delays = [wait_random(max_delay) for i in range(0, n)]
    sorted_delays = []
    for await_random in asyncio.as_completed(delays):
        delay = await await_random
        sorted_delays.append(delay)
    return sorted_delays
