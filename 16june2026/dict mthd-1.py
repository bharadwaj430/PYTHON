#dict methods

# mydict.keys() #return all keys


student = {
      "name" :"bharadwaj",
      "subjects" : {
             "phy":97,
             "chem":98,
             "math" :95
           }

} 
print(list(student.keys()) )#type cast similar to float(9)
#output :['name', 'subjects']

print(len(student))
#or

print(len(list(student.keys())))



