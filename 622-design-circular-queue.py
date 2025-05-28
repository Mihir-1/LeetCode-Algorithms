class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = -1
        self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.rear == -1 or self.rear == self.size - 1:
            if self.rear == -1:
                self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.front] = None
        if self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1

        if self.queue[self.front] is None:
            self.front = -1
            self.rear = -1
        return True

    def Front(self) -> int:
        return self.queue[self.front] if self.front != -1 else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if self.rear != -1 else -1

    def isEmpty(self) -> bool:
        return True if self.front == -1 else False

    def isFull(self) -> bool:
        if self.front == -1:
            return False
        if (self.rear == self.size - 1 and self.front == 0) or self.front - 1 == self.rear:
            return True
        return False


'''


'''

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
