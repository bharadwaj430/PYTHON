"""

#prob -1 multiple assignment

Assign values to five variables in a single line.
Print all values.
"""
var1,var2,var3,var4,var5 = 1,2,3,4,5

print(var1,var2,var3,var4,var5) #1 2 3 4 5


"""
Problem 2 Chain Assignment
Assign the same value to four variables.
Now change only one variable.
Predict the output before running.
 """
a = b= c = d = 5

d = 23
print(a,b,c,d) #5 5 5 23


"""
Problem 3  Input and Type

Take input:

Name
Age
Salary

Print:

Value
Data type
"""

name = str(input("enter your name:"))
age = int(input("enter your age:"))
salary = int(input("enter your salary:"))

#values
print("the name of the employee:",name) #enter your name:bharadwaj
print("the age of the employee:",age) #enter your age:23
print("the salary of employee:", salary) #enter your salary:50000

#datatypes
print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(salary)) #<class 'int'>

"""

problem 4 Type Conversion

Take one integer input.
Convert it into:
float
string
boolean
Print converted values and their data types
"""

a = int(input("enter the integer:")) #enter the integer:239

print("the decimal representation of integer" , float(a)) #the decimal representation of integer 239.0
print("the string represnetation of integer",str(a)) #the string represnetation of integer 239
print("the boolean represnetation of integer",bool(a)) #the boolean represnetation of integer True


"""
problem 5  marks analysis
Input:
Marks in five subjects.

Store:
Total
Average
Percentage

Print all values.

"""
telugu = 95
english = 98
maths = 79
hindi = 45
science = 80

print("marks scored in telugu:" , telugu) #marks scored in telugu: 95
print("marks scored in english:", english) #marks scored in english: 98
print("marks scored in maths:", maths) #marks scored in maths: 79
print("marks scored in hindi :", hindi )#marks scored in hindi : 45
print("marks scored in science:", science) #marks scored in science: 80


total_marks =telugu + english + maths + hindi + science
print(total_marks) #397

average = total_marks / 5
print(average) #79.4

percentage =(total_marks / 500 ) * 100
print(percentage) #79.4



"""
prob -6   rectangle calculator

Input:
Length
Breadth

Calculate:

Area
Perimeter

Store each result separately.
"""

length = int(input("enter length of rectangle:")) ##enter length of rectangle: 45
breadth  = int(input("enter breadth of rectangle:")) #enter breadth of rectangle:20
area_of_rectangle = length * breadth

print("area of rectangle  is :", area_of_rectangle)  #area of rectangle  is : 900 
perimeter_of_rectangle = 2*(length + breadth)   

print("permimeter of rectangle is :", perimeter_of_rectangle) #permimeter of rectangle is : 130


"""
Problem 7  Circle Calculator

Input radius.

Calculate:

Diameter
Circumference
Area

"""

radius_ofcircle = int(input("radius of circle is:"))


diameter_of_circle = 2 * radius_ofcircle
print( "diameter of circle is:" , diameter_of_circle) #diameter of circle is: 50

circumference_of_circle = 2*3.14* radius_ofcircle
print("circumference of circle:" , circumference_of_circle) #circumference of circle: 157.0

area_of_circle = 3.14*radius_ofcircle**2

print("area of circle is:" , area_of_circle) #area of circle is: 1962.5



 









