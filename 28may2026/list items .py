#it can can be referred by index number
rand_list = ["school","college", "university" , "corporate job","business", "govt job", "finance manager"]
print(rand_list[2]) #university


#negative indexing starts from an end 
#-1 starts from an end
#-2 refers as second last item
print(rand_list[-3])  #business


#range of indexes
#we can specify where to start and where to end
#when specify a range , return val will be new list with specified items

print(rand_list[2:5]) #['university', 'corporate job', 'business']
#2 will be included and 5 will be not included

list_i_have = ["book","pen","laptop","mobile","adaptor"]
print(list_i_have[:4])  #['book', 'pen', 'laptop', 'mobile']
#it prints  and returns every item from beginning  in the list except index  element(that mentioned )


the_list = ["fruit","vegetable", "water","protein"]
print(the_list[2:])
#the items given after indexed element are displayed upto end

#range of -ve indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])   #['orange', 'kiwi', 'melon']












