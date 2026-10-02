"""
a fn is a 
1.block of code which only runs when it called
2.fn can return data as result
3.avoids code repetition

"""
def my_function():
  print("Hello from a function")

my_function() #calling a fn

"""
fn name rules
can start with letter or _
can contains letters,nos,underscores
are case sensitive

some valid fns are
calculate_sum()
_private_function()
myFunction2()



use of fns
to avoid code repetition



#return values
Functions can send data back to the code that called them using the return statement.
"""
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#or

#return val directly

def get_greeting():
  return "Hello from a function"

print(get_greeting())


"""
THE PASS STATEMENT
Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:


The pass statement is often used when developing, allowing you to define the structure first and implement details later.


"""
def my_function():
  pass
