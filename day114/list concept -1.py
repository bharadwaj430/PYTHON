#change list items

#change item value
#to change the specific item,refer to index number
ihavelist = ["student","worker","professor","principal"]
ihavelist[1] = "scavenger"
print(f"the updated list is {ihavelist}")

"""
o/p:the updated list is ['student', 'scavenger', 'professor', 'principal']

"""

#change a range of item values

ihavelist[0:3] =[ "undergrad" ,"cleaners","lecturer" ]
print(f"list with change in item values {ihavelist}")

# output : list with change in item values ['undergrad', 'cleaners', 'lecturer', 'principal']


#If you insert less items than you replace, the new items will be inserted where you specified, 
#and the remaining items will move accordingly:
ihavelist[0:3] = ["sportsmen"]
print(f"sending less items than we replace{ihavelist}")

"""
output :
sending less items than we replace['sportsmen', 'principal']
"""





