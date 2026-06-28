
#1  swap without third variable
list = ["benz","audi"]
list[0],list[1] = list[1],list[0]

print(list)  #['audi', 'benz']

#2---find datatype of variable
a = 25.5
print(type(a)) #<class 'float'>

#3----convert string to int
"""
int(x): Converts x to an integer. 
Floats will be truncated toward zero (decimals are discarded).
float(x): Converts x to a floating-point number.
str(x): Converts x into its string representation.
bool(x): Converts x to True or False.
 Empty collections or 0 evaluate to False, while anything else evaluates to True
"""
number = int("25")
print(type(number)) #<class 'int'>

