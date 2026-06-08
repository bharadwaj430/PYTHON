#using sub  conditions in if statements is called nesting
# nesting is completely valid in python 
age = 34

if(age>= 18 ):
  if(age>=80):
    print("cannot drive")  #age 82 cannot drive
  else :
   print("can drive") #age 34 can drive
else:
  print("CANNOT drive")