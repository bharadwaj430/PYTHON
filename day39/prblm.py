#Remove empty strings from a list of strings
str_list = ["bharath", "Mohan", "", "chaitanya", None, "madhu", ""]
res_list = []
for s in str_list:
    # check for non empty string
    if s:
        res_list.append(s)
print(res_list)