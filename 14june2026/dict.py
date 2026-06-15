"""
dictionary in python
dictionaries are used to store data values in key:value pairs
they are unordered , mutable(changeable) & don't allow duplicate keys

dict  = {
"name" : "shradha"
"cgpa" : 9.6,
"marks " : [98,97,95]
}

dict ["name"],dict["cgpa"],dict["marks"]
dict["key"] = "value"  #to assign or add new
"""

info = {
    "key" : "value",
    "subjects" : ["python","c","c++","java"] ,
    "name" :"consistency.ai",
    "learning" : "python coding",
    "age" : 35 ,
    "is_adult":True,
    "marks" : 94.4
}
print(info)
"""
output:
{'key': 'value', 
'subjects': ['python', 'c', 'c++', 'java'], 
'name': 'consistency.ai', 
'learning': 'python coding', 
'age': 35, 'is_adult': True, 
'marks': 94.4
}
"""