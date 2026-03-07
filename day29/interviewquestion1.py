"""
How are strings immutable in Python, and what does that mean?

Strings in Python are immutable, which means once a string is created, it cannot be changed.
 Any operation that seems to modify a string will actually create a new string object in memory instead of altering the original string.

Immutability means the content of the object cannot be altered after it’s created.
For strings, this implies that individual characters in the string or the entire string cannot be modified in place.

"""
# Example of string immutability
original_string = "Hello, World!" 

# Attempting to change a character in the string (this will not work)
# original_string[0] = 'h'  # This will raise a TypeError

s = "hello"
s = s + " world"
print(s)  # Output: "hello world"



