"""
SIMULATION
Simulation- imitating a process step by step exactly as described.
Many coding interview questions are simulation problems.
"""
# a robot starting at position zero
#conditions given
#R → move right (+1)
#L → move left (-1)

position = 0

commands = ["R", "R", "L", "R"]

for cmd in commands:
    if cmd == "R":
        position += 1
    else:
        position -= 1

print(position) #2

#the connectivity of problems
#level 1.arrays
#level 2.matrices
#level 3.simulation


