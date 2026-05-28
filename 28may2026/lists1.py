"""
scenario: you are a teacher in a class and storing marks of students


"""


marks1 =94.4
marks2 = 87
marks3 =95
marks4 =66
marks5 = 45
#to simplify this we use a built in datatype

marks = [ 94.4,87,95,66,45]
print(marks)  #[94.4, 87, 95, 66, 45]
print(type(marks)) #<class 'list'>
print(marks[1:4]) #[87, 95, 66]
print(marks[1:]) #[87, 95, 66, 45]
print(marks[:4]) #[94.4, 87, 95, 66]


#list is similar to strings
print(marks[0]) #94.4
print(marks[1]) #87
print(len(marks)) #5


#student list
#printing list as student =[ name,marks,age,location]
student = ["bharath",85,20,"hyderabad"]
print(student)






