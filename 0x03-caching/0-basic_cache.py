#!/usr/bin/env python3
""" 0. Basic dictionary  """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class for BasicCache"""
    def __init__(self):
        """Init for Basic"""
        super().__init__()

    def put(self, key, item):
        """Insert data into cache_data"""
        if key:
            if item:
                self.cache_data[key] = item

    def get(self, key):
        """Obtain data from cache_data"""
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
