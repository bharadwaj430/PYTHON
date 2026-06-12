tuple = (1,) #the right way for a single tuple value to create(if we remove comma it takes as integer)
print(tuple) #(1,)
print(type(tuple)) #<class 'tuple'>

#if we remove comma it takes as integer
#for mul val

tuple1 =(1,2,3,4,) #comma is optional
print(tuple1[1:3]) #(2,3)

#if we want to find element 2
print(tuple1.index(2)) #return index of first occurence


# #existing of the element in tuple , counts total occurences
tuple2 = (1,2,3,4,1,2,3,4 ,4)
print(tuple2.count(4)) #3


