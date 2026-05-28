# advanced data structures in python

# Stack: folloes the Last In First Out (LIFO) principle, implemented using list
print("-----Stack-----")
stack = []
stack.append("test1") # adding an element to the top of the stack
stack.append("test2")
stack.append("test3")
print(stack)

stack.pop()  # removing the top element of the stack
print(stack)
print(stack.pop())



#queue
print("-----Queue-----")
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



#linkedlist
print("-----Linkedlist-----")
class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList:
   def __init__(self):
       self.head = None

   def add_song(self, song):
       new_node = Node(song)

       if not self.head:
           self.head = new_node
           return

       temp = self.head
       while temp.next:
           temp = temp.next

       temp.next = new_node

   def show_playlist(self):
       temp = self.head
       while temp:
           print(temp.data)
           temp = temp.next


playlist = LinkedList()

playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

playlist.show_playlist()


#Heap
print("-----Heap-----")
import heapq

patients = []

heapq.heappush(patients, (2, "Patient B"))
heapq.heappush(patients, (1, "Patient A"))
heapq.heappush(patients, (3, "Patient C"))

print("Next Patient:", heapq.heappop(patients))

#Heap practise 
print("\n")
tasks =[]
heapq.heappush(tasks, (3, "Task 3 : watch movie"))
heapq.heappush(tasks, (1, "Task 1 : Fix bug"))
heapq.heappush(tasks, (2, "Task 2 : Complete assignment"))

print("Next Task: ", heapq.heappop(tasks) )

#practise set 
print("\n------Resume Skill Checker------")

skills = ["python", "java", "aws"]
resume = input("Enter resume text: ")

for skill in skills:
    if skill in resume.lower():
        print(skill, "found in resume")
    else:  
        print(skill, "not found in resume")


print("\n------Student Record System------")
student = {}

student["name"] = input("Enter name: ")
student["age"] = input("Enter age: ")
student["course"] = input("Enter course: ")

print(student)

print("\n------Simple Contact Book------")
contacts = {}

name = input("Enter name: ")
number = input("Enter number: ")

contacts[name] = number

print(contacts)

print("\n------Expense Tracker------")
expenses = []

for i in range(3):
   amount = int(input("Enter expense: "))
   expenses.append(amount)
print("Expenses:", expenses)






