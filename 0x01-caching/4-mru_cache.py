#!/usr/bin/python3
"""MRU caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache inherits from BaseCaching and implements a MRU caching system"""
    
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []  # لتتبع ترتيب المفاتيح

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove the key if it's already in cache
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # إزالة العنصر الأكثر استخدامًا مؤخرًا
                last_key = self.order.pop(-2)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        
        # إذا تم الوصول للمفتاح، ننقله لآخر قائمة الترتيب
        self.order.remove(key)
        self.order.append(key)
        
        return self.cache_data[key]
# #!/usr/bin/python3
# """LIFO caching system"""
# BaseCaching = __import__('base_caching').BaseCaching


# class MRUCache(BaseCaching):
#     """LIFOCache inherits from BaseCaching ,implements a LIFO caching system"""
#     def __init__(self):
#         """Initialize the class"""
#         super().__init__()
#         self.order = []

#     def put(self, key, item):
#         """Add an item in the cache"""
#         if key is not None and item is not None:
#             if key in self.cache_data:
#                 # Remove the key if it's already in cache
#                 self.order.remove(key)
#             self.order.append(key)
#             self.cache_data[key] = item

#             if len(self.cache_data) > BaseCaching.MAX_ITEMS:
#                 last_key = self.order.pop(-2)
#                 del self.cache_data[last_key]
#                 print(f"DISCARD: {last_key}")

#     def get(self, key):
#         """Get an item from the cache"""
#         return self.cache_data.get(key) if key is not None else None
