#!/usr/bin/env python3
"""0x0B redis basic"""

import redis
from typing import Union, Optional, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of the Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs for a particular function"""
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        """Wrapper function"""
        self._redis.rpush(input_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls of a particular function"""
    redis_engine = redis.Redis()
    qualname = method.__qualname__
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"
    input_list = redis_engine.lrange(input_key, 0, -1)
    output_list = redis_engine.lrange(output_key, 0, -1)
    print(f"{qualname} was called {int(redis_engine.get(qualname))} times:")
    for k, v in zip(input_list, output_list):
        if k:
            k = k.decode('utf-8')
        if v:
            v = v.decode('utf-8')
        print("{}(*{}) -> {}".format(qualname, k, v))


class Cache():
    """ Cache class using redis """

    def __init__(self):
        """ Init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
