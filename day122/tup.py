# Basic Tuple Example

# Creating tuples
fruits = ("apple", "banana", "mango", "orange")
numbers = (10, 20, 30, 40, 50)

# Printing tuples
print("Fruits:", fruits)
print("Numbers:", numbers)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing
print("First two fruits:", fruits[:2])

# Length
print("Number of fruits:", len(fruits))

# Membership
print("Is 'banana' present?", "banana" in fruits)

# Loop through tuple
print("\nFruits:")
for fruit in fruits:
    print(fruit)

# Tuple concatenation
new_tuple = fruits + ("grapes", "kiwi")
print("\nAfter concatenation:", new_tuple)

# Tuple repetition
print("Repeated tuple:", ("Hi",) * 3)

# Count and Index
marks = (90, 85, 90, 75, 90)
print("\nCount of 90:", marks.count(90))
print("Index of 75:", marks.index(75))

# Packing
student = ("Bharadwaj", 20, "IT")
print("\nPacked tuple:", student)

# Unpacking
name, age, branch = student
print("Name:", name)
print("Age:", age)
print("Branch:", branch)

# Nested tuple
nested = ((1, 2), (3, 4))
print("\nNested tuple:", nested)
print("First element of second tuple:", nested[1][0])

# Converting list to tuple
my_list = [100, 200, 300]
my_tuple = tuple(my_list)
print("\nList to tuple:", my_tuple)