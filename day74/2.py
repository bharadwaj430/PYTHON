#python datatypes
"""
'Numeric': int, float, complex
"Sequence Type": string, list, tuple
"Mapping Type": dict
"Boolean": bool
"Set Type": set, frozenset
"Binary Types": bytes, bytearray, memoryview"""


#sequence type = string , list , tuple
"""
A sequence is an ordered collection of items,
 which can be of similar or different data types

 string : array of bytes representing unicode characters
"""

s = 'ai engineering is in trending roles'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1]) # -1 refers to the last character, -2 is second last, and so on
