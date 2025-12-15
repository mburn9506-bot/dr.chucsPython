# https://youtu.be/PszWLQEHjLI?t=10067
#enumerate() in Python (simple explanation)

# enumerate() is used to loop over a list
#  (or any iterable) and get both the index 
# and the value at the same time.
#====== code enumerate   ====
# fruits = ["apple", "banana", "cherry"]

# for index, fruit in enumerate(fruits):
#     print(index, fruit)
""""
output:
0 apple
1 banana
2 cherry
"""
#======start counting from a different number ===========
# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)
#========= old way ===========
# for i in range(len(fruits)):
#     print(i, fruits[i])
#=======better way ========
# fruits = ["apple", "banana", "cherry"]
# for i, fruit in enumerate(fruits):
#     print(i, fruit)
"""
output:
0 apple
1 banana
2 cherry
"""
#======== example in CRUD =====
# students = ["Ali", "Sara", "John"]

# for i, student in enumerate(students, start=1):
#     print(f"{i}. {student}")
#output:
# 1. Ali
# 2. Sara
# 3. John
#============= work with string ==============
# word ="python"
# for i, ch in enumerate(word):
#     print(i, ch)
# output:
# 0 p
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n
# ========Basic list of dictionaries==========
students = [
    {"name": "Ali", "age": 15, "grade": "A"},
    {"name": "Sara", "age": 16, "grade": "B"},
    {"name": "John", "age": 15, "grade": "A+"}
]

# for index, student in enumerate(students, start=1):
#     print(index, student)
#output:
# 1 {'name': 'Ali', 'age': 15, 'grade': 'A'}
# 2 {'name': 'Sara', 'age': 16, 'grade': 'B'}
# 3 {'name': 'John', 'age': 15, 'grade': 'A+'}
#====== access dictionary values =======
# for i, student in enumerate(students, start=1):
#     print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
#output:
# 1. Name: Ali, Age: 15, Grade: A
# 2. Name: Sara, Age: 16, Grade: B
# 3. Name: John, Age: 15, Grade: A+
#======= update item using enumerate =====

for i, student in enumerate(students):
    if student["name"] == "Sara":
        students[i]["grade"] = "A+"
print(students)

# [{'name': 'Ali', 'age': 15, 'grade': 'A'},
#  {'name': 'Sara', 'age': 16, 'grade': 'A+'},
#  {'name': 'John', 'age': 15, 'grade': 'A+'}]
# ===================
name_to_delete = "Ali"

students = [
    student
    for i, student in enumerate(students)
    if student["name"] != name_to_delete
]
print(students)
#output:
#[{'name': 'Sara', 'age': 16, 'grade': 'A'},
#  {'name': 'John', 'age': 15, 'grade': 'A+'}]
#========= display students with numbering ====
# def display_students():
#     if not students:
#         print("No students found")
#         return

#     for i, student in enumerate(students, start=1):
#         print(f"{i}. {student['name']} | Age: {student['age']} | Grade: {student['grade']}")

# display_students()
#output:
#1. Sara | Age: 16 | Grade: A+
# 2. John | Age: 15 | Grade: A+
# ============== 
import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for index, row in enumerate(reader, start=1):
        print(index, row)
"""
output
1 {'name': 'Ali', 'age': '15', 'grade': 'A'}
2 {'name': 'Sara', 'age': '16', 'grade': 'B'}
3 {'name': 'John', 'age': '15', 'grade': 'A+'}
"""
#=============================
# with open("students.csv", "r", newline="") as file:
#     reader = csv.DictReader(file)

#     for i, row in enumerate(reader, start=1):
#         print(f"{i}. Name: {row['name']} | Age: {row['age']} | Grade: {row['grade']}")

"""
1. Name: Ali | Age: 15 | Grade: A
2. Name: Sara | Age: 16 | Grade: B
3. Name: John | Age: 15 | Grade: A+
"""
#====find and update row ====

# import csv

# students = []

# Read
# with open("students.csv", "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append(row)

# Update (using enumerate)
# for i, student in enumerate(students):
#     if student["name"] == "Sara":
#         students[i]["grade"] = "A"

# Write back
# with open("students.csv", "w", newline="") as file:
#     fieldnames = ["name", "age", "grade"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(students)
#======= delete row ======
# name_to_delete = "Ali"

# students = [
#     student
#     for i, student in enumerate(students)
#     if student["name"] != name_to_delete
# ]
# print(students)
"""
[{'name': 'Sara', 'age': '16', 'grade': 'A'}, 
{'name': 'John', 'age': '15', 'grade': 'A+'}]
"""
#===crud style from csv =======

