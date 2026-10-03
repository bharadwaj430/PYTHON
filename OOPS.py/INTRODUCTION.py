
#python is object oriented programming language
"""

INIT CONSTRUCTOR
python __init__method
__init__-------------built in methods for classes
# It runs automatically when an object is created.
# It is commonly used to initialize object data.

#CLASS----Class = Blueprint
#OBJECT-----Object = Real thing created from the blueprint

# self represents the current object.
# It allows each object to have its own data.

# A method is a function defined inside a class.
# Methods usually describe what an object can DO.


#four types in OOP
1.ENCAPSULATION
2.INHERITANCE
3.POLYMORPHISM



1.encapsulation---protects data inside a class

two imp methods
getter method--can accesss private property
setter method--can change/modify the private property

"""


class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Ram")
student.set_grade(85)
print(student.get_grade()) #85
print(student.get_status()) #Passed


"""
polymorphism --- many forms
diff classes have mthds/fns/operators  with same name
"""
class Dog:

    def sound(self):
        print("Dog says Woof")


class Cat:

    def sound(self):
        print("Cat says Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()



"""
inheritance--allows one class to reuse prop and mthds of another cls



# Inheritance allows one class to reuse
# properties and methods of another class.
"""

#Parent class
class Animal:

    def eat(self):
        print("Animal is eating")


# Child class
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()    # Inherited from Animal
dog.bark()   # Dog's own method


"""
# Abstraction means hiding unnecessary implementation details
# and exposing only what the user needs.

"""
# Abstraction example
# We use a simple method to hide the internal details.

class ATM:

    def withdraw_money(self, amount):
        # Internal process is hidden from the user
        self.check_bal()
        self.process_transaction()
        print(f"₹{amount} withdrawn successfully")

    def check_bal(self):
        print("Checking balance...") 

    def process_transaction(self):
        print("Processing transaction...")


# User only needs to call this
atm = ATM()

atm.withdraw_money(500)




