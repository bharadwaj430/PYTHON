"""
Add two complex numbers 2 + 3j and 4 + 5j. Print the result.
Subtract 1 + 2j from 5 + 8j.
Multiply 3 + 2j and 1 + 4j. Print the result and verify manually using the formula (ac - bd) + (ad + bc)j.
Divide 10 + 5j by 2 + 1j. Print the result.
What happens when you try to use // (floor division) on complex numbers? Try (4 + 2j) // (1 + 1j) and note the error.
"""

# 1. Add two complex numbers  Print the result.
z1 = 2 + 3j
z2 = 4 + 5j
result_addition = z1 + z2
print("Addition result:", result_addition)

# 2. Subtract 1 + 2j from 5 + 8j.
z3 = 5 + 8j 
z4 = 1 + 2j
result_subtraction = z3 - z4
print("Subtraction result:", result_subtraction)

# 3. Multiply 3 + 2j and 1 + 4j. Print the result 
# verify manually using the formula (ac - bd) + (ad + bc)j.
z5 = 3 + 2j
z6 = 1 + 4j
result_multiplication = z5 * z6
print("Multiplication result:", result_multiplication)

# Manual verification:
# (3 + 2j) * (1 + 4j)
# ac - bd = (3 * 1) - (2 * 4) = 3 - 8 = -5
# ad + bc = (3 * 4) + (2 * 1) = 12 + 2 = 14
# So the result should be -5 + 14j, which matches the output.

# 4. Divide 10 + 5j by 2 + 1j. Print the result.
z7 = 10 + 5j
z8 = 2 + 1j
result_division = z7 / z8
print("Division result:", result_division)
"""
# 5. What happens when you try to use // (floor division) on complex numbers?
z9 = 4 + 2j
z10 = 1 + 1j  
result_floor_division = z9 // z10
print("Floor division result:", result_floor_division)
# This will raise a TypeError because floor division is not supported for complex numbers.
"""


