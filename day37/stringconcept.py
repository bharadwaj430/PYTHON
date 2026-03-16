#deleting  a string
m = "startup requires hardwork and sacrifice"
b = "continuous learning"
del b
print(m)

#updating a string
#As strings are immutable, “updates” 
# create new strings using slicing or methods such as replace().
s = "hey guys"
s1 = "H" + s[1:]                  
s2 = s.replace("guys", "quick learners")  
print(s1)
print(s2)