import os


f = open("demo.txt", "w")
f.write("Hello! This is my first file.\n")
f.write("Python is awesome!")

f = open("demo.txt", "r")
content = f.read()
print(content)
"""output:
Hello! This is my first file.
Python is awesome!
"""
if os.path.exists("demo.txt"):
    print("The file exists!")
else:
    print("File not found!")
    """ output:
Hello! This is my first file.
Python is awesome!
The file exists!
"""

f.close()