class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    def delmin(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        min_value = self.heap[0]
        last_value = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_value
            self._sift_down(0)
            
        return min_value
    def getmin(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]
    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2
    def _sift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_index = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest_index]:
            smallest_index = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest_index]:
            smallest_index = right_child_index
        if smallest_index != index:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self._sift_down(smallest_index)
minheap=MinHeap()
minheap.insert(5)
minheap.insert(3)
minheap.insert(8)
minheap.insert(1)
minheap.insert(10)
print(minheap.getmin())  
print(minheap.delmin())
print(minheap.getmin()) 
