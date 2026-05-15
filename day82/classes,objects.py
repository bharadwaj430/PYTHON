#python classes and objects
#python is oop
"""
everything in object is python , with properties and methods
class = obj constructor
as it is blueprint for creating objects 
"""
#create a class keyword
#ex: 
class MyClass:
  x=5

#CREATE object
#we use class name to create objects

#we  an obj object1 and print x
object1 = MyClass()
print(object1.x)

#DELETE  objects
#we use del keyword
#ex: 
del object1

#MULTIPLE OBJECTS
#we create multiple objects in same class

"""
creating simple objects from MyClass class:
"""
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print(obj1.x)
print(obj2.x)
print(obj3.x)

#note:
#each object is independent and has own copy of class properties


