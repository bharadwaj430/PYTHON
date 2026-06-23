#The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) #{'google', 'cherry', 'banana', 'microsoft'}


#an alternative for symmetric_difference() method 
#prints the same result

set4 = set1 ^ set2
print(set4) #{'google', 'cherry', 'banana', 'microsoft'}

#The symmetric_difference_update() method will also keep all but the duplicates,
#  but it will change the original set instead of returning a new set.

set1.symmetric_difference_update(set2)

print(set1)






