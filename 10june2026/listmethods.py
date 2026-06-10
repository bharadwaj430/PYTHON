# #list methods
"""
#1   list append  -----------list mutation (changing order of elements)
#2 list.sort ----------sorts in ascending order
#two types of sorting -----ascending and descending order
#list.sort #list goes to ascending order
#list.sort returns none  value
#list in descending order ------- list.sort(reverse ==True )  
list.sort(reverse = True)
"""


list = [2,1,3]
print(list.append(4) )
print(list.sort(reverse = True))
print(list)


list1 = ["banana" , "litchi" , "mango" ]
print(list1.sort(reverse = True))  #['mango', 'litchi', 'banana']-------i.e descending order
print(list1)


list2 = ["a","e","d","f"]
list2.reverse()
print(list2) #['f', 'd', 'e', 'a']


# #list.insert(index, element) #insert element at index

list3 = [4,1,2,3,6]
# #index   0 1 2 3 4 

# #if we want element 5 at  index 1

list3.insert(1,5)
# print(list3) #[4, 5, 1, 2, 3, 6] #1 val replaced  by 5















