#!/usr/bin/python3
"""MRU Caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """LIFOCache inherits from BaseCaching ,implements a LIFO caching system"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove the key if it's already in cache
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.order.pop(-2)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
