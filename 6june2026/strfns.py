#string functions


#sub string is a small part of a string

#str.endswith() - returns true if string ends with substr
#if it ends  prints true or else prints false
str = "i am studying python from consistency ai"
print(str.endswith("ai")) #True
print(str.endswith("from")) #False


# str.capitalize - capitalizes 1st character
print(str.capitalize())  #I am studying python from consistency ai
#str . capitalize - creates new string with changes and the old string has no changes

#if we want old string modification 
str = str.capitalize()
print(str)  #I am studying python from consistency ai




# str.replace(old , new) -replace all occurences of old
print(str.replace("o", "a")) 


#we can replace a substring too
print((str.replace("python", "c language")))  #I am studying c language from consistency ai

#str.find(word) - returns 1st index of 1st occurrer
print(str.find("o")) #18 #"I am studying python fro" --- 18 INCLUDING SPACES




