"""
a function is a block of code which only runs when it called
a fn can return data as result
a function helps avoiding code repetition
"""
#creating a function
def  my_fn():
  print("Hello from a function")

# calling a function
my_fn()
#calling multiple times
my_fn() #Hello from a function
my_fn()#Hello from a function
my_fn()#Hello from a function
my_fn() #Hello from a function
my_fn()#Hello from a function
my_fn()#Hello from a function



"""
function names
1. must start with letter or underscore
2.should contain only letters,numbers, and underscores
function names are case-sensitive(myfn and Myfn are different)

some valid fns names are:
calculate_sum()
_private_function()
myFunction2()


"""
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit -32)*5/9

print(fahrenheit_to_celsius(77)) ##25.0
print(fahrenheit_to_celsius(95)) #35.0
print(fahrenheit_to_celsius(50)) #10.0

"""
Return values
Functions can send data back to the code that called them using the return statement.

When a function reaches a return statement, it stops executing and sends the result back:

"""

def give_a_greeting():
  return "hello from a function"
message = give_a_greeting()
print(message) #hello from a function


"""
THE PASS STATEMENT
Function definitions cannot be empty. If you need to create a function placeholder without any code,
 use the pass statement:
"""
def my_function():
  pass    #returns nothing


"""
PYTHON FUNCTION ARGUMENTS




Arguments are specified after the function name, inside the parentheses.
 You can add as many arguments as you want, 
just separate them with a comma.




"""
def my_function(fname):
  print(fname + " PUBLIC SCHOOL")

my_function("hyderabad") #hyderabad PUBLIC SCHOOL
my_function("delhi")     #delhi PUBLIC SCHOOL
my_function("secunderabad") #secunderabad PUBLIC SCHOOL



"""
parameter vs arguments
A parameter  is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.

"""

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("bharath") # "bharath" is an argument   #Hello bharath



"""
By default, a function must be called with the correct number of arguments.

If your function expects 2 arguments, you must call it with exactly 2 arguments.

"""
def my_function(first_name, last_name):
  print(first_name + " " + last_name)

my_function("bharadwaj", "Marri") #bharadwaj Marri


"""
default parameter values

You can assign default values to parameters. 
If the function is called without an argument, it uses the default value:
"""

def my_function(name = "friend"):
  print("Hello", name)

my_function("mohan")
my_function("chaitanya")
my_function()
my_function("saheel")
"""
output:
Hello mohan
Hello chaitanya
Hello friend
Hello saheel

"""
"""

keyword arguments

You can send arguments with the key = value syntax.

"""
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")




















