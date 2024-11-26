class MaxHeap:
    # Class variables
    arr = []  # Array to hold the heap elements
    max_size = 0  # Maximum size of the heap
    heap_size = 0  # Current number of elements in the heap

    def __init__(self, max_size):
        """
        Initializes the MaxHeap with a given maximum size.
        Creates an empty array to hold heap elements.
        """
        self.max_size = max_size
        self.heap_size = 0
        self.arr = [None] * max_size

    def peek(self):
        """
        Returns the maximum element (root) without removing it.
        Raises an error if the heap is empty.
        """
        if self.heap_size == 0:
            raise IndexError("Heap is empty")
        return self.arr[0]

    def poll(self):
        """
        Removes and returns the maximum element (root).
        Replaces the root with the last element, reduces size, and re-heaps.
        """
        if self.heap_size == 0:
            raise IndexError("Heap is empty")
        root = self.arr[0]
        self.arr[0] = self.arr[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return root

    def max_heapify(self, i):
        """
        Ensures the subtree rooted at index i satisfies the max-heap property.
        Swaps the largest child with the root recursively until the property is restored.
        """
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < self.heap_size and self.arr[left] > self.arr[largest]:
            largest = left
        if right < self.heap_size and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)

    def parent(self, i):
        """
        Returns the index of the parent node for a given index i.
        """
        return (i - 1) // 2

    def lChild(self, i):
        """
        Returns the index of the left child of node at index i.
        """
        return 2 * i + 1

    def rChild(self, i):
        """
        Returns the index of the right child of node at index i.
        """
        return 2 * i + 2

    def remove_max(self):
        """
        Removes and returns the maximum element (root).
        Handles special cases when heap size is 1.
        """
        if self.heap_size == 0:
            raise IndexError("Heap is empty")
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.arr[0]

        root = self.arr[0]
        self.arr[0] = self.arr[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return root

    def increase_key(self, i, newVal):
        """
        Increases the value of an element at index i to newVal.
        Moves the element up the heap to restore the heap property.
        """
        self.arr[i] = newVal
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)

    def get_max(self):
        """
        Returns the maximum element (root) without removing it.
        """
        return self.arr[0]

    def cur_size(self):
        """
        Returns the current size of the heap (number of elements).
        """
        return self.heap_size

    def delete_key(self, i):
        """
        Deletes the element at index i by increasing its value to infinity
        and then removing it as the maximum element.
        """
        self.increase_key(i, float('inf'))
        self.remove_max()

    def insert_key(self, key):
        """
        Inserts a new key into the heap.
        Adds the key at the end and moves it up to maintain the heap property.
        Raises an error if the heap is full.
        """
        if self.heap_size == self.max_size:
            raise IndexError("Heap is full")

        self.heap_size += 1
        i = self.heap_size - 1
        self.arr[i] = key

        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)

        

if __name__ == "__main__":
    # Initialize a MaxHeap with a maximum size of 10
    heap = MaxHeap(10)

    # Test insert_key
    heap.insert_key(15)
    heap.insert_key(10)
    heap.insert_key(20)
    heap.insert_key(5)
    print("Heap after insertions:", heap.arr[:heap.heap_size])

    # Test get_max
    print("Maximum element:", heap.get_max())

    # Test remove_max
    print("Removed max:", heap.remove_max())
    print("Heap after removing max:", heap.arr[:heap.heap_size])

    # Test increase_key
    heap.insert_key(8)
    heap.increase_key(1, 25)
    print("Heap after increasing key:", heap.arr[:heap.heap_size])

    # Test delete_key
    heap.delete_key(0)
    print("Heap after deleting key at index 0:", heap.arr[:heap.heap_size])

    # Test cur_size
    print("Current size of heap:", heap.cur_size())

    # Test peek
    print("Peek max element:", heap.peek())

    # Test poll
    print("Polled max element:", heap.poll())
    print("Heap after polling:", heap.arr[:heap.heap_size])





        


        