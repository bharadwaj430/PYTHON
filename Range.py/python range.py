#The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
#the set of numbers has its own datatype called range

#creating ranges
"""
the range() function can be called with 1,2,3 arguments by using
syntax:
range(start,stop,step)
range(x) --- x is stopping value
if range(10) -- then it takes as 0 to 9
0 --- inclusive
10--- stop argument is exclusive
"""
x = range(10)


#calling range() with two arguments
"""
range(3,10)---- 3 is start value , 10 is stop value---- numbers from 3 to 9
"""
y = range(3,10)


#calling with three arguments-----returns a sequence of each number from 3 to 9, with a step of 2:
range(3,10,2)



