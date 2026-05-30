#concept required for 566 leetcode problem
#reshape matrix
"""
1.#required concepts - mid level problem solving range
2. array concept
3.matrix concept
4.simulation concept
"""
#arrays [ lists in python ]
"""
array is collection of values stored in order
"""
#           0  1  2  3  4  --> index
numbers = [10,20,30,40,50]
#Access elements

print(numbers[0]) #10
print(numbers[2])  #30


#modifying elements - changing existing elements to a new value
numbers[1] = 100
print(numbers) #[10, 100, 30, 40, 50] -> changed value is 100 in place ofindex 1 i.e 20

#IMPORTANT ARRAY OPERATIONS

#length of array
print(len(numbers)) #5


#looping through an array 
for num in numbers:
  print(num)

"""
10
100
30
40
50
"""

#LOOPING THROUGH AN INDEX 
for i in range(len(numbers)):
    print(i,numbers[i])

    """
    0 10
    1 100
    2 30
    3 40
    4 50
    """










