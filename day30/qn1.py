#arranging string characters such that lowercase letters should come first, 
# then uppercase letters, and then digits.

string_1 = "GFGnpci123"
print("Original String: ", string_1)
lowercase = []
uppercase = []
digits = []
for char in string_1:
    if char.islower():
        lowercase.append(char)
    else :
        uppercase.append(char)
result = lowercase + uppercase + digits
print("Rearranged String: ", ''.join(result))