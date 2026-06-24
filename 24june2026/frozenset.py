#it is an immutable version of set
#like sets , it contain unique, unordered , unchangeable elements
#unlike sets, elements cannot be added or removed from frozen set

#creating a frozen set
#frozenset()-------constructor to create a frozenset from any iterable

x = frozenset({"apple","banana","cherry"})
print(x)
print(type(x))