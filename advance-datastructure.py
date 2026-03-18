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

