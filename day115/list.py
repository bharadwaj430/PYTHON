#LIST COMPREHENSION
#shorter syntax when you want to create a new list based on values of existing list

#syntax
# newlist = [expression for item in iterable if condition == True]

"""
the return value is new list ,leaving the old list unchanged
"""
#CONDITION 
#the condition is like a filter that only accepts the items that evaluate to True

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)#['apple', 'banana', 'mango']


#or

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #['apple', 'banana', 'mango']






