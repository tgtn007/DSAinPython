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


encodes = {}
reverse = {}
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

    return encoded_data, root


# Defining a function to assign code by using recursion
def coding(root, codes):
    if root is None:
        return

    if root.char is not None:
        encodes[root.char] = codes
        reverse[root.char] = root.char

    coding(root.left, codes + "0")
    coding(root.right, codes + "1")

def huffman_decoding(data,tree):
    encodes = ""
    decoded_data = ""
    for char in data:
        encodes += char
        if encodes in reverse:
            character = reverse[encodes]
            decoded_data += character
            encodes = ""
    return decoded_data



code, tree = huffman_encoding("The bird is the word")
decoded = huffman_decoding(code, tree)
print(code)
print(decoded)