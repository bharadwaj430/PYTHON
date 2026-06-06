#accessing parts of string
#str[starting index : ending index]
#starting index is included
#ending index is not included i.e excluded

str = "consistencyai "
#slicing - breaking of string pieces
print(str[1:4]) #ons
print(str[0:3]) #con


#if we need only .ai
print(str[11:13])  #ai
#string length = last index + 1
print(str[5:len(str)]) #stencyai


#missed slice no = automatic default 0 by python
print(str[:11])





