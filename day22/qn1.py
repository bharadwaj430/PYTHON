#looping through a string
s = "Hello World"
for i in s:
    print(i)

#string length
s = "Hello World"
print(len(s))

#check string
txt = "The best things in life are free!"
print("free" in txt)


#use if statement to check if "free" is present in the stringtxt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")  
#check if not present
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
    