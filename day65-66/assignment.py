"""write a decorator to implement square of a number 
which was acquired by the 2 func add() & sub() 
these are outer functions
"""
# The deco fn
def square_deco(func):
    def wrapper(*args, **kwargs):
        # Call the origin fn (add and sub)
        result = func(*args, **kwargs)
        # Return square numbers
        return result ** 2
    return wrapper

# Applying the decorator to the outer functions
@square_deco
def add(a, b):
    return a + b

@square_deco
def sub(a, b):
    return a - b

#f string printing
print(f"Square of add(3, 4): {add(3, 4)}")  
print(f"Square of sub(10, 5): {sub(10, 5)}")


