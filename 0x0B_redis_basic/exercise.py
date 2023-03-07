#!/usr/bin/env python3
"""0x0B redis basic"""

import redis
from typing import Union
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
