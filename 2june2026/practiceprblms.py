
#1 write a program to input 2 numbers & print their sum
a = int(input("enter the first number:")) #7 by user
b = int(input("enter the second number:")) #9 by user
sum = a + b #7+9 = 16
print(sum) #16


#2 write a program to input side of a square and print its area
side = int(input("enter side of square:")) #25 by user
area = side * side #area of square is side ** 2  #25*25 = 625
print("the area of square is:", area) #625



#3 write a program to input 2 floating point numbers and print thier average
decimal_val_1 = float(input("enter float value 1:"))
decimal_val_2 = float(input("enter float value 2:"))
print("average =" ,  (decimal_val_1 + decimal_val_2) / 2)

"""
output  #3 : 
enter float value 1:  4.5
enter float value 2: 6.5
average = 5.5
"""





#write a program to input 2 int numbers , a and b 
#print true if greater than or equal to b. if not print False.
a = int(input("the first number is:"))
b = int(input("the second number is:"))
if a >= b :
  print(True)
else:
  print(False)
"""

#case 1 true

the first number is:7
the second number is:5
True


#case 2 false
the first number is:35
the second number is:45
False
"""



