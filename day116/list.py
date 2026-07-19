fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#syntax : newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits if x != "apple"]
print(f"printing with a condition : {newlist}")#except apple all are printed because not equal to
#printing with a condition : ['banana', 'cherry', 'kiwi', 'mango']


#creating an iterable
#use range() function to create iterable---(list,tuple,set)

newlist = [x for x in range(10)]
print(f"using range to create an iterable: {newlist}")#using range to create an iterable: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


thislist = [x for x in range(10) if x < 5]
print(f"printing list with two conditions: {thislist}")#printing list with two conditions: [0, 1, 2, 3, 4]


#Set the values in the new list to upper case
newlist = [x.upper() for x in fruits]
print(f"the list with uppercase is: {newlist}")#the list with uppercase is: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print("setting any outcome we want: {newlist}") #setting any outcome we want: {newlist}

#Return "orange" instead of "banana"--------"Return the item if it is not banana, if it is banana return orange".
newlist = [x if x != "banana" else "orange" for x in fruits]








