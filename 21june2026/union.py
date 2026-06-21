set1  = {"a","b","c"}
set2 = {1,2,3}
set3  = set1.union(set2)
print(set3) #{'c', 'a', 1, 'b', 2, 3}



#we can use operator |  instead of union() method 
set3 = set1 | set2
print(set3) #{1, 'a', 2, 3, 'b', 'c'}