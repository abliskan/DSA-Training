class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)  # Create a new node
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node  # Head now points to the new node

    def insert_at_the_end(self, new_data):
        new_node = Node(new_data)  # Create a new node
        current = self.head
        # Check if the list is empty
        if self.head is None:
            self.head = new_node # If the list is empty, make the new node the head
            return -1
        else:
            # Otherwise, traverse the list to find the last node
            while current.next:
                current = current.next
            current.next = new_node # Change the next of current node

    def display_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.key, end=" -> ")
            temp_node = temp_node.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(44)
    llist.insert_at_beginning(13)
    llist.insert_at_beginning(38)
    llist.insert_at_beginning(27)
    llist.insert_at_the_end(59)
    llist.display_list()
