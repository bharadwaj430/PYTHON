#set is the collection of the unordered items
#each element on the set must be unique and immutable

nums = {1,2,3,4}
set2 = {1,2,2,2,}
#repeated elements stored only once , so it resolved to {1,2}

null_set = set() #empty set syntax

#creation of a set
collection = {1,2,3,4,2,2,"hello","world","world",4}
#duplicate values are ignored
print(collection) #{1, 2, 3, 4, 'world', 'hello'}
print(type(collection)) #<class 'set'>
print(len(collection))  #total no of items = 6


collection1={}  #empty dictionary
collection2 = set() #empty set syntax

print(type(collection1))
print(type(collection2))

