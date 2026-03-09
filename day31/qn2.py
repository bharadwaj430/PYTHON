"""
String characters balance Test
Write a program to check if two strings are balanced. 
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. T
he character’s position doesn’t matter.

"""
s1 = "abc"
s2 = "cbadef" 
# convert string to set
s1_set = set(s1)  
s2_set = set(s2)
# check if s1_set is subset of s2_set
if s1_set.issubset(s2_set):
    print("The strings are balanced.")
else:
    print("The strings are not balanced.")
  

