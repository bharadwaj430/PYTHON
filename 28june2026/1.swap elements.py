
#METHOD 1 SWAPPING ELEMENTS(tuple assignment)

#python  lets bypass that by a feature called iterable unpacking(tuple assignment)
#  Python can evaluate expressions on RHS of an assignment operator before binding them to the variables on the LHS. This allows you to swap two variables in a single line without a third variable.


a = 23
b = 9
a,b = b,a
print(f"a:{a},b:{b}") #a:9,b:23


#METHOD 2 SWAPPING ELEMENTS(swapping by list)

#SWAPPING BY two items inside a list
#need target on index elements


#index     0      1       2
items = ["benz","ford","mustang"]
items[0],items[1]= items[1],items[0]
print(items) #['ford', 'benz', 'mustang']


#here we can observe that the elements are swapped with the help of the indices i.e
#the interchanging elements are 0-benz,1-ford


#method 3  (using tempo var)

a = 5
b = 10
variable = a
a = b
b = variable

print(a)
print(b)  #elements are swapped a = 10 , b =5






