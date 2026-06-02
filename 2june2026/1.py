#input in python 
"""
input() - used to accept values(using keyboard) from user
input() #result for input() is always string
int(input()) #int
float(input()) #float


"""

name = input("enter your name:") #user entered bharadwaj
print("welcome", name) #prints - enter your name:bharadwaj
                                 #welcome bharadwaj

age = input("your age is:") #input taken as 20 from user
age = ("you entered" , age) #output given  is 20


v = input("enter some value:")
print(type(v) , v)  # when entered some value <class 'str'> 1000
  #input converts anything to string





#typecasting any value to integer
int("9")
val = int(input("enter some value:"))
print(type(val), val) # when typed value as input as 27 - <class 'int'> 27


name = input("enter name:")
age = input("enter age:")
marks = input("enter marks:")

print("welcome" , name)
print("age  = " , age )
print("marks = " , marks)

"""  
output :
enter name:Bharadwaj
enter age:20
enter marks:95
welcome Bharadwaj
age  =  20
marks =  95

"""



 
