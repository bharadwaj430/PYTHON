import sys
nums = []
prev = -1
for i in range(17):
  size = sys.getsizeof(nums)
if size != prev: # capacity jumped
  print(f"len={len(nums):>2} bytes={size}") #len= 0 bytes=56
prev = size
nums.append(i)
