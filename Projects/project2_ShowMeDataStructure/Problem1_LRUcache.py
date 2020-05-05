#!/usr/bin/env python
# coding: utf-8


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.items = dict()
        self.length = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.items:
            val = self.items.pop(key)  # Removing the element and adding to operate 'use' operation
            self.set(key, val)
            return val
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.length < self.capacity:
            self.items[key] = value
            self.length += 1
        elif key in self.items:  # If key already exists in cache, then no need to append, we'll overwrite.
            self.items[key] = value
        else:  # If cache overflows
            key_to_remove = list(self.items.keys())[0]
            del (self.items[key_to_remove])
            self.length -= 1
            self.set(key, value)  # To append now with updated length after deleting the least recently used cache.
            pass


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
