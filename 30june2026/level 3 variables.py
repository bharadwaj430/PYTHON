#11    Variable update
"""
manual debugging
given salary = 30000

Increase it by
1.10% #30,000 *0.1 = 3000 
first hike = 30000+3000 = 33000

2.then another 5%
#hike2 = first hike * 0.05 = 33000*0.05 = 1650

final salary = first hike + hike 2 = 33000+1650 = 34650 -----final salary

Print final salary
"""


salary = 30000
salary_hike1 = 30000 * 0.1   #10% = 10/100 = 1/10 = 0.1
updated_salary = salary_hike1 + salary

salary_hike2 = updated_salary * 0.05
final_salary = updated_salary + salary_hike2

print(f"The final salary after all hikes is:{final_salary}")


# 12. variable reference 
"""
a = 10
b = a
a = 20
print(a)   expected  : 20
print(b)   expected :10

predict the output
"""
a = 10
b = a
a = 20
print(a)  #20  
print(b) #10


"""
reason:
step by step analysis

1.A variable a is assigned the value 10.
2.The current value of a (which is 10) is assigned to b.
3.Both variables now refer to the integer object 10
4.This does not change the value of 10.
Instead, a is reassigned to a different integer object, 20

Since integers are immutable (their value cannot be changed),
Python creates or reuses the integer 20 and makes a point to it. b continues to point to 10

because b still refers to 10.
"""












