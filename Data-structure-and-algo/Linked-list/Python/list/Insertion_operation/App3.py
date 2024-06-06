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
        current = self.head # Next for new node becomes the   current head
        # Check if the list is empty
        if self.head is None:
            self.head = new_node # If the list is empty, make the new node the head
            return -1
        else:
            # Otherwise, traverse the list to find the last node
            while current.next:
                current = current.next
            current.next = new_node # Change the next of current node

    def insert_at_spesific_position(self, new_data, position):
        new_node = Node(new_data)  # Create a new node
        current = self.head  # Next for new node becomes the   current head
        index = 0

        # If the position is head
        if position == 0:
            # If linked list is empty
            if self.head is None:
                print("Linked list is empty")
                return new_node
            else:
                # Head needs to change
                new_node.next = current
                return new_node
        else:
            # Keep looping until the position same as index
            while position > 0:
                if position == index:
                    # Making the new Node to point to
                    # the old Node at the same position
                    new_node.next = current.next
                    # Replacing headNode with new Node
                    # to the old Node to point to the new Node
                    current.next = new_node
                    break
                index += 1
                current = current.next
            return current

    def display_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.key, end=" -> ")
            temp_node = temp_node.next


if __name__ == '__main__':
    llist = LinkedList()
    print("*** Created Linked List ***")
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(44)
    llist.insert_at_beginning(13)
    llist.insert_at_beginning(38)
    llist.insert_at_beginning(27)
    print("Linked list original: ")
    llist.display_list()
    print("Linked list after insert 81 at position 4: ")
    data = 81
    new_index = 4
    llist.insert_at_spesific_position(data, new_index)
    llist.display_list()



