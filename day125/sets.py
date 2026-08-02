myset = {"gloves","leather jacket","bike","helmet",True,0}
print(myset) #{0, True, 'helmet', 'gloves', 'leather jacket', 'bike'}

#length of set
print(len(myset)) #6
print(type(myset)) #<class 'set'>

#set can be of any datatype
set1 = {"abc", 34, True, 40, "male"}
print(set1)


#access set items
for x in myset:
  print(x)
"""
True
helmet
gloves
leather jacket
bike
"""


print("bike" in myset) #True 
print("bike" not in myset) #False

#add items in set
myset.add("car")
print(myset) #{0, True, 'helmet', 'gloves', 'car', 'bike', 'leather jacket'}

aeroplane = {"switches","passengers" , "uniform","luggage"}
myset.update(aeroplane)

print(myset) #{0, True, 'helmet', 'car', 'passengers', 'switches', 'leather jacket', 'uniform', 'gloves', 'bike', 'luggage'}


#add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) #{'apple', 'cherry', 'kiwi', 'banana', 'orange'}


#remove items
myset.remove("gloves")
myset.discard("leather jacket")
myset.pop()

print(myset) #{True, 'bike', 'uniform', 'helmet', 'passengers', 'switches', 'car', 'luggage'}


#loop sets
set = {"book","bottle","bag"}
for x in set:
  print(x)

"""
bottle
bag
book

"""

set_1 = {"fire","water","land"}
set_2 = {"sky","air"}
set_3 = {'god','godess'}

five_elements = set_1.union(set_2,set_3) #join
set3 = set_1 | set_2 #join
print(set3) #{'sky', 'land', 'fire', 'water', 'air'}
print(five_elements)


#joining multiple sets
product_based = {"apple",'meta',"amazon",'google'}
the_set = set1.union(set_2,product_based)
print(the_set) #{True, 34, 'apple', 'sky', 'abc', 40, 'air', 'google', 'amazon', 'meta', 'male'}


#INTERSECTION
set1 = {"apple", "banana", "cherry"}
set2 = {"TCS", "wipro", "infosys","apple"}
# set3 = set1.intersection(set2)  or set3 = set1 & set2
set3 = set1 & set2 
print(set3)#{'apple'}  





















