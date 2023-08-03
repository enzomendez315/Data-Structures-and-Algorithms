"""
Implementation for a queue.
"""

# Initialize a queue
queue_1 = []

# Enqueue elements
queue_1.append('a')
queue_1.append('b')
queue_1.append('c')

print(queue_1)

# Dequeue. FIFO order
print(queue_1.pop(0))
print(queue_1.pop(0))
print(queue_1.pop(0))


"""
Another implementation using the queue module.
"""
from queue import Queue

# Initialize a queue
queue_2 = Queue()

# Enqueue elements
queue_2.put('x')
queue_2.put('y')
queue_2.put('z')

# Dequeue. FIFO order
print(queue_2.get())
print(queue_2.get())
print(queue_2.get())