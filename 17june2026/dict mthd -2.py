#my.Dict.values()  #return all values
student = {
      "name" :"bharadwaj",
      "subjects" : {
             "phy":97,
             "chem":98,
             "math" :95
           }

} 
#print(list(student.values())) #['bharadwaj', {'phy': 97, 'chem': 98, 'math': 95}]

print(list(student.items()))  #returns all (key,val)pairs as tuples
#o/p:[('name', 'bharadwaj'), ('subjects', {'phy': 97, 'chem': 98, 'math': 95})]



