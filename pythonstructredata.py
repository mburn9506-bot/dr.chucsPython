


numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)#[1,2,3,4,5]

coordinates = (10, 20)
print(coordinates[0])#10
#set
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)#{1, 2, 3, 4}
#dict
student = {
    "name": "Ali",
    "age": 15,
    "grade": "10th"
}
print(student["name"])#Ali
#string
text = "Hello Python"
print(text.upper())#HELLO PYTHON
#stack
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.pop()
print(stack)#[10, 20] delete last element
#queue
from collections import deque
queue = deque()
"""What is deque?

deque stands for Double-Ended Queue.
It is a data structure from the collections
 module that allows 
fast insertion and deletion from both ends."""
queue.append(1)
queue.append(2)
queue.popleft()#What is popleft()?
# popleft() is a method used with a queue implemented using collections.deque.
# It removes and returns the first (leftmost) element of the queue.
# print(queue)
print(queue)#deque([2])

#nested data
students = [
    {"name": "Ali", "age": 14},
    {"name": "Sara", "age": 15}
]
print(students[1])
#===========
student = {
    "name": "Ali",
    "age": 15,
    "grade": "10th"
}
print(student["name"])
print(list(student.items()))
print(tuple(student.items()))
