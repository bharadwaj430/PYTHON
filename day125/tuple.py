#changing tuple values
x =("hyderabad","Mumbai","bangalore")
y = list(x)
y[1] = "jaipur"
x = tuple(y)
print(x) #('hyderabad', 'jaipur', 'bangalore')

#add items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


#remove items
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#deleting tuple
del thistuple
#  print(thistuple)  ---- raises an error


#UNPACK TUPLES

fruits = ("apple","banana","cherry")
(green,yellow,red) = fruits
print(green) #apple
print(yellow)#banana
print(red) #cherry


#using asterisk
froot = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red) = froot
print(red) #['cherry', 'strawberry', 'raspberry']

#loop through tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  """
  output:
apple
banana
cherry
  """

tuple1 = ("a","b","c")
tuple2 = (1,2,3)
tuple3 = tuple1+tuple2
print(tuple3)#('a', 'b', 'c', 1, 2, 3)


# multiply tuples
mytuple = thistuple * 3
print(mytuple)


#tuple methods
"""
count()---	Returns the number of times a specified value occurs in a tuple
index()---	Searches the tuple for a specified value and returns the position of where it was found

"""
tuple = (1,2,2,2,3,3,4,5,6,7,7)
print(tuple.count(7)) #2
print(tuple.count(2)) #3









