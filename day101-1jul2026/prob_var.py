# problem 8 memory reference 
x = [10,20]
y = x

y.append(30)

print(x)
print(y)

"""

here x is the given list and append() method is used to add single item to 
end of the list
so to x as list y = 30 is added as y = x is given x = [10,20,30]

as we mentioned here  y = x in code ,
total list of x is copied to y  and 30 is added to existing list
"""


#problem 9
"""
Predict.

a = 100
b = 100

print(id(a))
print(id(b))
print(a is b)

Then try

a = [1]
b = [1]

print(id(a))
print(id(b))
print(a is b)

"""


# 9  integer identity test
a = 100
b =100

print(id(a)) #140734929920216
print(id(b)) #140734929920216
print(a is b) #True 
"""
explanation
small integers range from -5 to 256----are preallocated

100 falls in the above range--- it doesnt create to seperate integer objects---but it points both variables to exact same obj in memory
point to same obj so id () values are identical ---------{ id()---returns  memory address of object}

3. is operatoer checks for identity(whether two variables point to exact same memory allocation)
so a is b evaluates True

"""

# #part 2 list identity test
a = [1]
b = [1]

print(id(a)) #2572492715968
print(id(b)) #2572492599232
print(a is b) #False


"""
mutable objects: lists
python is forced to allocate a brand new block of memory for it
regardless  ofwhether a list of identical content already exists

even though a and b have exact same value,but two are distinct objects

id(a) and id(b)-----yield different memory addresses


there is different locations
the identity check a is b evaluates  to False
"""

