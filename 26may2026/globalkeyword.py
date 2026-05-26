#global keyword is used to modify a global variable
my_var = 10 #global variable
def change_var():
  global my_var #allows modification of a global variable
  my_var = 20
change_var()
print(my_var)  #my_var is now modified to globally 20