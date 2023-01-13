print("******************* Linked List - search(from start to end node)")
# Examples: Input: 14->21->11->30->10, X = 14, Output: Yes, Explanation: 14 is present in the linked list.
# Input: 6->21->17->30->10->8, X = 13, Output: No
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    # This function insert a new node at the
    # beginning of the linked list
    def push(self, new_data):

        # Create a new Node
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # This Function checks whether the value
    # x present in the linked list
    def search(self, x):
        # Initialize current to head
        current = self.head

        # loop till current not equal to None
        while current != None:
            if current.data == x:
                return True  # data found

            current = current.next

        return False  # Data Not found

    def printList(self):
        temp = self.head
        while (temp):
            print(" %d" % (temp.data)),
            temp = temp.next

# Driver code
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    print("Created Linked List: ")
    ''' Use push() to construct below list
        14->21->11->30->10 '''
    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)
    llist.printList()

    # Function call
    print("Search for number 21: ")
    if llist.search(21):
        print("Found")
    else:
        print("Not found")

    print("Search for number 100: ")
    if llist.search(100):
        print("Found")
    else:
        print("Not found")