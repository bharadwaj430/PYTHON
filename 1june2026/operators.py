#logical operators
#it is a symbol that performs a certain operations between operand
#1.NOT , AND ,OR


a = 50
b = 30


print(not False) #True 
print(not True) #False
print(not (a > b))   #False


value1 = True
value2 = False
print("AND  operators:", value1 and value2)   #False
print("OR  operators condition 1:", value1 or value2)  #True
print("OR operator condition 2:", (a == b) or value2)  #False 
print("OR operator condition 3:", (a == b) or (a > b )) #True
print("NOT operator:" ,  not value2 ) #True

