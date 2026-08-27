# 1. Simple function
def greet():
    print("Hello, welcome to Python!")


# 2. Function with parameters
def greet_user(name):
    print("Hello", name)


# 3. Function with return value
def add(a, b):
    return a + b


# 4. Function with multiple parameters
def calculate_total(price, quantity):
    return price * quantity


# 5. Function with a default parameter
def introduce(name, age=18):
    print(f"My name is {name} and I am {age} years old.")


# 6. Function accepting any number of arguments
def calculate_average(*marks):
    total = sum(marks)
    return total / len(marks)


# 7. Function calling another function
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Main program
greet()

greet_user("Bharadwaj")

result = add(10, 20)
print("Addition:", result)

total = calculate_total(500, 3)
print("Total price:", total)

introduce("Bharadwaj")
introduce("Bharadwaj", 20)

average = calculate_average(85, 90, 78, 92)
print("Average:", average)

grade = calculate_grade(average)
print("Grade:", grade)