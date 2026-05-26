#GLOBAL SCOPE
#variables that are declared outside any fns or classes
#1.can be accessed from anywhere
#here my_var can be accessed from anywhere even not defined in fn
my_var = 100

def show_var():
  print(my_var)

show_var()#100
print(my_var) #100

#FOR LOCAL scoped variable defined inside a fn globally accessible
#we use global keyword
my_var_1 = 7

def show_variables():
  global my_var_2
  my_var_2 = 10
  print(my_var_1)
  print(my_var_2)
show_variables() #7 10

#my_var_2 is now a global variable and can be accessed anywhere in the program

print(my_var_2) # 10




