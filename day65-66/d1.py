#decorators with parameters
def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a,b):
    return a+b
print("The result is : ", add(23,9))
@decorator_name
def sub(a,b):
    return a-b
print("The result of subtraction:" ,sub(23,9))
@decorator_name
def mul(a,b) :
    return a*b
print("the result of multiplication is :", mul(23,9))
@decorator_name
def div(a,b):
    return a/b



