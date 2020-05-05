class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1 == None or llist_2 == None:
        return None
    union = LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head

    unique_nodes = set()      #     Remove duplicates
    while node1:
        unique_nodes.add(node1.value)
        node1 = node1.next
    while node2:
        unique_nodes.add(node2.value)
        node2 = node2.next

    for element in unique_nodes:        #     Remove duplicates
        union.append(element)

    return union

def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1 == None or llist_2 == None:
        return None
    intersection = LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head
    unique = set()
    while node1:
        unique.add(node1.value)
        node1 = node1.next

    while node2:
        if node2.value in unique:
            intersection.append(node2.value)
            unique.remove(node2.value)
        node2 = node2.next

    return intersection


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))  # Returns the list of union of linked list.
print (intersection(linked_list_1,linked_list_2))   # Returns the list of intersection of linked list.

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))  # Returns the list of union of linked list.
print (intersection(linked_list_3,linked_list_4)) # Returns None.