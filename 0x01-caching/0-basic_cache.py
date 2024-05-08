#!/usr/bin/env python3
"""Creating a Basic Cache Class inheriting from BaseCaching and is a
caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Creating a Cache Class
    """

    def __init__(self):
        """Class Initialization Dunder Method"""
        super().__init__()

    def put(self, key, item):
        """Method for putting items in a dictionary"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Method that returns the value in self.cache_data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
