
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.capacity = capacity
        self.heap = [None] * (capacity + 1)
        self.size = 0

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator"""
        if not self.is_full():
            self.heap[self.size + 1] = item
            self.size += 1
            self.perc_up(self.size)
            return True
        return False

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""""
        if self.is_empty():
            return None
        else:
            return self.heap[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty():
            return None
        else:
            maximum = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.heap[self.size] = 0
            self.perc_down(1)
            self.perc_down(self.size)
            self.size -= 1
        return maximum

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        if self.is_empty():
            return []
        else:
            return self.heap[1:self.size + 1]

    def build_heap(self, alist):
        """Discards all items in the current heap and builds a heap from
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        self.size = 0
        if len(alist) > self.capacity:
            self.capacity = len(alist)
        self.heap = [0] + alist + [0] * (self.capacity - len(alist))
        self.size = len(alist)
        i = self.size // 2
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return self.size == 0

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return self.size == self.capacity

    def get_capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size

    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while 2 * i <= self.size:
            if 2 * i + 1 <= self.size and self.heap[2 * i] < self.heap[2 * i + 1]:
                maxc = 2 * i + 1
            else:
                maxc = 2 * i
            if self.heap[i] < self.heap[maxc]:
                temp = self.heap[maxc]
                self.heap[maxc] = self.heap[i]
                self.heap[i] = temp
            i = maxc

    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        parent = i // 2
        while parent > 0:
            if self.heap[parent] < self.heap[i]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[i]
                self.heap[i] = temp
                i = parent
            parent = parent // 2

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        self.build_heap(alist)
        for j in range(len(alist) - 1, -1, -1):
            alist[j] = self.dequeue()
