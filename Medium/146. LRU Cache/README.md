An LRU (Least Recently Used) cache is a data structure that stores a fixed number of items in memory and removes the least recently used item when the cache becomes full. This helps to speed up access to frequently used data and reduce the amount of time spent on slow I/O operations.

In this Python implementation, an LRU Cache is created using an OrderedDict. An OrderedDict is a dictionary that maintains the order in which its items were inserted. This makes it easy to track the least recently used item in the cache and remove it when necessary.

The LRUCache class has two methods: get and put. The get method takes a key as input and returns the corresponding value if it exists in the cache, otherwise it returns -1. If the key is present in the cache, the method updates the position of the key in the OrderedDict to indicate that it was recently used.

The put method takes a key-value pair as input and adds it to the cache. If the key is already present in the cache, the method updates the value and updates the position of the key in the OrderedDict to indicate that it was recently used. If the cache is full, the method evicts the least recently used item from the cache before adding the new key-value pair.

Overall, this implementation provides an efficient solution to the problem of caching in Python using an OrderedDict.
