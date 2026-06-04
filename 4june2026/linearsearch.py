"""
DSA  is backbone of problem solving
- DS stores data in a structured way like arrays , dict, linked lists
- algo is process how we are solving prblms
Time  COMPLEXITY and space complexity
1.time  complexity measures how it grows with input size

2.space complexity measures how much memory is required

O(1) -  constant ----i.e no loops
O(log N)- logarithmic---- search algos having log n if they are sorted(binary search)
O(n)- linear --- for  loops and while loops with n items
O(n log(n)) log linear ------used in sorting operations

-O(n^2)-Two nested loops--- Quadratic- every element in a collection needs comparison to every other element
-O(2^n)- Exponential------- recursive algorithms that solves a prblm of size N
-O(n!) Factorial- you are adding a loop for every element
-Iterating through half a collection is still O(n)
-Two separate collections: O(a * b)



O(n) ---- linear search ----checks each

"""
#Linear search works by checking every element 
# in a list one by one from start to finish until the target value is found.
#2. it is also called as sequential search
#3 it is simplest searching algorithm


def linear_search(arr, target):
    # Loop through every element using its index
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if the target is not in the array

# Example Usage
numbers = [10, 50, 30, 70, 80, 20]
target_value = 30

result = linear_search(numbers, target_value)
print(f"Element found at index: {result}")  # Output: 2
