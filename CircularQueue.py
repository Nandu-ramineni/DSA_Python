class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.k == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full.")
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        elif self.front == self.rear:
            data = self.queue[self.front]
            self.front = self.rear = -1
            return data
        else:
            data = self.queue[self.front]
            self.front = (self.front + 1) % self.k
            return data

    def search(self, data):
        if self.is_empty():
            print("Queue is empty.")
        else:
            index = self.front
            while index != self.rear:
                if self.queue[index] == data:
                    return index
                index = (index + 1) % self.k
            if self.queue[index] == data:
                return index
            print("Element not found in the queue.")
            return -1

    def update(self, old_data, new_data):
        if self.is_empty():
            print("Queue is empty.")
        else:
            index = self.search(old_data)
            if index != -1:
                self.queue[index] = new_data
                print("Element updated successfully.")
            else:
                print("Element not found in the queue.")

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            index = self.front
            while index != self.rear:
                print(self.queue[index], end=" ")
                index = (index + 1) % self.k
            print(self.queue[index])


# Example usage:
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.display()  # Output: 1 2 3 4
cq.dequeue()
cq.display()  # Output: 2 3 4
cq.update(2, 5)
cq.display()  # Output: 5 3 4