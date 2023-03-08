#!/usr/bin/env python3
""" 5. Implementing an expiring web cache and tracker """

import requests
import redis


def get_page(url: str) -> str:
    """Obtains the HTML content of a particular URL and returns it"""
    redis_engine = redis.Redis()
    response = requests.get(url)
    count_key = f"count:{url}"
    content_key = f"content:{url}"
    redis_engine.incr(count_key)
    redis_engine.set(content_key, response.text, ex=10)
    return response.text
