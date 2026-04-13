#decorators with parameters
def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper
""""
#decorator name
def add(a,b):
    return a+b
print("The result is : ", add(23,9))
"""



