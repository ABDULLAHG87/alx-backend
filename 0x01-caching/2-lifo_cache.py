#!/usr/bin/env python3
"""Creating a LIFO Cache Class inheriting from BaseCaching and is a
caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                last_key, last_value = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Method that returns the value in self.cache_data"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
