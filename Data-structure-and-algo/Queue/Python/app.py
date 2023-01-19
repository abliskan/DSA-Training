print("******************* queue - dequeue() + isEmpty()")


class Queue:
    # __init__ function
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Queue is full when size becomes
    # equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    # Function to remove an item from queue.
    # It changes front and size
    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    # Function to add an item to the queue.
    # It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return

        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue" % str(item))


queue = Queue(30)
queue.EnQueue(10)
queue.EnQueue(20)
queue.EnQueue(30)
queue.EnQueue(40)
queue.DeQueue()