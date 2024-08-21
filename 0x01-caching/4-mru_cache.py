#!/usr/bin/python3
"""MRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache inherits from BaseCaching, implements an MRU caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        # To keep track of the order of keys in the dictionary self.cache_data
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # If the key is already in cache, remove it from the order list
                self.order.remove(key)
            self.cache_data[key] = item
            # Add the key to the order list
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the most recently used item (last item in the order list)
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

    def get(self, key):
        """Get an item from the cache"""
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end to mark it as most recently used
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
# #!/usr/bin/python3
# """MRU Caching"""
# from collections import OrderedDict
# BaseCaching = __import__('base_caching').BaseCaching


# class MRUCache(BaseCaching):
#     """ inherits from BaseCaching and is a caching system"""
#     def __init__(self):
#         """Initialize the class"""
#         super().__init__()
#         # To keep track of the order of keys in the dictionary self.cache_data
#         self.order = []

#     def put(self, key, item):
#         """Add an item in the cache"""
#         if key is not None and item is not None:
#             if key in self.cache_data:
#                 self.order.remove(key)
#             self.cache_data[key] = item
#             self.order.append(key)
#             if len(self.cache_data) > BaseCaching.MAX_ITEMS:
#                 last_key = self.order.pop()
#                 del self.cache_data[last_key]
#                 print(f"DISCARD: {last_key}")

#     def get(self, key):
#         """Get an item from the cache"""
#         if key is not None:
#             self.order.remove(key)
#             self.order.append(key)
#             return self.cache_data.get(key)
#         return None