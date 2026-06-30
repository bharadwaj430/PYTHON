#  13  chain assignment

x = y = z = 5

x += 2 #7
y *= 3 #15
z -= 1 #4

print(x , y, z) #7 15 4
print(x+y+z) #26



#problems on output formatting
#14 print pyramid using *
"""
  0  1 2 3 4 5 6 7 8
0          *
1        *   *
2      *   *   *
3    *   *   *   *
4  *   *    *  *    *

#spaces are decreasing in horizontal rows so we take n-i-1
"""

n = int(input("enter no of rows:"))
 #we use 2  nested for loops, one is for row and one is for column

for i in range(n):
  for j in range(n-i-1):
    print(" ",end = " ")
  for j in range(2*i+1):
    print("*",end = " ")
  print()







 



