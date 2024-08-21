#!/usr/bin/python3
""" LRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        # To keep track of the order of keys in the dictionary self.cache_data
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Get an item from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        return None
