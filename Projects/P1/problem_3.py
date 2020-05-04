#!/usr/bin/env python
# coding: utf-8

# In[35]:


import sys
import heapq

class HeapNode:
    
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None

    def __lt__(self, compare):
        return self.freq < compare.freq

    def __eq__(self, compare):
        if compare is None:
            return -1
        if (not isinstance(compare, HeapNode)):
            return -1
        return self.freq == compare.freq


# In[39]:


encodes = {}  # Dictionary to store the encoded data
reverse = {}  # Dictionary to store the reversed data for decoding
def huffman_encoding(data):
    heap = []

    # Making frequency dict.
    frequency = {}
    for char in data:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1

    # Making the heap
    for key in frequency:
        temp = HeapNode(key, frequency[key])
        heapq.heappush(heap, temp)

    # Merging the nodes
    while len(heap) > 1:
        alpha = heapq.heappop(heap)
        beta = heapq.heappop(heap)

        merge = HeapNode(None, alpha.freq + beta.freq)

        merge.left = alpha
        merge.right = beta
        heapq.heappush(heap, merge)

    # Assigning Code to each nodes.
    codes = ""
    root = heapq.heappop(heap)
    coding(root, codes)

    encoded_data = ""
    for char in data:
        encoded_data += encodes[char]

#     print(encoded_data)
    return encoded_data, root


# Defining a function to assign code by using recursion
def coding(root, codes):
    if root is None:
        return

    if root.char is not None:
        encodes[root.char] = codes
        reverse[codes] = root.char

    coding(root.left, codes + "0")
    coding(root.right, codes + "1")


# In[40]:


def huffman_decoding(data,tree):
    encodes = ""
    decoded_data = ""
    # Searching for each data in reverse and appending to the list
    for char in data:
        encodes += char
        if encodes in reverse:
            character = reverse[encodes]
            decoded_data += character
            encodes = ""
    return decoded_data


# In[41]:


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

