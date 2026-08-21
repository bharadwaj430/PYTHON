#problem 1
#Student result calculator
python = int(input("enter python marks:"))
sql = int(input("enter SQL marks:"))
dsa = int(input("Enter DSA marks:"))
Total_marks = python + sql + dsa
Average_marks = Total_marks / 3
print(python)
print(sql)
print(dsa)
print(Total_marks)
print(Average_marks)
def calculate_total(python, sql, dsa):
  if Average_marks>=90:
    print("Grade: A")
  elif Average_marks>=75:
    print("Grade: B")
  elif Average_marks>=60:
    print("Grade:C")
  elif Average_marks>=50:
      print("Grade:D")
  else:
      print("Grade:F")

calculate_total(95,67,79)



#problem 2 -- simple calculator
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
operator = input("Enter operator:")
           

def calculator(num1,num2,operator):
   if operator == "+":
    print(num1 + num2)
   elif operator == "-":
    print(num1 - num2)
   elif operator == "*":
    print(num1*num2)
   elif operator == "/":
     print(num1/num2)




#problem 3   employee salary calculator
def calculate_salary(basic_salary, bonus=5000, tax_rate=10):
    gross_salary = basic_salary + bonus
    tax = gross_salary * tax_rate / 100
    net_salary = gross_salary - tax

    return net_salary


print(calculate_salary(30000))
print(calculate_salary(30000, 8000))
print(calculate_salary(30000, tax_rate=15))




#problem 5
def calculate_average(*marks):
    total = sum(marks)
    average = total / len(marks)
    return average


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


def display_result(name, *marks):
    average = calculate_average(*marks)
    grade = find_grade(average)

    print("Student Name:", name)
    print("Marks:", marks)
    print("Average:", average)
    print("Grade:", grade)

display_result("Bharadwaj", 85, 90, 78, 88, 92)





     




