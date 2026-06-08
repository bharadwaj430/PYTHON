#write a program to check if a number entered by user is odd or even
number = int(input("enter number given by user:"))
if number % 2 == 0 :
  print("The number is even ")
else:
  print("The number is odd")


#write a program  to find the greatest of 3 numbers entered by user
a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))

if(a>= b and a>=c):
  print("firt number is greatest", a)
elif(b>=c):
  print("second number is greatest", b)
else:
  print("third number is greatest",c)
  



