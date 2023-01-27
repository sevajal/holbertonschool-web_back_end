#!/usr/bin/python3
""" 2. LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class for LIFOCache"""
    def __init__(self):
        """Init for LIFO"""
        super().__init__()

    def put(self, key, item):
        """Insert data into cache_data"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data)[-2]
                print('DISCARD: {}'.format(last_key))
                self.cache_data.pop(last_key)

    def get(self, key):
        """Obtain data from cache_data"""
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
