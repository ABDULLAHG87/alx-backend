#!/usr/bin/env python3
"""Creating a MRU Cache Class inheriting from BaseCaching and is a
caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Creating a Cache Class"""

    def __init__(self):
        """Class Initialization Dunder Method"""
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """Method for putting items in a dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
        if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
            discard = self.usedKeys.pop(-2)
            del self.cache_data[discard]
            print('DISCARD: {:s}'.format(discard))

        def get(self, key):
            """Method that returns the value in self.cache_data"""

            if key is not None and key in self.cache_data.keys():
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
                return self.cache_data.get(key)
            return None
