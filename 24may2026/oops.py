#The self parameter is a reference to the current instance of the class.
#It is used to access properties and methods that belong to the class.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()



