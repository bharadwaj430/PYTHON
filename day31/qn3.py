#BASIC PROBLEM 
#non overlapping occurrences
s = "banana"
sub = "ana"

count = s.count(sub)
print(count)


 #Find all occurrences of a substring in a given string by ignoring the case
#overlapping occurrences
s = "hello World"
sub = "hello"

s_lower = s.lower()
sub_lower = sub.lower()

occurrences = []

for i in range(len(s_lower) - len(sub_lower) + 1): #string length - substring length + 1 11-5+1 = 7
    if s_lower[i:i+len(sub_lower)] == sub_lower:
        occurrences.append(i)

print(occurrences)
