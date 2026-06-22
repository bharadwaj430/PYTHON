#join multiple sets 
#All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas:

#join multiple sets with the union()  method

set1 = {"a","b","c"}
set2 = {"john","elena"}
set3 = {"apple","bananas","cherry"}
set4 = {"apple","bananas","cherry"}

myset  = set1.union(set2,set3,set4)
print(myset) #{'elena', 'c', 'bananas', 'cherry', 'b', 'a', 'apple', 'john'}

thisset = set1 | set2 
print(thisset) #{'john', 'c', 'b', 'a', 'elena'}


#join a set and a tuple 
#The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a","b","c"}
y = (1,2,3)


#The union() method allows you to join a set with other data types, like lists or tuples.
z = x.union(y)
print(z)