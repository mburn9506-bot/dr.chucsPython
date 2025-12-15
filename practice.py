# https://youtu.be/PszWLQEHjLI?t=10380
for _ in range(2):
        print("rita josephine")
#output:
# rita josephine
# rita josephine

l = [[1,2,3],[4,5,6],[7,8,9]]
for x, _, z in l:
        print(x, z)

for index in range(0, 10, 2):#(start index,end index, step)
      print(index)  
"""
output:
0
2
4
6
8
"""
names = ['rita','josephine','michel']
ages = [28,26,65]
for names,ages in zip(names,ages):
     print(f"name is {names} is age {ages}")  
"""name is rita is age 28
name is josephine is age 26
name is michel is age 65"""
d = {x: x **2 for  x in range(5)}
print(type(d),d)
#<class 'dict'> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}