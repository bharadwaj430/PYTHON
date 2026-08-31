# Function to calculate total marks
def calculate_total(maths, python, dsa):
    total = maths + python + dsa
    return total

# Function to calculate average
def calculate_average(total):
    average = total / 3
    return average

# Function to determine grade
def find_grade(average):
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


# Taking input
maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
dsa = int(input("Enter DSA marks: "))

# Calling functions
total = calculate_total(maths, python, dsa)
average = calculate_average(total)
grade = find_grade(average)

# Displaying results
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)