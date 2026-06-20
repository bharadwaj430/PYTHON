#add items
#once a set is created you cannot chnage its items, but you can add new items

#to add one item to a set use the add() method

have_set = {"tomato","brinjal","bottlegourd"}
have_set.add("pumpkin")
print(have_set) #{'tomato', 'bottlegourd', 'pumpkin', 'brinjal'}

#add sets 
#to add items from other set into current set , we use update() method

fruits = {"apple","pineapple","mango"}
leaf_veggies = {"moringa", "coriander","lettuce"}
fruits.update(leaf_veggies)
print(fruits)

