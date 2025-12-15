# https://youtu.be/PszWLQEHjLI?t=10067
s = 'python'
# for index, element in enumerate(s):#for index in range(len(s)) # for element in s
#         print(f"index = {index}, element = {element}")

l = ['a','b','c','d']
for index, element in enumerate(l[3:], start =3):
        print(f"index = {index}, element = {element}")
#=============================================
l = ['a','b','c','d']
for index, element in enumerate(l, start =3):
        print(f"index = {index}, element = {element}")
# output:
"""
indes = 3, element = d
==================
indes = 3, element = a
indes = 4, element = b
indes = 5, element = c
indes = 6, element = d
"""
#https://youtu.be/PszWLQEHjLI?t=10284
d = {'a':1,'b':2,'c':3}
for index, (key, value) in enumerate(d.items()):
        print(f"index = {index}, key = {key}, value = {value}")
"""
index = 0, key = a, value = 1
index = 1, key = b, value = 2
index = 2, key = c, value = 3
"""