class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

    def peek(self):
        if len(self) == 0:
            raise Exception("Stack is empty right know")
        return self.stack[0]


if __name__ == '__main__':
    stack1 = Stack()
    stack1.push(1)
    stack1.push(3)
    stack1.push(5)
    stack1.push(4)
    print("Current element on stack: " + str(stack1.stack))
    stack1.is_empty()
    print("Size of the stack:", stack1.stack_size())
