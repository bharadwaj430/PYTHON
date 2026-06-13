""""
write a program to check if a list contains a palindrome of elements or not
front and back reading is same
in coding if we make a copy and reverse it the last values come first ,then becomes palindrome
if it is non palindromic list
(i): copy
(ii): reverse
(iii):check original nd copy if same palindrome or else or not
ex: [1,2,3,2,1]
2.[1,"abc","abc",1]
3.racecar
4.ma'am
"""
list1 = [1,2,1] #prints palindrome
list2 = [1,2,3] #prints not palindrome


copy_list1 = list1.copy()
copy_list1.reverse() 
if (copy_list1 == list1 ):
  print("palindrome")
else:
  print("not palindrome")



copy_list2= list2.copy()
copy_list2.reverse() 
if (copy_list2 == list2):
  print("palindrome")
else:
  print("not palindrome")