def display_students():
    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, start=1):
            print(f"{i}. {row['name']} ({row['age']}) - {row['grade']}")

display_students()
"""
1. Ali (15) - A
2. Sara (16) - A
3. John (15) - A+
"""
"""


You said:
python enumerate
ChatGPT said:
enumerate() in Python (simple explanation)
enumerate() is used to loop over a list (or any iterable) and get both the index and the value at the same time.

Basic example
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
Output

0 apple
1 banana
2 cherry
Start counting from a different number
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
Output

1 apple
2 banana
3 cherry
Why use enumerate() instead of range(len())?
❌ Old way:

for i in range(len(fruits)):
    print(i, fruits[i])
✅ Better way:

for i, fruit in enumerate(fruits):
    print(i, fruit)
✔ Cleaner
✔ Less error-prone
✔ More Pythonic

Example with your CRUD-style learning
students = ["Ali", "Sara", "John"]

for i, student in enumerate(students, start=1):
    print(f"{i}. {student}")
Output

1. Ali
2. Sara
3. John
Works with strings too
word = "Python"

for i, ch in enumerate(word):
    print(i, ch)
If you want, I can show:

enumerate() with lists of dictionaries

enumerate() in file handling

A real CRUD example

Just tell me 👍

You said:
enumerate() with lists of dictionaries
ChatGPT said:
enumerate() with lists of dictionaries (clear examples)
This is very common in CRUD projects 👍

Example 1: Basic list of dictionaries
students = [
    {"name": "Ali", "age": 15, "grade": "A"},
    {"name": "Sara", "age": 16, "grade": "B"},
    {"name": "John", "age": 15, "grade": "A+"}
]

for index, student in enumerate(students, start=1):
    print(index, student)
Output

1 {'name': 'Ali', 'age': 15, 'grade': 'A'}
2 {'name': 'Sara', 'age': 16, 'grade': 'B'}
3 {'name': 'John', 'age': 15, 'grade': 'A+'}
Example 2: Access dictionary values
for i, student in enumerate(students, start=1):
    print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
Example 3: Update an item using enumerate()
for i, student in enumerate(students):
    if student["name"] == "Sara":
        students[i]["grade"] = "A"
Example 4: Delete an item (important ⚠️)
name_to_delete = "Ali"

students = [
    student
    for i, student in enumerate(students)
    if student["name"] != name_to_delete
]
✔ Safe way to delete
✔ No index errors

Example 5: Display students with numbering (CRUD-style)
def display_students():
    if not students:
        print("No students found")
        return

    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} | Age: {student['age']} | Grade: {student['grade']}")

display_students()
When to use enumerate() with dictionaries
Use it when you need:

The position (index) of the dictionary

AND the dictionary data itself

Perfect for:

Update

Delete

Display numbering

Menu-based programs

If you want next:

enumerate() + CSV file

enumerate() + JSON

Full CRUD project example

Just tell me 🚀

You said:
enumerate() + CSV file
ChatGPT said:
enumerate() + CSV file (easy & practical example)
This fits perfectly with your CRUD + file-handling learning 👍

1️⃣ Sample CSV file (students.csv)
name,age,grade
Ali,15,A
Sara,16,B
John,15,A+
2️⃣ Read CSV and use enumerate()
import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for index, row in enumerate(reader, start=1):
        print(index, row)
Output

1 {'name': 'Ali', 'age': '15', 'grade': 'A'}
2 {'name': 'Sara', 'age': '16', 'grade': 'B'}
3 {'name': 'John', 'age': '15', 'grade': 'A+'}
3️⃣ Display nicely (recommended)
with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for i, row in enumerate(reader, start=1):
        print(f"{i}. Name: {row['name']} | Age: {row['age']} | Grade: {row['grade']}")
4️⃣ Find & update a row using enumerate()
CSV files can’t be edited directly → read → modify → write back

import csv

students = []

# Read
with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

# Update (using enumerate)
for i, student in enumerate(students):
    if student["name"] == "Sara":
        students[i]["grade"] = "A"

# Write back
with open("students.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
5️⃣ Delete a row using enumerate()
name_to_delete = "Ali"

students = [
    student
    for i, student in enumerate(students)
    if student["name"] != name_to_delete
]
6️⃣ CRUD-style display from CSV
def display_students():
    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, start=1):
            print(f"{i}. {row['name']} ({row['age']}) - {row['grade']}")

display_students()
Key takeaway 🧠
enumerate() gives you row number + row data

Perfect for:

Numbered display

Update by index

Delete by index

CRUD menus

If you want next:

Full CRUD project with CSV

Select row by number (1, 2, 3…)

Convert CSV → list of dictionaries
"""






