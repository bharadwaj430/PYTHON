#local variable
def greet():
  message = "hey! How are you doing?"
  print(message)
greet()

#diff between local and global variable
x = 10  # Global variable

def func():
    x = 5   # Local variable
    print("Inside:", x)

func()
print("Outside:", x)


"""
Output:
hey! How are you doing?
Inside: 5
Outside: 10
"""