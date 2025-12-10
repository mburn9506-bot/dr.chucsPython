#to import <module name> import <method1, method2,.....,,methodn>
# syntax example: from math import sqrt,pow,pi
# this will import multiple functions (square, power, and Pi)
# of math modulein a program
# example:
# from math import sqrt, pow, pi
# print(sqrt(625))
# print(round(pi, 2))
# print(pow(3,3))
# """
# 25.0
# 3.14
# 27.0
# """
#-----------------------------------
# to import all methods from a module
#from module name import*
# from math import * #this will import will all the constants and function methods of math module
# print (pi)
# print (factorial(5))
# print (sqrt(225))
#----------------------------------
# import statement is the simplest and the most common way to use modules in our ConnectionRefusedError
#for example "import math"
#on executingthis statment python will perform these operations:
        #* search for the file "math.py"
        #* create space where modules definition and variable will be created
        #* execute the statemments in module
# import statement does not directly import the functions and constants in the program
# to access /use any of the functions present in the imported module
# followed by the name of the function seperated by a dot (also known as period) this format is called dot notation
# example:
# import math
# result = math.sqrt(144)
# print (result)
#output:12
# ======== retrieving objects from a module ========
# there is another function dir() which ,when applied to a module gives you the names of all that is defined inside the module
#example:
# import area
# print(dir(area))
#output:

# ['WGS84_RADIUS', '__builtins__', '__cached__', 
# '__doc__', '__file__', '__loader__', '__name__', 
# '__package__', '__path__', '__spec__', '__version__',
#  'area', 'division', 'json', 'pi', 'polygon__area',
#  'rad', 'ring__area', 'sin']
#---------------------------------------------
#import test
# import the module "test" and creates a reference to that module

#in the current calling program(or namespace)
# after executing this statement you can use test.name to refer to the objects define in module test
# import test1, test2, test3
# this statement shall import three modules namely test1 test2 test3 in current namespace
# as  a result all the definitions of these modules are available and can be used as :
# <module_name>,<name>
# <sub_module/any object>
# from test import *
# when you use import* statement, it shall import all the sub-modules or objects defined in the module "test"
# into the current namespace so after executing this statement 
# you are required to simply give the name of the object to be referred to
# definedin the module test 
# 
# in other words <name> would nowbe used as name only,without specifying modules's name 
#(i.e test.name ) is not required to be given if name was already defined it is replaced by 
#new version, the one impoted from the module
# import math as m
#using the alias to access functions from the math module
# if the mame of the module is long
# print(m.sqrt(25))
# print(m.pi)
# # from module_name import item_name as alias
# from math import sqrt as square_root
# print(square_root(16))
# https://youtu.be/inpPKwxKq0Y?t=27192
# https://youtu.be/inpPKwxKq0Y?t=24102

# ====== create dictionary from nested list =======
# nested_list = [["subject","math"],["student",30],["teacher","ritajose"],["room","b205"]]
# my_dict = dict(nested_list)
# print(my_dict)
#output:{'subject': 'math', 'student': 30, 'teacher': 'ritajose', 'room': 'b205'}
#===========================================
# to add an item to the dictionary we can use square[] and initializing dictionary value
# my_dict = {}
# my_dict['fruit']="apple" 
# my_dict["color"]="red"
# my_dict["quantity"]=5
# print(my_dict)
# output:{'fruit': 'apple', 'color': 'red', 'quantity': 5}
# ========= to access element in dictionary you can use square brackets []======
# my_dict = {"name":"nancy",'age':12,'city':"new york"}
# print(my_dict['name'])
# print(my_dict['age'])
# print(my_dict['city'])
#====== iterating over keys using a for loop: =======
my_dict = {'name':"nancy",'age':12,'city':'newyork'}
for key in my_dict:
        value = my_dict[key]
        print(key, ':',value)
# https://youtu.be/inpPKwxKq0Y?t=24244



