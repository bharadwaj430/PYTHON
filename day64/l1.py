"""
Write a generator function count_up(n) that 
yields numbers from 0 to n‑1, 
one at a time when iterated.
"""
def num5():
    yield 0
    yield 1
    yield 2
    yield 3
    yield 4
for i in num5():
  print(i)
