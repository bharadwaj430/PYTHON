# 1. Basic Function (No parameters, no return)
def greet():
    """Prints a simple greeting."""
    print("Hello! Welcome to Python.")


# 2. Function with Parameters (Takes inputs)
def greet_user(name):
    """Greets a specific user by name."""
    print(f"Hello, {name}!")


# 3. Function with a Return Value (Sends data back)
def square(number):
    """Calculates and returns the square of a number."""
    return number * number


# 4. Function with Default Parameters (Optional inputs)
def power(base, exponent=2):
    """Raises a base to an exponent. Defaults to squaring."""
    return base**exponent


# 5. Function Returning Multiple Values (Returns a tuple)
def get_min_max(numbers):
    """Finds both the lowest and highest values in a list."""
    lowest = min(numbers)
    highest = max(numbers)
    return lowest, highest


# =====================================================================
# FUNCTION CALLS (Executing the code above)
# =====================================================================

# Calling a basic function
greet()

# Passing an argument to a function
greet_user("Alice")

# Saving a returned value into a variable
result = square(5)
print(f"The square of 5 is: {result}")

# Using default values vs overriding them
print(f"Default exponent (3^2): {power(3)}")
print(f"Custom exponent (3^3): {power(3, 3)}")

# Unpacking multiple returned values
my_list = [4, 1, 8, 2, 9]
low, high = get_min_max(my_list)
print(f"Lowest: {low}, Highest: {high}")
