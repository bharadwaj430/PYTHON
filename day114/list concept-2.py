#insert items

#to insert new list item ,without replacing any of the existing values,we use
#insert()  method-----The insert() method inserts an item at the specified index:

cars = ["porsche","benz",'BMW',"Audi","benz"]
cars.insert(1,"tata sierra")
print(f"the total list is:{cars}")#the total list is:['porsche', 'tata sierra', 'benz', 'BMW', 'Audi', 'benz']


#ADD LIST ITEMS

#append items
cars.append("volkswagen")
print(f"added an element to existing list:{cars}")  #added an element to existing list:['porsche', 'tata sierra', 'benz', 'BMW', 'Audi', 'benz', 'volkswagen']


#The extend() method does not have to append lists,
#you can add any iterable object (tuples, sets, dictionaries etc.).
bikes = ["splendor","platina","glamour"]
cars.extend(bikes)
print(f"the combination of bikes and cars is : {cars}") #the combination of bikes and cars is ['porsche', 'tata sierra', 'benz', 'BMW', 'Audi', 'benz', 'volkswagen', 'splendor', 'platina', 'glamour']


#remove specified item 
cars.remove("benz")
print(cars) #['porsche', 'tata sierra', 'BMW', 'Audi', 'benz', 'volkswagen', 'splendor', 'platina', 'glamour']



#remove specified index
#remove second item 
print(bikes.pop(0)) #splendor


#del keyword
del cars[4]
print(f"deleting the item benz from list:{cars}")


#CLEAR THE LIST
bikes.clear()
print(f"returning list with empty list elements:{bikes}")












