#!/usr/bin/env python3
"""Task 4"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """async routine called task_wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn task_wait_random
    n times with the specified max_delay. wait_n should return
    the list of all the delays (float values). The list of the
    delays should be in ascending order without using sort()
    because of concurrency."""
    delays = [task_wait_random(max_delay) for i in range(0, n)]
    return [await task for task in asyncio.as_completed(delays)]
