#loop through index numbers
thislist = ["tomato","potato","capsicum"]
for i in range(len(thislist)):
  print(thislist[i])



#or
##loop through list
for x in thislist:
  print(x)

"""
o/p :
tomato
potato
capsicum
"""


#loop through list comprehension
#List Comprehension offers the shortest syntax for looping through lists:
[print(x) for x in thislist]




