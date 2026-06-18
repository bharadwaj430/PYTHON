student = {
      "name" :"bharadwaj",
      "subjects" : {
             "phy":97,
             "chem":98,
             "math" :95
           }

} 

student.update({"city":"delhi"})
print(student)  #{'name': 'bharadwaj', 'subjects': {'phy': 97, 'chem': 98, 'math': 95}, 'city': 'delhi'}

#city name is added in the existing dictionary

#or


new_dict = {"city":"delhi","age":16}
student.update(new_dict)
print(student) #{'name': 'bharadwaj', 'subjects': {'phy': 97, 'chem': 98, 'math': 95}, 'city': 'delhi', 'age':16}


#Dictionaries don't allow duplicate keys. 

new_dict1 = {"name":"munna"}
student.update(new_dict1)
new_dict2 = {"subjects":"sociology"}
student.update(new_dict2)
print(student)  #{'name': 'munna', 'subjects': 'sociology', 'city': 'delhi', 'age': 16}

