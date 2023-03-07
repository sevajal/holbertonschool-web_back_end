#!/usr/bin/env python3
"""0x0B redis basic"""

import redis
from typing import Union, Optional, Callable
import uuid


class Cache():
    """ Cache class using redis """

    def __init__(self):
        """ Init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random key and stores data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """Gets a key from Redis and change the format"""
        if fn:
            return fn(self._redis.get(key))
        return (self._redis.get(key))

    def get_str(self, key: str) -> str:
        """Returns a str from redis"""
        return (self.get(key, str))

    def get_int(self, key: str) -> int:
        """Returns an int from redis"""
        return (self.get(key, int))
