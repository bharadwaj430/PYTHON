#the object in the update() method does not have to be a set, it can be iterable objects like (list,tuple,dict)

#adding set items
set1 = {"book","table","pen"}
set2 = {"bag","shoes","clothes"}

set1.update(set2)
print(set1) #{'book', 'bag', 'clothes', 'shoes', 'pen', 'table'}


#remove items using remove() method
#to remove an item in a set, use the remove(), or the discard() method.
set1.remove("table")
print(set1) #{'pen', 'bag', 'book', 'clothes', 'shoes'} #table is excluded


#remove items using discard()  method

set2.discard("clothes")
print(set2) #{'bag', 'shoes'}

#pop()---- removes one item randomly
set3 = {"student","teacher","worker"}
x = set3.pop()
print(x) #worker or teacher or student
print(set2)

#clear method empties the set
set3.clear()
print(set3) #set()


#del keyword delete set completely

set = {"apple","banana","avocado"}
del set 
print(set) 