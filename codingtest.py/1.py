# #1 Print Hello World without using a variable

print("Hello World")

# #2 Swap two numbers without a third variable
a = 3
b = 4
temp = a
a = b
b = temp
print(a)
print(b)

# #3 . Check whether a number is positive, negative or zero.
a = int(input("enter a number:"))
if a > 0 :
  print("it is a positive number")
if a ==0:
  print("it is zero")
if a < 0 :
  print("it is negative number")


#4  Find the largest of three numbers
d = int(input("enter the first  number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

print(f"the largest of three numbers is:{max(d,b,c)}")


#5 . Check whether a number is even or odd.
num = int(input("enter a number:"))
if num % 2 == 0 :
  print("the number is even")
if num % 2 != 0 :
  print("the number is odd")


# 6.Calculate factorial.
number = int(input("enter the number:"))
fact = 1
for i in range(1,number+1):
  fact = fact* i
print("factorial of give no is:",fact)

#7 Check whether a number is prime
num = int(input("enter a no:"))
for i in range(2,num):
  if num % i == 0 :
    print("number is not a prime number")
  else:
    print("it is a prime number")

#8 Count words in a sentence.

line = input("enter a line:")
words = line.split()
print(len(words))

#9  reverse a string
txt = input("enter a str:")
rev = " "
for char in txt:
  rev = char + rev
  print(rev)

#10 remove duplicates from string
txt = input("enter a string:")
res = " "
for char in txt :
  if char not in res:
    res = res + char
    print("the final result after removing duplicates:",res)


#11 merge two dictionaries
dic1 = {"name":"bharadwaj","course":"b.tech"}
dic2 = {"intern":"consistency.ai","college":"bhaskar engineering college"}

merge_dic = dic1.copy()
for key,value in dic2.items():
  merge_dic[key] = value
print("the final merged dict" , merge_dic)

#12 find common keys between dictionaries
dict = {"name":"bharadwaj","age":20,"hometown":"hyderabad"}
dict1 = {"branch":"information tech", "age":20,"hometown":"hyderabad"}

comm_keys = []

for keys in dict:
  if keys in dict1:
    comm_keys.append(keys)

print("the common keys b/w dictionaries are:",comm_keys)



#13 invert a dict

original = {
  "name":"bharadwaj",
  "course":"B.tech",
  "branch":"IT"

}


inverted = {}

for key,value in original.items():
  inverted[value] = key
  print("the before inverted:",original)
  print("after inverted:", inverted)


#14 commom elements between two lists
list1 = list(map(int,input("enter first list:"))).split()
list2 = list(map(int,input("enter second list:"))).split()
common = []
for num in list1 :
  if num in list2 and num not in common:
    common.append(num)
    print("common elements:",common)

























































































































