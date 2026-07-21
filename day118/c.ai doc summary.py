"""
a python list is a dynamic array ---means---1.A Python list is a container that stores multiple values in order.
dynamic = automatically changes its size when needed----If you need more space, magically becomes larger.

"""
numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)


"""
computer RAM is like apartments
in memory
100
101
102

each number is one memory location

contigious -----next to each other without gaps
ex : 10,11,12,13,14-------contigious
ex: 10,15,20,25----- these are not contigious



#HOLDING POINTERS TO OBJECTS
Python list does not store actual objects directly.
It stores addresses
"""
lst = [10,20,30]
print(lst[2])

#O(1) means--Always takes almost the same amount of time, regardless of list size.

#address = base address + (index * pointer size)---direct searching   ---indexing is O(1)




