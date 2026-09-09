# Common array (list) operations in Python

arr = [5, 2, 8, 1, 9, 3]

# Basic operations
arr.append(10)          # Add to end
arr.insert(0, 0)         # Insert at index
arr.pop()                 # Remove & return last element
arr.remove(2)             # Remove first occurrence of value
arr.sort()                # Sort in place
arr.reverse()              # Reverse in place

# Slicing
print(arr[1:4])           # Elements from index 1 to 3
print(arr[::-1])          # Reversed copy

# Common patterns
print(max(arr), min(arr), sum(arr))
squared = [x**2 for x in arr]              # List comprehension
evens = [x for x in arr if x % 2 == 0]     # Filtering
total = sum(x for x in arr if x > 3)       # Conditional sum

# Searching
print(8 in arr)            # Membership check
print(arr.index(8))        # Find index of value

# 2D array (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]