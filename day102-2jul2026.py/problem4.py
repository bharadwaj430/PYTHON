"""
Convert kilometers to

1.meters
2.centimeters
3.millimeters
"""


kilometers = int(input("enter the no . of kilometers:")) #enter the no . of kilometers:5

meters =  kilometers * 10**3
centimeters = kilometers * 10**5
millimeters = kilometers* 10 **6

print("the conversion of km to m is:", meters , "m") #the conversion of km to m is: 5000 m
print("the conversion of km to cm is:", centimeters , "cm") #the conversion of km to cm is: 500000 cm
print("the conversion of km to mm is:", millimeters , "mm") #the conversion of km to mm is: 5000000 mm





