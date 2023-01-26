#!/usr/bin/python3
""" 0. Basic Cache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class for BasicCache"""
    def put(self, key, item):
        """Insert data into cache_data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Obtain data from cache_data"""
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
