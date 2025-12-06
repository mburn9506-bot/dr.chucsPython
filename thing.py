# def thing ():
#         print('hello')
#         print('fun')
        
# thing()
# print(1 + 2 *float(3) / 4-5)
# -2.5
# ===================
# eval = '123'
# type(eval)

# print(eval+1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# ival = int(eval)
# type(ival)

# print(ival+1)#output:-2.5 and 124
# ================
def greet(lang):
        if lang == 'es':
                print ('hello')
        elif lang=='fr':
                print('french')
        else:
                print('hello')
greet('es')
greet('fr')
greet('en')

def greet1 ():
        return "hello"
print(greet1(),"rita")
print(greet1(), "josephine")
"""python3 
Python 3.12.9 (v3.12.9:fdb81425a9a, Feb  4 2025, 12:21:36) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> def greet(lang):
...     if lang == 'es':
...         return 'hola'
...     elif lang == 'fr':
...         return 'bonjour'
...     else:  
...         return 'hallo'
... 
>>> print(greet('es'),'rita')
hola rita
>>> print(greet('fr'),'josephine')
bonjour josephine
>>> print(greet('en'),'michel')
hallo michel
>>> """
def addtwo(a,b):
        added = a + b
        return added
x = addtwo(3,5)
print(x)

"""Python 3.12.9 (v3.12.9:fdb81425a9a, Feb  4 2025, 12:21:36) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> def addtwo(3,5):
  File "<stdin>", line 1
    def addtwo(3,5):
               ^
SyntaxError: invalid syntax
>>> def addtwo(a,b):
...     added = a + b
...     return added after declaring 
the function here press enter 
to finish then add the rest of code
... 
>>> x =addtwo(3,5)
>>> print(x)
8"""
