student = {
      "name" :"bharadwaj",
      "subjects" : {
             "phy":97,
             "chem":98,
             "math" :95
           }

} 

pairs = list(student.items())
print(pairs[0]) #('name', 'bharadwaj')
print(pairs[1]) #('subjects', {'phy': 97, 'chem': 98, 'math': 95})



print(student["name"]) #bharadwaj   #if name2 given error is thrown
print(student.get("name"))  #bharadwaj  #no error-> None   if name2 is given instad of name
#prints the same output



#print("BEFORE")
#print(student["name2"]) #error
#print("AFTER")
#error thrown , then the next  after code won't execute

"""
the after never prints  because the name2 throws an error in solving the compilation time
and the code after the error will never be executed

"""




