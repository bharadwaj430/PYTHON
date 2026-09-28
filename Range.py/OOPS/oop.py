class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

"""
self in init method is used
to store data inside a particular object
"""


#INHERITANCE
"""
INHERITANCE allows us to define a class that inherits all the methods and properties from another class.

parent class ---base class
child class -- derived class

"""
def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("bharadwaj", "marri")
print(x)



#POLYMORPHISM
"""
polymorphism --- many forms
mthds/fns/operators with same name can be executed on many objs or classes

functional polymorphism
len()----returns number


class polymorphism
multiple classes with same method name
"""

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")


class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("suzuki", "volkswagen")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("air india", "british airways")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()




