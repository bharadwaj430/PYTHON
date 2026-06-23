#the difference method will return a new set which has
#1.only items of set1 and they are not present in set2

set1 = {"apple","meta","netflix","amazon"}
set2 = {"apple","google","paytm","phonepe"}

set3 = set1.difference(set2)
print(set3) #{'amazon', 'meta', 'netflix'}



#we can also use "-" operator instead of difference() method --------we get same result

set3 = set1 - set2
print(set3) ##{'amazon', 'meta', 'netflix'}

"""
Note: The - operator only allows you to join sets with sets,
and not with other data types like you can with the difference() method

"""


#The difference_update() method will keep the items from the first set that are not in the other set,
#but it will change the original set instead of returning a new set

fruits = {"apple","banana","cherry"}
companies = {"google","microsoft","apple"}

fruits.difference_update(companies)

print(fruits) #{'banana', 'cherry'}



