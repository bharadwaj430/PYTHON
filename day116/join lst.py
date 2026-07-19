#join or concatenate two or more lists
# mthd 1  using + operator
list1 = ["a","b","c","d"]
list2 = [1,2,3,4]

final_list = list1 + list2
print(f"the cobined list of two lists is:{final_list}")


#mthd 2 appending all items from list2 to list1
for x in list2:
  list1.append(x)
print(list1)

#mthd 3 using extend() method, where purpose is to add elements from one list to other list

list1.extend(list2)
print(list1)







