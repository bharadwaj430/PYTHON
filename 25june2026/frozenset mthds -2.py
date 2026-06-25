#method 6 ---issuperset()-----(>=)	 /(>)----Returns True if this frozenset is a (proper) superset of another


a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b)) #True
print(a >= b) #True
print(a > b) #True



#method 7 ------symmetric_difference()-----	^-----	Returns a new frozenset with the symmetric differences
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b)) #frozenset({1, 2, 4, 5})
print(a ^ b) #frozenset({1, 2, 4, 5})

#method 8 -----------union()-------	|------	Returns a new frozenset containing the union
a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))
print(a | b)




