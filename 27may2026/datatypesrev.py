#prerequsites: datatypes in py : str,int,float
#build on programs need how to view type of variable
#example of var 
developer = 'Devin'
#to see what type of datatype it is we use type()
print(type(developer)) #<class 'str'>
# it means that developer is a string


#all the data types at a glance
my_integer_var = 1500       
print(type(my_integer_var))  # <class 'int'>

my_float_var = 43.56
print(type(my_float_var))  # <class 'float'>

my_string_var = 'bharadwaj'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'python', 3.4}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'bharadwaj', 'age':20}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'consistency.ai', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>