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

    def delete_at_spesific_position(self, position):
        # Store head node
        current = self.head
        index = 0

        # If linked list is empty
        if self.head is None:
            print("Linked list is empty")
            return None

        # If head needs to be removed
        if position == 0:
            self.head = current.next
            current = None
            return None

        if position >= 1:
            while current.next and index < position:
                previous = current
                current = current.next
                index += 1
            print("\nDelete element on index:", index)
            if index < position:
                print("\nIndex is out of range.")
            else:
                previous.next = current.next
                current = None

    # Utility function to print the linked LinkedList
    def display_list(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print("\n")


if __name__ == '__main__':
    llist = LinkedList()
    print("*** Created Linked List ***")
    llist.insert_at_beginning(2)
    llist.insert_at_beginning(3)
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(6)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(8)
    print("Linked list original: ")
    llist.display_list()
    llist.delete_at_spesific_position(4)
    print("Linked list after deletion: ")
    llist.display_list()
