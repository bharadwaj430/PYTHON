# Creating a tuple
fruits = ("apple", "banana", "mango", "banana")

# Printing the tuple
print("Tuple:", fruits)

# Accessing elements
print("First element:", fruits[0])
print("Last element:", fruits[-1])

# Slicing
print("Slice (1:3):", fruits[1:3])

# Length
print("Length:", len(fruits))

# Membership test
print("Is 'apple' present?", "apple" in fruits)

# Count occurrences
print("Count of banana:", fruits.count("banana"))

# Index of an element
print("Index of mango:", fruits.index("mango"))

# Looping through the tuple
print("\nLooping through tuple:")
for item in fruits:
    print(item)

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("\nCombined tuple:", combined)

# Tuple repetition
print("Repeated tuple:", tuple1 * 2)

# Packing
student = ("Bharadwaj", 20, "IT")

# Unpacking
name, age, branch = student
print("\nUnpacked Values:")
print("Name:", name)
print("Age:", age)
print("Branch:", branch)

# List to tuple
numbers_list = [10, 20, 30]
numbers_tuple = tuple(numbers_list)
print("\nList to Tuple:", numbers_tuple)

# Tuple to list
numbers_list_again = list(numbers_tuple)
print("Tuple to List:", numbers_list_again)

# Nested tuple
nested = ("Python", (100, 200, 300))
print("\nNested Tuple:", nested)
print("Second value inside nested tuple:", nested[1][1])

# Numeric tuple functions
marks = (85, 90, 78, 95, 88)
print("\nMaximum:", max(marks))
print("Minimum:", min(marks))
print("Sum:", sum(marks))