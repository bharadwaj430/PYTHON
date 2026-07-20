"""
problem
clear sensor data

data = [25, None, 31, None, 18, 20, None]
return
[25,None,31,None,18,20,None]
"""

data = [25, None, 31, None, 18, 20, None]

data.remove(None)
data.remove(None)
data.remove(None)

print(data) #[25, 31, 18, 20]






