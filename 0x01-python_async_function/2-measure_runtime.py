#!/usr/bin/env python3
"""2. Measure the runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. It should return a float.
    Use the time module to measure an approximate elapsed time."""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_execution = time.perf_counter() - start
    return time_execution
