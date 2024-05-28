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

    def search_item(self, item):
        temp_node = self.head  # Create temp_node to start with the head of the linked list
        node_position = 0  # Create a variable to keep track of the node position
        # Start traverse the linked list
        while temp_node:
            if temp_node.key == item:
                return f"Your item '{item}' is inside linked list at node {node_position}"
            temp_node = temp_node.next
            node_position += 1

        return f"Your item '{item}' isn't found on the linked list"

    # Utility function to print the LinkedList
    def display_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.key, end=" -> ")
            temp_node = temp_node.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(30)
    llist.insert_at_beginning(11)
    llist.insert_at_beginning(21)
    llist.insert_at_beginning(14)
    llist.display_list()
    print("\nCheck if number 100 is in the linked list!")
    print(llist.search_item(30))
