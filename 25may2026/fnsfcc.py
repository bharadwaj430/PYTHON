#fns are reusable pieces of code that run when you call them
"""
prog lang come with built in fns that are easier to get started
py is no exception 

#input built in fns - input()
"""
#program 1
name = input('What is your name?')
print('Hello', name) 

#output program 1
"""
What is your name? bharadwaj      
Hello bharadwaj 
"""

#int()- converts a no , boolean and num string into integer
#program 2
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 

#program 2 output 
def hello():
    print('Hello World')
def calculate_sum(a,b): #a and b are parameters which are placeholder variables that acts as slots for values we pass into fns
    print(a+b)


"""
to use parameters we need to pass in arguments
arguments are the values you pass to a function 
when we don't use return py returns none by default  
"""
#program 3 
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None








 