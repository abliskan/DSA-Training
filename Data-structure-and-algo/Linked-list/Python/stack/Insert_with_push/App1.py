class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def display_list(self):
        iteration_node = self.head
        if self.head is None:
            print("Linked list is empty")
            return None
        else:
            while iteration_node is not None:
                print(iteration_node.data, end="")
                iteration_node = iteration_node.next
                if iteration_node is not None:
                    print(" -> ", end="")
            return -1


if __name__ == '__main__':
    llist = LinkedListStack()
    print("*** Created Linked List ***")
    llist.push(10)
    llist.push(44)
    llist.push(13)
    llist.push(38)
    llist.push(27)
    print("Linked list original: ")
    llist.display_list()