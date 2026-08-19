# Stack implementation using a Python list

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top:", stack.peek())
print("Popped:", stack.pop())
print("Top after pop:", stack.peek())
