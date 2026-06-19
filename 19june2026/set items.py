#set items are unordered , unchangable, do not allow duplicate values
"""
unordered
items in a set do not have a defined order

set items can appear in a different order everytime u use them
cannot be referred to be index or key


UNCHANGEABLE
set items are unchangeable, means that we cannot change the items after the set has been created

DUPLICATES are not allowed in sets

"""

my_set = {"banana","cherry","apple"}
print(my_set) #'banana', 'cherry', 'apple'}

#true and 1 are considered as same value

my_set1 = {"fruits","veggies","proteins",True,1,2}
print(my_set1)  #{'proteins', 2, True, 'fruits', 'veggies'}

"""
Sets are unordered:
 The items do not have a defined order,
 so the exact sequence of the output might vary each time the code is run,
but it will only contain those five unique items
"""


