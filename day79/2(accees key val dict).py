#access item in dict()
"""

step 1 : refer to key name
st 2 : keys used in square brackets
get() - we can access dict elements
"""

d = {1: 'python', 'name': 'needs', 3: 'practice'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(1)) #access  1st element
print(d.get(2)) #access not present element
print(d.get(3)) #access 3rd element
"""
#output :
needs
python
None
practice
"""