#!/usr/bin/env python3
"""Creating a LFU Cache Class inheriting from BaseCaching and is a
caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Creating a LFU Cache Class"""

    def __init__(self):
        """Class Initialization Dunder Method"""
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """Method for putting items in a dictionary"""
        if key is not None and item is not None:
            if (len(self.keys) == BaseCaching.MAX_ITEMS) and \
                    key not in self.keys:
                discard = self.keys.pop(self.keys.index(self.findLFU()))
                del self.cache_data[discard]
                del self.uses[discard]
                print(f"DISCARD: {discard:s}")
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.uses[key] = 0
            else:
                self.keys.append(
                    self.keys.pop(self.keys.index(key)))
                self.uses[key] += 1

    def get(self, key):
        """Method that returns the value in self.cache_data"""
        if key is not None and key in self.cache_data.keys():
            self.keys.append(
                self.keys.pop(self.keys.index(key)))
            self.uses[key] += 1
            return self.cache_data.get(key)
        return None

    def findLFU(self):
        """Method that return key with least frequencey of uses"""
        items = list(self.uses.items())
        freqs = [item[1] for item in items]
        least = min(freqs)

        lfus = [item[0] for item in items if item[1] == least]
        for key in self.keys:
            if key in lfus:
                return key
