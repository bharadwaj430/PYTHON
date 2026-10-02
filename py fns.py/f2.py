"""
f2

functional arguments:Information can be passed into functions as arguments.
"""

def my_fn(fname):
  print(fname + " sharma ")
my_fn("rohit")
my_fn("anushka")
my_fn("mohan")
"""
output:
rohit sharma 
anushka sharma 
mohan sharma 
"""



"""
parameter vs arguments
A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.
"""

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("bharat") # "bharat" is an argument


#default parameter values
def my_function(name = "friend"):
  print("Hello", name)

my_function("mohit")
my_function("yuvatej")
my_function()
my_function("vardhan")
"""
output:
Hello mohit
Hello yuvatej
Hello friend
Hello vardhan
"""

#keyword arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "cat", name = "Micky")


#positional arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")



