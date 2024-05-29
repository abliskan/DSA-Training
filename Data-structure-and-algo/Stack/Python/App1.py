class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

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
