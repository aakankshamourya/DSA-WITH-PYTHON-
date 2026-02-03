class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)
s=stack()
s=stack()
s.push(10)
s.push(20)
s.pop()
print(s.peek())
print(s.size())
print(s.is_empty())
s.push(120)
s.push(220)
s.push(320)
print(s.size())
    