#while loop = execute some code While some condition remains true

name = input("Enter your name:")
if name == " ":
  print("You did not enter your name")
else:
  print(f"Hello {name}")


#we can replace if statement with a while loop

while name == "":
  print("You did not enter your name")
  name = input("Enter your name:")
print(f"Hello {name}")


#example
age = int(input("enter your age:"))

while age < 0 :
  print("age can't be negative")
  age = int(input("enter your age:"))
print(f"you are {age} years old")


#example 2
food = input("enter a food you like(q to quit):")

while  not food == "q":
  print(f"You like {food}")
  food = input("enter a food you like(q to quit):")
print("bye")



# example 4
num = int(input("enter a number between 1-10: "))

while num < 1 or num > 10:
  print(f"{num} is not valid")
  num = int(input("enter a number between 1-10:"))
print(f"your number is {num}")

