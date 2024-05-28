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

    # Delete at last index
    def delete_at_the_end(self):
        # Check if the list is empty
        if self.head is None:
            print("Linked list is empty")
            return None

        # If there's only one node, remove the head by making it None
        if self.head.next is None:
            self.head = None
            print("First node already been deleted, linked list is empty now")
            return None
        else:
            # Otherwise, go to the second-last node
            previous_last = self.head
            while previous_last.next.next is not None:
                previous_last = previous_last.next

        previous_last.next = None  # Remove the last node by setting the next pointer of the previous last node to None

    # Utility function to print the linked LinkedList
    def display_list(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" -> ")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    print("Created Linked List: ")
    llist.insert_at_beginning(2)
    llist.insert_at_beginning(3)
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(6)
    llist.insert_at_beginning(4)
    llist.insert_at_beginning(7)
    llist.display_list()
    print("\nLinked List after deletion at last:")
    llist.delete_at_the_end()
    llist.display_list()
