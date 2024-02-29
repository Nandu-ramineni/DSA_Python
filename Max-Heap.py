class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self, x):
        self.heap.append(x)
        self._sift_up(len(self.heap) - 1)

    def delMin(self):
        if len(self.heap) == 0:
            return
        self._swap(0, len(self.heap) - 1)
        min_element = self.heap.pop()
        self._sift_down(0)
        return min_element

    def getMin(self):
        if len(self.heap) == 0:
            return "Empty"
        return self.heap[0]

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self._swap(parent_index, index)
            self._sift_up(parent_index)

    def _sift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self._swap(smallest, index)
            self._sift_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# Main code
t = int(input())
heap = MinHeap()
for _ in range(t):
    operation = input().split()
    if operation[0] == "insert":
        heap.insert(int(operation[1]))
    elif operation[0] == "delMin":
        heap.delMin()
    elif operation[0] == "getMin":
        print(heap.getMin())
        
#construct avl tree by inserting 10 to 1 