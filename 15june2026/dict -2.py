# #we Can make a key as a floating value , bool or tuple ----value once assigned dont change
# #   Dictionaries   are mutable.
# # strings are only in dictionaries mostly as a beginner make sense
# #string , List and tuple have index in common.
# #  dictionarieshave no index, that's why it is unordered. 
# #list and dict are mutable
# #dict keys are not mutable


#common data
data = {
  "student name" : "bharadwaj",
    "college" : "bhaskar engg clg",
    "skill learning" : "consistency.ai",
       "age " : 20 ,
       "is_adult": True ,
       12.99 : 94.3



 }

print(data["student name"]) #bharadwaj
print(data["college"]) #bhaskar engg clg
print(data["skill learning"]) #consistency.ai

#key without exist comes error
#prgrm
data["name"] = "bharath",
data["surname"] = "marri",
print(data)



"""
 prgrm  ---o/p:
 {'student name': 'bharadwaj', 'college': 'bhaskar engg clg', 'skill learning': 'consistency.ai', 'age ': 20, 'is_adult': True, 12.99: 94.3, 
 'name': ('bharath',), 'surname': ('marri',)}












"""





