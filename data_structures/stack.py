"""
Implementation for a stack.
"""

# Initialize a stack
stack = []

# Push elements in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

# LIFO order
print(stack.pop())
print(stack.pop())
print(stack.pop())