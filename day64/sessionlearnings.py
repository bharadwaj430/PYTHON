#Generators---------
#it is special type of a function that returns values one by one instead of returning everything at once
#1st program
def num():
    print(1)
    print(2)
n = num()
print(n) 

#2nd program
def num():
    return [1,2,3]
print(num())   #printing list

#3rd program
def num():
    yield 1
    yield 2
    yield 3
print(num())
for i in num():   # printing sequence of line by line numbers
    print(i) 

#advantages of generators
#memory efficient-saves more space
#Faster to execute
#useful for large data analysis


#4th program
def square(n): # user i/p
    for i in range(n): # 0,1,2,3,4
        yield i*i #0,1,4,9,16

n = int(input())#i/p 
for j in square(n):#
    print(j)


def num():
    yield 1
    yield 2
    yield 3

n = num()

print(next(n))
print(next(n))
print(next(n))



#output :
"""
1
2
None 
[1, 2, 3]    
<generator object num at 0x000001401B375C00>  
1 
2
3
"""