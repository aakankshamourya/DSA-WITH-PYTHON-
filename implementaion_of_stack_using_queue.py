"""
Implementation of stack using a single queue:
1) append item
2) rotate queue so last item becomes front
"""



from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)
        # Rotate the queue to make the last added item to be at the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
s = StackUsingQueue()
s.push(100)
s.push(200)
s.pop()
s.push(250)
s.pop()
s.push(300)
print(s.peek())
print(s.size())
print(s.peek())