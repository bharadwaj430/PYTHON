#level 2 ----input & type conversion

#6 
"""
Take input:

1.Name
2.Age
3.CGPA

Print them with their data types.

"""

name = str(input("enter name of the student:")) #ganesh
age = int(input("enter age of student")) #19
CGPA =float(input("enter your score:")) #9.5

print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(CGPA)) #<class 'float'>


#7  calculator variables
a = 10
b = 5
print(a+b)# ---addition-------- #15
print(a - b) #---subtraction---- #5
print(a*b) #----multiplication--- #50
print(a/b) #----divison---- #2.0
print(a%b) #---modulus---- #0
print(a//b )# ---floor divison---- #2
print(a**b) #---power #100000


#8 celsius to fahrenheit
"""
concept involved :
#8(i) fahrenheit to celsius
c = (f -32)*5/9


#8(ii)  celsius to fahrenheit
f = 32 + 9/5 *c => 32 + 1.8*c
c =(f-32) *1.8

"""
c = float(input("enter celsius temperature:")) #enter celsius temperature:45
division_of_c = c * 1.8
result  = division_of_c + 32

f = result

print(f"the value of celsius is {c} .the value of fahrenheit is {f} ") #the value of celsius is 45.0.the value of fahrenheit is 113.0 


# 9 area calculator
l = int(input("enter length:")) #enter length:25
b = int(input("enter breadth:")) #enter breadth:5
area = l*b
a = area
print("the area is:",a)  #the area is: 125

#10 type conversion challenge
n = 25
print("enter the float value of n is:",float(n)) #25.0
print("type is",type(float(n))) #type is <class 'float'>

print("enter the string value of n is", str(n)) #25
print("type is", type(str(n))) #type is <class 'str'>

print("enter the boolean value of n is:",bool(n)) #True
print("type is:" ,type(bool(n))) #type is: <class 'bool'>



















