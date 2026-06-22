#the update method inserts all items from one set into another
#the update() changes  the original set and does not return a new set

#the update item inserts the items in set2 into set1

set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1) #{'b', 1, 2, 3, 'a', 'c'}

