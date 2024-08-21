#!/usr/bin/python3
"""LRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache inherits from BaseCaching and implements an LRU caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # If the key is already in cache, move it to the end to mark it as recently used
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the least recently used item (the first item in the OrderedDict)
                lru_key, _ = self.cache_data.pop(0)
                print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Get an item from the cache"""
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end to mark it as recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
