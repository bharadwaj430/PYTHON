#CRUD Operations 
"""
c - create/add elements
r - read/access elements
u - update/modify
d - delete/remove 
"""
#creating a student list
lst_1 = ["rahul","priya","aman","sneha"]
print(f"the list is created{lst_1}")

#2. Add Multiple Numbers
#Create a list.
#Take five integers from the user and store them

lst = []
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
d = int(input("enter the fourth number:"))
e = int(input("enter the fifth  number:"))

lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)
lst.append(e)
print(lst)



#insert Mango at index 1
fruits = ["Apple","Banana","Orange"]
# fruits.insert(1,"Mango")
# print(fruits) #['Apple', 'Mango', 'Banana', 'Orange']


#add "python " at beginning
fruits.insert(0,"Python")
print(fruits) #['Python', 'Apple', 'Banana', 'Orange']

#add at end
fruits.append("AI")
print(fruits) #['Python', 'Apple', 'Banana', 'Orange', 'AI']




