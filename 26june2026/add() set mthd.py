#python has a set of built in methods that you can use on sets

"""
add()----adds an element to the set
1.The add() method inserts exactly one immutable element (such as a string, number, or tuple) into the set. 
2.You cannot pass mutable objects like lists or dictionaries into this method.

"""

#create a set
fruits = {"apple","banana"}

#add a new element
fruits.add("cherry")
print(fruits) #{'banana', 'apple', 'cherry'}   -----sets are unordered

#adding an existing element(duplicate)

fruits.add("apple")
print(fruits)  #{'apple', 'banana', 'cherry'}----duplicates are quietly ignored

"""
add()-----Adds a single item---------.Only immutable items.-------Adds the whole iterable object as a single element (if immutable).

update()-------Adds multiple items----.Any iterable object-----Unpacks the iterable and adds its individual elements.

update()
The update() method adds multiple items at once.
it accepts any iterable object as an argument, such as another set, a list, a tuple, or a dictionary

 """
#example for update()

numbers = {1,2}#create a initializing set
numbers.update([3,4,2])
print(numbers) #{1, 2, 3, 4} ----duplicate 2 was ignored

#adding elements from other set and tuple simultaneously
extra_numbers = {5,6}
more_tuples = (7,8)
numbers.update(extra_numbers , more_tuples)
print(numbers)






