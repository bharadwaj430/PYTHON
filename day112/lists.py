a = ["earth","sun","sky","air","water"]
#printing the list
print(a) #['earth', 'sun', 'sky', 'air', 'water']

#indexing in list
#positive indexing
print("the first item is:", a[0]) #the first item is: earth
print("the second item is:" , a[1])#the second item is: sun


#negative indexing
print("the last item is:" , a[-1]) #the last item is: water


#range of indexes
print("the range1 in positive indexes are:", a[1:3]) #the range1 in positive indexes are: ['sun', 'sky']
print("the range2 is:", a[1:]) #the range2 is: ['sun', 'sky', 'air', 'water'] 
print("the range4 is:", a[:4]) #the range4 is: ['earth', 'sun', 'sky', 'air']


#replacing the list elements
a[0] = "wind"
print(a)



