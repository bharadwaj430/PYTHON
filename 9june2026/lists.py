#lists in python
"""
a built in datatype  that stores set of values
- it can store element of different types(integer, float, string etc)
"""
#storing marks of five students
marks1 = 94.4
marks2 = 87
marks3 = 95
marks4 = 66
marks5 = 45.1
#to simplify this we got a datatype
marks = [94.4,87,95,66,45.1] #list in python
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

#python list can store different details together

student = ["bharadwaj","90","hyderabad"]
print(student) #print student information
#print each string
print(student[0]) 
print(student[1])
print(student[2])


#strings are immutable - immortal --- things that can't change
#lists are mutable -mortal ----things that can be changed
str = "hello"
#  str = [0] = "y"  ------as strings are immutable  shows error

student[0] = "mohan"
#studnet[5] --- error string index out of range
print(student)

