#Python __init__() Method
"""
all classes have built in method called ___init__()
always executed when class being inititated
"""
#__init__ method used to assign values to objects properties
#perform operations when object is created
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
#note : init method is called automatically every time the class is 
# being used to create a new object

#ex:


#default values in __init__()
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

#example:
"""
Emil
36
Emil 18
Tobias 25
"""
