#!/usr/bin/env python3
""" 3. LRU Caching  """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Class for LRUCache"""
    def __init__(self):
        """Init for LRU"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Insert data into cache_data"""
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(
                    self.cache_data.popitem(last=False)[0]))

    def get(self, key):
        """Obtain data from cache_data"""
        if key and key in self.cache_data.keys():
            self.cache_data.move_to_end(key, last=True)
            return self.cache_data[key]
        return None
