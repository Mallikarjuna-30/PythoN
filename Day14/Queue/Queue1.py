#<----- QUEUE ----->#
# FIFO => First In First Out

q = []
q.append(10)
q.append(20)
q.append(30)

print(q)
q.pop(0)
print(q)

# Using collections.deque
from collections import deque
queue = deque()
queue.append(30)
queue.append(40)
queue.append(50)
print(queue)
queue.popleft()
print(queue)

