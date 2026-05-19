class Queue:
    def __init__(self):
        self.item = []
    
    def is_empty(self):
        return len(self.item) == 0
    
    def front(self):
        return self.item[0]

    def enqueue(self,item):
        return self.item.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.item.pop(0)
    
        

    def push(self,item):
        self.item.append(item)
    def pop(self):
        if self.item==0:
            return 'empty queue'
        return self.item.pop(0)
    def peek(self):
        if self.item==0:
            return 'Queue is empty'
        return self.item[0]
    def rear(self):
        if self.item==0:
            return 'Queue is empty'
        return self.item[-1]
    def size(self):
        return len(self.item)
q=Queue()
q.push(10)  
q.push(20)
q.push(30)
q.pop()
q.is_empty()
print(q.peek())

print(q.rear())
print(q.size())