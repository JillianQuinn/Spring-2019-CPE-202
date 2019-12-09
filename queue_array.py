class Queue:
    """Implements an array-based, efficient first-in first-out Abstract Data Type
       using a Python array (faked using a List)"""

    def __init__(self, capacity):
        """Creates an empty Queue with a capacity"""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.back = 0
        self.num_items = 0

    def is_empty(self):
        """Returns True if the Queue is empty, and False otherwise"""
        return self.num_items == 0

    def is_full(self):
        """Returns True if the Queue is full, and False otherwise"""
        return self.num_items == self.capacity

    def enqueue(self, item):
        """If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError"""
        if not self.is_full():
            self.queue[self.back] = item
            self.back += 1
            self.num_items += 1
            if self.back == self.capacity:
                self.back = 0
        else:
            raise IndexError

    def dequeue(self):
        """If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError"""
        if not self.is_empty():
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            self.num_items -= 1
            if self.front >= self.capacity:
                self.front = 0
            return item
        else:
            raise IndexError

    def size(self):
        """Returns the number of elements currently in the Queue, not the capacity"""
        return self.num_items

