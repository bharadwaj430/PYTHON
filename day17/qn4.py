#conjugate and absolute value of a complex number
z = 3 + 4j
print(z.conjugate()) 
print(abs(z))

# Manual verification: sqrt(3² + 4²) = sqrt(9 + 16) = sqrt(25) = 5
import math
print(math.sqrt(z.real**2 + z.imag**2))  

z1 = 0 + 5j
z2 = 5 + 0j
print(abs(z1)) 
print(abs(z2))