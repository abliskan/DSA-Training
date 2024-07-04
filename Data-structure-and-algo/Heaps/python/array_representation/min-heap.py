import sys


# defining a class min_heap for the heap data structure

class min_heap:
    def __init__(self, size_limit):
        self.size_limit = size_limit
        self.heap_size = 0
        self.heap = [0] * (self.size_limit + 1)
        self.heap[0] = sys.maxsize * -1
        self.root = 1

    # this function will be needed for heapify and insertion to swap nodes not in order
    def swap_nodes(self, node1, node2):
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]

    # THE MIN_HEAPIFY FUNCTION
    def heapify_min(self, i):
        # If the node is a not a leaf node and is greater than any of its child
        if not (i >= (self.heap_size // 2) and i <= self.heap_size):
            if (self.heap[i] > self.heap[2 * i] or self.heap[i] > self.heap[(2 * i) + 1]):
                if self.heap[2 * i] < self.heap[(2 * i) + 1]:
                    self.swap_nodes(i, 2 * i)
                    self.heapify_min(2 * i)
                else:
                    self.swap_nodes(i, (2 * i) + 1)
                    self.heapify_min((2 * i) + 1)

    # THE HEAPPUSH FUNCTION
    def heap_push(self, element):
        if self.heap_size >= self.size_limit:
            return
        self.heap_size += 1
        self.heap[self.heap_size] = element
        current = self.heap_size
        while self.heap[current] < self.heap[current // 2]:
            self.swap_nodes(current, current // 2)
            current = current // 2

    # THE HEAPPOP FUNCTION
    def heap_pop(self):
        previous = self.heap[self.root]
        self.heap[self.root] = self.heap[self.heap_size]
        self.heap_size -= 1
        self.heapify_min(self.root)
        return previous

    # THE CREATE HEAP FUNCTION
    def create_heap(self):
        for i in range(self.heap_size // 2, 0, -1):
            self.heapify_min(i)

    # Print the heap
    def display_heap(self):
        for i in range(1, (self.heap_size // 2) + 1):
            print("Parent Node is " + str(self.heap[i]) + " Left Child is " + str(
                self.heap[2 * i]) + " Right Child is " + str(self.heap[2 * i + 1]))


# Driver Code
if __name__ == '__main__':
    minHeap = min_heap(10)
    minHeap.heap_push(15)
    minHeap.heap_push(7)
    minHeap.heap_push(9)
    minHeap.heap_push(4)
    minHeap.heap_push(13)
    minHeap.heap_push(10)
    minHeap.heap_pop()
    minHeap.display_heap()
