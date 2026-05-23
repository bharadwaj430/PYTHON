"""
oops in python
to map with real world scenarios,
we started using objects in code
called object oriented programming.

fns reduce redundancy
increase reusability
more than functional - object oriented programming"""


#multiple parameters

class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)


"""
Linus
30
Oslo
Norway



"""
