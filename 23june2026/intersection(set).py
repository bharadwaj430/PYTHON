#INTERSECTION


#keep only the duplicates
#shows and returns common items in both set


cars1 = {"porsche","bmw","benz"}
cars2 = {"benz","maruti800","xuv500"}



cars3 = cars1.intersection(cars2)
print(cars3)    #{'benz'}

#join two sets using & -----similar to intersection ()
cars4 = cars1 & cars2
print(cars4)   #{'benz'}


# intersection_update()
#keeps only duplicates---change original set instead of returning a new set ------Keep the items that exist in both set1, and set2

cars1.intersection_update(cars2)

print(cars1) #{'benz'}


#----------------------EXAMPLE 2-----------------------

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

#The values True and 1 are considered the same value. The same goes for False and 0.


set3 = set1.intersection(set2)

print(set3) #{False, 1, 'apple'}


 







