"""
problem 3
convert minutes into
1. hours
2.remaining minutes

"""
#1 hour = 60 min
#i min = 0.016 hr

# min = int(input("enter the no of minutes:")) #enter the no of minutes:35 
# in_hrs = min*0.016
# print(in_hrs) #0.56

# remaining_min = 60 - min
# print(remaining_min) #25


"""
problem 4
calculate simple interest

inputs as 
principle,rate,time
"""
#Simple_interest =p*t*r/100
#where p = principle
# r = rate of interest
# t = time taken


# p = float(input("enter the principle amount:")) #enter the principle amount:20000
# t = float(input("time taken by person:")) #time taken by person:2
# r = float(input("rate of interest:"))  #rate of interest:5

# simple_interest = p*t*r/100

# print("the simple interest is:", simple_interest) #the simple interest is: 2000.0


"""
calculate compound interest

A = amount(principle + interest)
P = principal(initial investment)
r = interest rate(decimal)
n = no of times interest compounded per year
t = time in years


p = 1000
r = 5.5
t = 3.3
A = P*(1+r/100)**nt
CI = A - P
"""

P = float(input("enter the initial investment:"))
r = float(input("enter the rate of interest:"))
t = float(input("enter the time in years:"))
n = float(input("no of times the interest compounded per year:"))

A = P*(1+r/100)**n*t
 
print("enter the total amount(principal+ interest)", A)
print("enter the principal amount:", P)

CI = A - P
print("the compound interest :", CI)







