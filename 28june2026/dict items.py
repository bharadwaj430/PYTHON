#dictionary items

"""
dictionary items are ordered,changeable , do not allow duplicates

dictionary items are in key:value pairs, refeered using the key name

"""
dictionary = {
  "brand" : "royal enfield",
  "model" : "hunter 350",
  "year" : "1995"
}


print(dictionary["brand"]) #royal enfield
print(dictionary["year"]) #1995
print(dictionary["model"])#hunter 350


#dict are ordered -----------items in defined order------i.e order dont change
#unordered means ---- items do not have defined order---cant refer to an item using index

#DUPLICATES ARE NOT ALLOWED
#cannot have two items with same key

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 #over writes existing value
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}