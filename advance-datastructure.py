# advanced data structures in python

# Stack: folloes the Last In First Out (LIFO) principle, implemented using list
stack = []
stack.append("test1") # adding an element to the top of the stack
stack.append("test2")
stack.append("test3")
print(stack)

stack.pop()  # removing the top element of the stack
print(stack)
print(stack.pop())

#queue
from collections import deque
queue = deque()

queue.append("Customer1")
queue.append("Customer2")
queue.append("Customer3")

print("Queue:", queue)

served = queue.popleft()

print("Served:", served)
print("Remaining:", queue)


#queue practise
from collections import deque

orders = deque()

orders.append("Pizza")
orders.append("Burger")
orders.append("Momo")

print("Orders:", orders)

served = orders.popleft()

print("Served:", served)

print("Remaining Orders:", orders)


