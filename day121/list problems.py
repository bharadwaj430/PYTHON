lst = ["car","bike","scooty","truck","van"]

#Access the third element of a list
print(f"the third element of the list is:{lst[2]}")

#List Length: Print the total number of items
print("length of the list" , len(lst))


#Check if the list is empty
if lst ==[]:
  print("The list is empty")
else:
  print("the list is not empty")
"""
Exercise 2. Perform List Manipulation
Practice Problem: Take a given list and modify it through five specific actions:

Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 o the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.
"""
list_m = [100, 50, 400, 500]

# a) Change Element
list_m[1] = 200
print(f"Updated (Change): {list_m}")

# b) Append Element
list_m.append(600)
print(f"Updated (Append): {list_m}")

# c) Insert Element
list_m.insert(2, 300)
print(f"Updated (Insert): {list_m}")

# d) Remove Element by value
list_m.remove(600)
print(f"Updated (Remove 600): {list_m}")

# e) Remove Element by index
list_m.pop(0)
print(f"Updated (Remove Index 0): {list_m}")



