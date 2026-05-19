from collections import deque

q= deque()

q.append(20)
q.appendleft(10)
q.appendleft(39)
q.popleft()
q.pop()
q.append(1000)
print(q)