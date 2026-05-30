#matrix
#python don't have built in fns for mtx
#we can use nested list,list to create a mtx or use a numpy library

#nested list as a matrix
#add and sub of mtx 
#we require two nested list
row = int(input("enter row number:"))
column = int(input("enter the column number:"))

print("enter the elements from matrix1:")
matrix1 = [[int(input())for i in range(column)] for j in range(row)]
print("matrix1:")
for i in range(row):
  for j in range(column):
    print(format(matrix1[i][j],"<3"),end="")
  print()

print("enter the elements from matrix2:")
matrix2 = [[int(input())for i in range(column)] for j in range(row)]
print("matrix2")
for i in range(row):
  for j in range(column):
    print(format(matrix2[i][j],"<3"),end="")
  print()

