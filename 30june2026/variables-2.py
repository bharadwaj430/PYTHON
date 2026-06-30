#VARIABLE NAMES

"""
rules of variable names

1.start with underscore /letter
2.can't start with number
3.contains only alphanumeric characters,underscores(A-Z),(0-9),(_)
4.THEY Are case sensitive
"""

_student = "bharadwaj"
Student0_ = "saheel"
student = "harish"
print(_student,Student0_,student) #bharadwaj saheel harish



#multi word variable names
myVariableName = "hyderabad" #camel case ----Each word, except the first, starts with a capital letter
MyVariableName = "John"#pascal case ----Each word starts with a capital letter
my_variable_name = "capital city"#  snake case -----Each word is separated by an underscore character

#assign multiple values 
#1. many values to multiple variables in one line
x,y,z = "ASIA","North america","russia"
print(x)
print(y)
print(z)



#one value to multiple variables
m = n = o = "bhaskar"
print(m) #bhaskar
print(n) #bhaskar
print(o) #bhaskar



#unpacking a collection

vegetables = ["brinjal","tomato","potato"]
j,k,l = vegetables
print(j) #brinjal
print(k) #tomato
print(l) #potato

#output variables

x = "python is awesome"
print(x)

d = "bharadwaj"
e = " is "
f = " student"
print(d,e,f) #bharadwaj  is   student
print(d +e+f) #bharadwaj is  student #space character matters


#global variables
#def : variables that are create outside of a function

#global variables can be used by everyone,both inside a fn and outsdie a fn

#Create a variable outside of a function, and use it inside the function
b = " bhaskar"
def myfunc():
  print("my college name is"  + b) #my college name is bhaskar
myfunc()



#Create a variable inside a function, with the same name as the global variable

c = "cinematography"
def myfunc():
  c = "video editing"
myfunc()
print("i love " + c)








