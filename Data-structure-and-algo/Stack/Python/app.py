print("******************* Stacks - push(), pop(), peek() using linked list")


class Node:
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # head is default NULL
    def __init__(self):
        self.head = None

    # Method to add data to the stack
    # adds to the start of the stack
    def push(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    # Remove element that is the current head (start of the stack)
    def pop(self):
        if self.isempty():
            return None

        else:
            # Removes the head node and makes
            # the preceding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    # Returns the head node data
    def peek(self):
        if self.isempty():
            return None

        else:
            return self.head.data

    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    # Prints out the stack
    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")

        else:
            while (iternode != None):
                print(iternode.data, end="")
                iternode = iternode.next
                if (iternode != None):
                    print(" -> ", end="")
            return

# Execution
s = Stack()
# push method
print("Push element into stack")
s.push(11)
s.push(22)
s.push(33)
s.push(44)
# Display stack elements
s.display()
print("\nRemove element from last node stack")
# Delete head of stack
print(s.pop())
# Print head of stack
print("Top element is", s.peek())
# Display stack elements
s.display()