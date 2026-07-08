# 1. Create a basic list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# 2. Access items using index numbers (Python starts counting at 0)
first_fruit = fruits[0]
print("First fruit:", first_fruit)

# 3. Add a new item to the end of the list
fruits.append("orange")
print("After adding orange:", fruits)

# 4. Change the value of an existing item
fruits[1] = "blueberry"
print("After changing banana to blueberry:", fruits)

# 5. Remove an item by its name
fruits.remove("cherry")
print("After removing cherry:", fruits)

# 6. Get the number of items in the list (length)
list_length = len(fruits)
print("Number of fruits in the list:", list_length)

# 7. Loop through the list to print each item
print("Looping through items:")
for fruit in fruits:
    print("-", fruit)


"""
Original list: ['apple', 'banana', 'cherry']
First fruit: apple
After adding orange: ['apple', 'banana', 'cherry', 'orange']
After changing banana to blueberry: ['apple', 'blueberry', 'cherry', 'orange']
After removing cherry: ['apple', 'blueberry', 'orange']
Number of fruits in the list: 3
Looping through items:
- apple
- blueberry
- orange
"""