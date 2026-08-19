#creating a function
def my_function():
  print("Hello from a function")

#calling a function
my_function()
#can call multiple times
my_function()
my_function()
my_function()
my_function()


"""
Function Names
Function names follow the same rules as variable names in Python:

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)

Functions help in code reusability


#without fns


temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

"""

#with fns
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77)) #25.0
print(fahrenheit_to_celsius(95)) #35.0
print(fahrenheit_to_celsius(50)) #10.0


def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)