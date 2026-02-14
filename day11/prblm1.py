#py program to print a number
x = 10
print(x)
#py program for global variable
x = 10
def func():
    print(x)  
func()
#py program for global keyword
x = "awesome"
def myfunc():
    global x
    x = "amazing"
myfunc()
print("Python is " + x)


"""
Output:
10
10
Python is amazing
"""
