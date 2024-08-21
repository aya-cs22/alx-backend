#!/usr/bin/python3
"""MRU Caching"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching



class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.mru_key = None
        self.cache_order = [] 

    def put(self, key, item):
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if key in self.cache_order:
            self.cache_order.remove(key)
        
        self.cache_order.append(key)  

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.mru_key = self.cache_order.pop(-2) 
            del self.cache_data[self.mru_key]
            print(f"DISCARD: {self.mru_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        if key in self.cache_order:
            self.cache_order.remove(key)
        self.cache_order.append(key)

        return self.cache_data[key]