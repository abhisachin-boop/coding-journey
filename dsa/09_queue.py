# Queue implementation using collections.deque

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.popleft()

    def front(self):
        if not self.items:
            return None
        return self.items[0]

    def is_empty(self):
        return not self.items


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front:", queue.front())
print("Dequeued:", queue.dequeue())
print("Front after dequeue:", queue.front())
