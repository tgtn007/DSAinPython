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
            val = self.items.pop(key)           # Removing the element and adding to operate 'use' operation
            self.set(key, val)
            return val
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.length < self.capacity:
            self.items[key] = value
            self.length += 1
        elif key in self.items:         # If key already exists in cache, then no need to append, we'll overwrite.
            self.items[key] = value    
        else:                           # If cache overflows
            key_to_remove = list(self.items.keys())[0]
            del(self.items[key_to_remove])
            self.length -= 1
            self.set(key, value)        # To append now with updated length after deleting the least recently used cache.
            pass
        



# our_cache = LRU_Cache(5)
#
# our_cache.set(1, 1);
# our_cache.set(2, 2);
# our_cache.set(3, 3);
# our_cache.set(4, 4);
#
#
#
#
# print(our_cache.get(1))       # returns 1
# print(our_cache.get(2))       # returns 2
# print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
#
#
#
#
# our_cache.set(5, 5)
# our_cache.set(6, 6)
#
# print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

def test_function(capacity, input_list, expected_output, test_details):
    our_cache = LRU_Cache(capacity)
    print("Initialize cache with capacity: {}".format(capacity))
    for key, value in input_list:
        print("Set {}:{}".format(key, value))
        our_cache.set(key, value)
    linked_list = our_cache.dlinkedlist.print_ll()
    if linked_list == expected_output:
        print(test_details + ': Pass {}'.format(linked_list))
    else:
        print(test_details + ': Fail {}'.format(linked_list))


def test_function2(capacity, input_list, get_element, expected_output, test_details):
    our_cache = LRU_Cache(capacity)
    print("Initialize cache with capacity: {}".format(capacity))
    for key, value in input_list:
        print("Set {}:{}".format(key, value))
        our_cache.set(key, value)
    if our_cache.get(get_element) == expected_output:
        print(test_details + ': Pass, Return {} for get({})'.format(expected_output, key))
    else:
        print(test_details + ': Fail, Actual: {} Vs Expected: {}'.format(our_cache.get(get_element), expected_output))


def test_function3(capacity, input_list, get_list, expected_output, test_details):
    our_cache = LRU_Cache(capacity)
    print("Initialize cache with capacity: {}".format(capacity))
    for key, value in input_list:
        print("Set {}:{}".format(key, value))
        our_cache.set(key, value)
    for key in get_list:
        print("Get {} - {}".format(key, our_cache.get(key)))
        our_cache.get(key)
    linked_list = our_cache.dlinkedlist.print_ll()
    if linked_list == expected_output:
        print(test_details + ': Pass')
    else:
        print(test_details + ': Fail')


test_details = "Create a new linked list that keeps track of the last element set"
input_list = [(1, 1), (2, 2), (3, 3), (4, 4)]
expected_output = [4, 3, 2, 1]
capacity = 5
test_function(capacity, input_list, expected_output, test_details)  # Expected Output: Pass

test_details = "Handles None input"
input_list = [(1, 1), (None, 2), (3, 3), (4, 4)]
expected_output = [4, 3, 1]
capacity = 5
test_function(capacity, input_list, expected_output, test_details)  # Expected Output: Pass

test_details = "Discard old values when capacity is reached"
input_list = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
expected_output = [7, 6, 5, 4, 3]
capacity = 5
test_function(capacity, input_list, expected_output, test_details)  # Expected Output: Pass

test_details = 'Handles cache miss'
input_list = [(1, 1), (2, 2), (3, 3), (4, 4)]
get_element = 15
expected_output = -1
capacity = 5
test_function2(capacity, input_list, get_element, expected_output, test_details)  # Expected Output: Pass

test_details = 'Retrieve proper value when cache hit'
input_list = [(1, 1), (2, 2), (3, 3), (4, 4)]
get_element = 4
expected_output = 4
capacity = 5
test_function2(capacity, input_list, get_element, expected_output, test_details)  # Expected Output: Pass

test_details = 'Update Linked List with most recently used'
input_list = [(1, 1), (2, 2), (3, 3), (4, 4)]
get_list = [2, 1]
expected_output = [1, 2, 4, 3]
capacity = 5
test_function3(capacity, input_list, get_list, expected_output, test_details)  # Expected Output: Pass

