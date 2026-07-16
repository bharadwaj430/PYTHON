this_list = ['table','chair',"sofa","television"]
#+ve indexing    0       1        2             3
#-ve indexing    -4    -3       -2           -1

#print last item using negative indexing
print(f"the last item using -ve indexing is:{this_list[-1]}")


#Print the second last item
print(f"the last item using -ve indexing is:{this_list[-2]}")

#Print the third last item.
print(f"the last item using -ve indexing is:{this_list[-3]}")


#Print the first and last elements using positive and negative indexing together

print(f"first and last elements using positive and negative indexing together{this_list[-4::2]}")

# Find whether first element equals last element.
# Print True or False.
if ["table"] ==  ["television"] in this_list:
  print(True)
else:
  print(False)

#Store the last element in a variable and print it
a = this_list[3]
print(a)


#swap printing order
list = [1,2,3]
print(list[2]) #3
print(list[1]) #2
print(list[0]) #1


