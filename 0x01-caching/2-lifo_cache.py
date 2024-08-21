#!/usr/bin/python3
"""FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching and implements a FIFO caching system"""
    
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []  # To keep track of the order of keys

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Get an item from the cache"""
        return self.cache_data.get(key) if key is not None else None
# #!/usr/bin/python3
# """LIFO caching"""
# BaseCaching = __import__('base_caching').BaseCaching


# class LIFOCache(BaseCaching):
#     """ inherits from BaseCaching and is a caching system"""
#     def __init__(self):
#         """Initialize the class"""
#         super().__init__()
#         # To keep track of the order of keys in the dictionary self.cache_data
#         self.order = []

#     def put(self, key, item):
#         """Add an item in the cache"""
#         if key is not None and item is not None:
#             if key not in self.cache_data:
#                 self.order.append(key)
#             self.cache_data[key] = item
#             if len(self.cache_data) > BaseCaching.MAX_ITEMS:
#                 oldest_key = self.order.pop()
#                 del self.cache_data[oldest_key]
#                 print(f"DISCARD: {oldest_key}")

#     def get(self, key):
#         """Get an item from the cache"""
#         if key is not None:
#             return self.cache_data.get(key)
#         return None
