#problems on variable and input

#1  Convert int to float
a = 25
print(float(a)) #25.0


#2Convert float to int
b =3.5
print(int(b)) #3

#3  multiple assignment

#type 3(i)  assign multiple values to multiple variables
#variables on LHS = Variables on RHS

name,age,height = "bharath",20,5.5
print("name of the person:",name)#name of the person: bharath
print("age of the person:",age) #age of the person: 20
print("height of the person:",height)


#type 3(ii) assign same values to multiple variables
# Assigning the integer 0 to three different variables
x = y = z = 12

print("value1 :",x) #value1 : 12
print("value 2:", y) #value2 : 12
print("value 3" ,z)#value3 : 12


#4 print variable values in one line
print({"student": "suresh","age": 25 , "weight":65})
#or

name = "shiva"
score = 95
status = "Passed"

print("Result:", name, score, status) #Result: shiva 95 Passed


# 5 take multiple inputs
name = str(input("enter student name:"))
standard =int(input("enter his standard in school:"))


#6 calculate sum using user input
a = int(input("enter first number:")) #enter student name:mohan
b = int(input("enter second number:")) #enter his standard in school:9

sum = a+b
print(sum)
"""
output
enter first number:5
enter second number:9
14
"""








