#scope is a point at which you can access variable
#CONTROLS LIFEtime of a variable

#python LEGB rule
"""
usecase
to resolve  the scope of variables in program




"""

#Local scope (L):  a variable declared inside a function or class can only be accessed within that fn or cls
#local scope code example
def my_func(): #my_func() has own scope can't be accessed outside the fn
    my_var = 10
    print(my_var)   #10
#printing my_var outside the fn -> NameeError

def my_func():
    my_var = 10 #locally scoped to my_func
    print(my_var)
 
"""
Enclosing scope means that a function that's nested inside another function
can access the variables of the function it's nested within
"""
#enclosing scope example:
def outer_func():
    msg = 'hi this is bharadwaj!'
    def inner_func():
        print(msg)
    inner_func()
outer_func() #hi this is bharadwaj