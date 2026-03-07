#arranging string characters such that uppercase letters should come first, 
# then lowercase letters, and then digits.

string_1 = "npciGFG123"
print("Original String: ", string_1)
uppercase = []
lowercase = []
digits = []
for char in string_1:
    if char.isupper():
        uppercase.append(char)
    else :
        lowercase.append(char)
result = uppercase + lowercase + digits
print("Rearranged String: ", ''.join(result))