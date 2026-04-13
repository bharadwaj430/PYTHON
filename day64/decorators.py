"""
decorators.py
A decorator in Python is a powerful tool that
 allows you to add extra behavior to 
 an existing function or method without 
 changing its actual code. 

usecase: 
many functions are there to avoid time constraint wastage
 we add one decorator
 to solve all the runnable runtime programs
 
 logging : tracking when fn is called
 auth/authorization: checking user is logged in before fn
 timing :measuring how long fn take
 caching: storing results of slow fn to take time
 """

# Applying the decorator to a function
def greet():
    print("Hello, World!")
greet()
#we use *args and *kwargs so our wrapper can accept
#  any number of arguments
"""
decorator syntax is shorthand for greet = decorator(greet)
"""
