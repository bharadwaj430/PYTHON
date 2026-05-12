"""
dict = collection of data values , to store info as map
unsimilar to other datatypes, dictionary have  - key value pairs
each key map to a value
benefits- 1.efficient access ,
2. retrieval of data

each val seperated by colon  (:)
multiple pairs seperated  by (,)


CREATE DICT IN PYTHON 
can be any datatype.
can be duplicated.
keys can't be repeated
must be immutable

dictionary created by built in fn dict()

note : case sensitive , same name but diff cases can treat distinctly

"""


#program 
# initialize empty dictionary
d = {}

d = {1: 'bharadwaj', 2: 'is', 3: 'learning'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'bharadwaj', 2: 'is', 3: 'learning'})
print(d1)