
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# print(thisdict["model"]) #Mustang
# print(len(thisdict)) #3
# print(type(thisdict)) #<class 'dict'>



# mydict = dict(name = "John", age = 36, country = "Norway")
# print(mydict) #{'name': 'John', 'age': 36, 'country': 'Norway'}



#accessing items
x = thisdict["brand"]


#to get list of keys
x = thisdict.keys()
y = thisdict.values()
z = thisdict.items()


#Check if "model" is present in the dictionary:

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#change values
thisdict["year"] = 2018
print(thisdict)


#Update the "year" of the car by using the update() method
thisdict.update({"year": 2020})
print(thisdict)

#update dictionary
thisdict.update({"color": "red"})
print(thisdict)

#remove dictionary
thisdict.pop("model")
print(thisdict)



#looping dict
for x in thisdict:
  print(x)

#copy dict
mydict = thisdict.copy()
print(mydict)








