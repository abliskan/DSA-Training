print("******************* Linked List - Traverse")
# Traversing using singly linked list
# Creating a node
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    # Traversal through linked List
    def Traversal(self):
        n = self.head
        while n is not None:
            print(n.data)
            n = n.next

list = LinkedList()
print("Insert value into linked list:")
list.head = Node("Monday")
l2 = Node("Tuesday")
l3 = Node("Wedneday")

# For traversing further, it is important to link each node, which is done by list.head.next = l2 and l2.next = l3.
# Link first Node to second
list.head.next = l2
# Link second Node to third node
l2.next = l3
list.Traversal()