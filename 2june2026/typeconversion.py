#types of conversion
#1.type conversion - interpretors do automatically
#type casting - manual conversion


#type conversion
a = 2
b = 4.25 #float is superior to int
          #4.25 + 2 = 6.25
print(sum) #<built-in function sum>
print(type(a)) # <class 'int'>


#typecasting
#prblm 1
d  = int("2") #typecasting string
e = 4.25
print(d + e)  #6.25

#prblm 2
f = float("2")
g = 3.25
print(f + g) #5.25

#character value cannot be converted to floating value
#success only when exisitng datatype fits to new datatype
a = 3.14
a = str(a)

print(type(a)) #class 'str'>
