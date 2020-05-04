### Problem 3
#### Huffman Encoding and Decoding

My choice of data structure to use in this problem was min heap, trees and dictionary.
Min heap was used to store the characters with its respective frequencies, and tree was used 
to create the huffman tree with characters in it.
The left child of huffman tree is encoded with 0 and right child with 1.
Then the dictionary was used to store the characters as keys and its encoded data as value.
By using the dictionary we easily found the encoded string of bytes.

The time complexity of code is O(N) that is the size of input to read each characters once while taking the frequency.
