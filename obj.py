# class PartyAnimal:
#         def __init__(self) :
#                self.x = 0

#         def party(self):
#                 self.x = self.x +1
#                 print('so far',self.x)
# an = PartyAnimal()
# an.party()
# an.party()
# an.party()
# print("---------------------")
# print("type: ",type(an))
# print("---------------------")
# print("dir: ",dir(an))
# print("---------------------")
# print("type: ",type(an.x))
# print("---------------------")
# print("type: ",type(an.party))
# https://youtu.be/cBgtQK6vhN4?t=202
"""so far 1
so far 2
so far 3
---------------------
type:  <class '__main__.PartyAnimal'>
---------------------
dir:  ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'party', 'x']
---------------------
type:  <class 'int'>
---------------------
type:  <class 'method'>"""
#=============================================
# class PartyAnimal:
#         def __init__(self) :
#                self.x = 0
#                print('i am construted')

#         def party(self):
#                 self.x = self.x +1
#                 print('so far',self.x)

#         def __del__(self):
#                 print('i am destructured',self.x)
# an = PartyAnimal()
# an.party()
# an.party()
# an =42
# print('an contains',an)
"""
i am construted
so far 1
so far 2
i am destructured 2
an contains 42
"""
#==============================
# class PartyAnimal:
#         def __init__(self,z) :
#                self.x = 0
#                self.name = z
#                print(self.name,"constructed")

#         def party(self):
#                 self.x = self.x +1
#                 print(self.name,"party count",self.x)

# s = PartyAnimal("sally")
# s.party()
# j = PartyAnimal("jim")

# j.party()
# s.party()
"""
sally constructed
sally party count 1
jim constructed
jim party count 1
sally party count 2
"""
# ======= inheritance ==========
# https://youtu.be/cOf7g_E2G8g?t=36
class PartyAnimal:
        def __init__(self,nam) :
               self.x = 0
               self.name = nam
               print(self.name,"constructed")

        def party(self):
                self.x = self.x +1
                print(self.name,"party count",self.x)

class FootBallFan(PartyAnimal):
        def __init__(self, nam):
                super().__init__(nam)
                self.points = 0
        def touchdown(self):
                self.points = self.points + 7
                self.party()
                print(self.name,"points",self.points)
        s = PartyAnimal("rita")
        s.party()


j = FootBallFan("josephine")
j.party()
j.touchdown()
"""printout :rita constructed
rita party count 1
josephine constructed
josephine party count 1
josephine party count 2
josephine points 7"""
