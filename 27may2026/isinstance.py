#unchecked topic 1

"""

isinstance().py
#ex var string assigned to it
"""
account_balance = 4.5

#when we try to do mathematical expression like division by  using account_balance 
#we recieve an error message

#to check whether account_balance is integer
#we use isinstance() fn like this

isinstance(account_balance, int)  #false
print(type(account_balance))   #<class 'str'>

#isinstance - helps in variable matching to specific datatype
 #           - fn allows to check multiple types at once
 # ex checking account_balance is int or float

isinstance(account_balance, (int, float)) # True
print(type(account_balance)) 
# <class 'int'> if acc bal = 12 i.e if int val     
#<class 'float'> if acc bal = 4.5 i.e decimal val






















