#Functions are reusable pieces of code that run when you call them. 
# Many programming languages come with built-in functions that make it easier to get started.
#  Python is no exception
#Another helpful built-in function is" input()"

name = input('What is your name?')  #user POV : "Bharadwaj" and enter

"""
int() converts number,boolean and numeric string into a integer
"""
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 

#custom function

def function():
  b = "bharadwaj"
  print( 'i am happy:' , b) #function's body

def hello():
  print('Hello World')
hello() #hello world


# Python relies on indentation to determine which groups of statements belong together.
#  These groups of statements are called "code blocks".

#output:
"""
What is your name?bharadwajmarri
3
42
1
0
Hello World
"""