"""
equals: a==b
not equals: a!=b
less than : a < b
greater than : a > b
greater than or equal to : a>=b

above conditions can be used in several ways---used in if statements and loops

if statement ---------- using if keyword
"""
a = 10
b = 20
if b>a:
  print("b is greater than a")  #b is greater than a---(the statement is true)

"""
condition = true --- code block inside executes
condition = false --- code block skippped
"""

#indentation plays a key role
"""
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")


indentation must be like this
"""

#boolean variables can be used directly in if statements---withhout comparison operators

is_entry = True
if is_entry :
  print("Welcome") #Welcome



"""
Elif  keyword in python 
The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as
 one of the conditions evaluates to True.
"""

score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")


#o/p : Grade: C
"""
working of elif:  As soon as it finds a condition that is true, 
it executes that block and skips all remaining conditions.
"""

#else statement
"""

The else statement is executed when the if condition (and any elif conditions)
evaluate to False.
"""

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") #a is greater than b


#else without elif
#The else statement provides a default action when none of the previous conditions are true.

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#if-elif-else chain
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")


#python shorthand if
#possible only one statement to execute------you can put if statement on same line

a = 5
b = 2
if a<b: print("a is greater than b") 


#assign a value with if....else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger) #Bigger is 20

#ONE LINE CONDITIONAL STAT
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


















