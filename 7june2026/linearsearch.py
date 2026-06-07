#linear search 

#linear search checks each element one by one until target is found

"""

Algorithm
1.Start from the first element.
2.Compare it with the target.
3.If equal, return its position.
4.Otherwise move to the next element.
5.Repeat until the end of the list.

Time Complexity 
Best Case : O(1)
Worst Case : O(n)
"""
#1 Find whether 25 exist in the list

numbers = [10, 15, 25, 40, 50]
target = 25

for num in numbers:
    if num == target:
        print("Found")
        break

#2 Find the index of 40.
numbers = [10, 15, 25, 40, 50]
target = 40

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Index:", i) #3
        break

#3 Count how many times 5 appears.
nums = [5, 2, 5, 7, 5, 1]
count = 0

for num in nums:
    if num == 5:
        count += 1

print(count)

#4 Find Largest Number Using Search
nums = [12, 45, 23, 89, 34]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print(largest)
