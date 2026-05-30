#finding sum using arrays
arr = [1,2,3,4]
total  = 0

for num in arr:
  total += num  #total = total + num = 0 + 10 = 10
print(total)   #10


#matrix
#a matrix is an  array of rows and columns
matrix = [
   [1,2,3],    # 00 01 02  #arrangement of elements
   [4,5,6],    #10 11 12
  [25,3,19]]    #20 21 22
print(matrix[1][1])  #5
print(matrix[2][2])  #19
print(matrix[2][0]) #25


#loop through matrix
for row in matrix:
    for element in row:
        print(element)  #printing all these elements 
"""
1
2
3
4
5
6
25
3
19
"""



#matrix problem sum of all elements
matrix = [
    [1, 2],
    [3, 4]
]

total = 0

for row in matrix:
    for num in row:
        total += num

print(total)
