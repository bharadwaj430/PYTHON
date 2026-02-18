# 1. Get user input and convert it to an integer
user_input = input("Enter a number to square and cube: ")
number = int(user_input)
# 2. Calculate the Square (number to the power of 2)
square = number ** 2

# 3. Calculate the Cube (number to the power of 3)
cube = number ** 3

# 4. Print the results
print("The square of " + str(number) + " is: " + str(square))
print("The cube of " + str(number) + " is: " + str(cube))