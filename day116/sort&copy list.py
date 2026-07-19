#sorting list alphanumerically-

#alphanumeric ---   alphabet + numericals(numbers)


#Sort the list alphabetically
havelist = ["book","pen","bag","laptop","earpods","spectaculars","apron"]
havelist.sort()
print(f"the sorted list alphabetically  is:{havelist}") #['apron', 'bag', 'book', 'earpods', 'laptop', 'pen', 'spectaculars']


#sorting list numerically
list = [23,45,67,89,9,56]
list.sort()
print(f"numerically sorted list is:{list}") #numerically sorted list is:[9, 23, 45, 56, 67, 89]


#sort descending---alphabets are sorted in right to left alphabetically
#to sort descending, use keyword argument reverse = True 

havelist.sort(reverse = True)
print(havelist) #['spectaculars', 'pen', 'laptop', 'earpods', 'book', 'bag', 'apron']

#customize sort fn-- customize own fn by key = function
#Sort the list based on how close the number is to 50:

def myfunc(n):
 return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) #[50, 65, 23, 82, 100]



#case insensitive sort
#uppercase to lowercase order
islist = ["banana", "Orange", "Kiwi", "cherry"]
islist.sort()
print(islist) #['Kiwi', 'Orange', 'banana', 'cherry']

#lowercase to uppercase order
islist.sort(key = str.lower)
print(islist) #['banana', 'cherry', 'Kiwi', 'Orange']



#reverse order not considering alphabetically
islist.reverse()
print(islist) #['Orange', 'Kiwi', 'cherry', 'banana']





#copy lists
#built-in List method copy() to copy a list.


inlist = islist.copy()
print(f"the copied list method 1 is :{inlist}")


#or
#using slice operator
list_ = islist[:]
print(f"the copied list method 3 is :{list_}")



















