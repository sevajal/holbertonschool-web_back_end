#!/usr/bin/python3
""" 1. FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class for FIFOCache"""
    def __init__(self):
        """Init for FIFO"""
        super().__init__()

    def put(self, key, item):
        """Insert data into cache_data"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(first_key))
                self.cache_data.pop(first_key)

    def get(self, key):
        """Obtain data from cache_data"""
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
