# \t - tag  escape sequence character ----leaves a tag or a space after a senetence
stringno_1 = "this is python code.\t executing code through compiler"
print(stringno_1)

#WE USE ESCAPE SEQUENCE CHARACTERS WHEN WE USE strings for  printing paragraphs


#concatenation: adding strings through + operator
str1 = "engineering"
str2 = "college"
print(str1+ str2) #engineeringcollege
finalstr = str1 + str2
print(finalstr) #engineeringcollege
finalized_string  = str1 +"  "+str2
print(finalized_string)  #engineering  college


#calculating string length

len1 = len(str1)
length2 = len(str2)
print(len1) #11
print(length2) #7
print(len(finalized_string)) #20
#length includes finalized string that has all the spaces and special characters as a length count


