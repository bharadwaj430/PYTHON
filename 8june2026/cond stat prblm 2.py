#write a program for finding greatest of 4 numbers given by user

#defining inputs of 4 numbers
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
d = int(input("Enter the fourth number:"))


#single line nested conditional expression
greatest_among_4 =  (a if a > b and a > c and a > d else (b if b > c and b > d else (c if c > d else d)))
print("The greatest number is:", greatest_among_4)
"""
Enter the first number:5
Enter the second number:6
Enter the third number:7
Enter the fourth number:8
The greatest number is: 8
"""



#write a program to check if a number is multiple of 7 or not
num = int(input("Enter the  number"))
if (num % 7 == 0 ):
  print("The number is divisible by 7")  #49 divisible by  7
else:
  print("The number is  not divisible by 7") #65 not divisible by 7



















