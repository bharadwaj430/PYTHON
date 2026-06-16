#creating an empty dictionary
null_dict ={}
null_dict["name"] = "consistency.ai"
print(null_dict)  #{'name': 'consistency.ai'}


#nested dictionaries
#make a value as a dictionary
student = {
"name" : "mohan",
"subjects": {
      "phy": 97,
      "chem": 95,
      "math":85
   }
}
print(student)#-{'name': 'mohan', 'subjects': {'phy': 97, 'chem': 95, 'math': 85}}
print(student["subjects"]["chem"]) #95
#nested dict acquiring format
