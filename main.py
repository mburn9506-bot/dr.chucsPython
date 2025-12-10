# amodule is like your drawer
# keeps functions and variable organized for reuse
import mod
mod.say_hi()
from mod import add_nums,my_variable
print(add_nums(5,3))
print(my_variable)

import mod as mm
mm.say_hi()

import math
print(math.sqrt(16))
print(math.pi)

# import specific from math like sine and cosine
from math import sin, cos
print(sin(math.pi/2))

from mod import square, cube, my_constant, power
print(square(4))
print(cube(3))
print(my_constant)
print(power(2,3))