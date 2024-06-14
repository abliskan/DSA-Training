class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty right know")
        else:
            return self.queue.pop(0)

    def display_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.queue[0]

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    queue1 = Queue()
    queue1.enqueue(5)
    queue1.enqueue(1)
    queue1.enqueue(3)
    queue1.enqueue(7)
    print("Current element on Queue: " + str(queue1.queue))
    print("Size of the Queue: ", queue1.size())
    queue1.dequeue()
    print("Current element on Queue after pop(): " + str(queue1.queue))