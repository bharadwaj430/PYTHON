
#method 1 -------copy() - returns a shallow copy of set

fs = frozenset({1,2,3})
cp  = fs.copy()
print(fs) ##frozenset({1, 2, 3})
print(cp) #frozenset({1, 2, 3})

#method 2 ---- difference() ----(-)------returns a new frozenset with the difference

b = frozenset({1,2,3,4})
m = frozenset({3,4,5})
c = frozenset({2,3})
print(b.difference(m)) #frozenset({1, 2})
#or
print(b-m) #frozenset({1, 2})

#method 3 -----intersection()---(&)------returns a new frozenset with the intersection

print(b.intersection(m)) #frozenset({3, 4})

#or

print(b&m) #frozenset({3, 4})


#method 4 ---isdisjoint()----(<=/<)----Returns True if there is NO intersection between two frozensets

print(b.isdisjoint(m)) #False
print(b.isdisjoint(c)) #False


#method 5 ----issubset()---(>=/>)----	Returns True if this frozenset is a (proper) superset of another

print(b.issuperset(m)) #False
print(b>=m) #False
print(b>m) #False

print(b.issuperset(c)) #True




