# In Python, standard dynamic arrays are built-in lists
numbers = [10, 20, 30, 40, 50]

# Access & Modify
first_item = numbers[0]  # 10
numbers[1] = 25  # [10, 25, 30, 40, 50]

# Add & Remove
numbers.append(60)  # Adds to the end -> [10, 25, 30, 40, 50, 60]
numbers.insert(2, 99)  # Inserts at index 2 -> [10, 25, 99, 30, 40, 50, 60]
removed_item = numbers.pop()  # Removes & returns last element (60)
numbers.remove(99)  # Removes first occurrence of 99

# Slicing [start:stop:step]
subset = numbers[1:3]  # [25, 30]
