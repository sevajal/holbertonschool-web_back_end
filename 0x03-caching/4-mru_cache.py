#!/usr/bin/python3
""" 4. MRU Caching  """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Class for MRUCache"""
    def __init__(self):
        """Init for MRUCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Insert data into cache_data"""
        max = BaseCaching.MAX_ITEMS - 1
        if len(self.cache_data) > max and key not in self.cache_data.keys():
            print('DISCARD: {}'.format(self.cache_data.popitem(last=True)[0]))
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Obtain data from cache_data"""
        if key and key in self.cache_data.keys():
            self.cache_data.move_to_end(key, last=True)
            return self.cache_data[key]
        return None
