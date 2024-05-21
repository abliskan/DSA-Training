# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Delete at first index
    def delete_at_first(self):
        # if linked list is empty
        if self.head is None:
            print("Empty,nothing to remove")
            return None

        # Point head to the second node
        self.head = self.head.next

    # Utility function to print the linked LinkedList
    def display_list(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" -> ")
            temp = temp.next


llist = LinkedList()
print("Created Linked List: ")
llist.insert_at_beginning(2)
llist.insert_at_beginning(3)
llist.insert_at_beginning(5)
llist.insert_at_beginning(6)
llist.display_list()
print("\nLinked List after deletion at first:")
llist.delete_at_first()
llist.display_list()
