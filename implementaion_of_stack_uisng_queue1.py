from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)
        # rotate to make new item top
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


s = StackUsingQueue()
s.push(100)
s.push(200)
s.push(150)
s.pop()
s.push(250)
s.pop()
s.push(300)
s.push(400)
print(s.peek())
print(s.size())
print(s.pop())
print(s.peek())