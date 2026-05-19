from collections import deque

class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = deque()  # For pushing elements
        self.stack2 = deque()  # For popping elements

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("pop from empty queue")
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("peek from empty queue")
        return self.stack2[-1]

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        return len(self.stack1) + len(self.stack2)

q = QueueUsingTwoStacks()
q.push(100)
q.push(200)
q.push(300)
print(q.peek())
print(q.size())
print(q.pop())      