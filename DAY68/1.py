#forward recursion concept
def printNumbers(number , n):
    if number > n : # Base Case
        return
    print(number , end=' ')
    printNumbers(number , n) 
n = 7
number  = 10
for n in range (0,n):
 printNumbers( number ,n)
