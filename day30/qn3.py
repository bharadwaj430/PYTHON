# Given string
text = "B@hkiaj$#1239"

# Initialize counters
letter_count = 0
digit_count = 0
special_count = 0

# Loop through each character
for char in text:
    if char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z':
        letter_count += 1
    elif char >= '0' and char <= '9':
        digit_count += 1
    else:
        special_count += 1

# Display results
print("String:", text)
print("Letters:", letter_count)
print("Digits:", digit_count)
print("Special Symbols (including spaces):", special_count)

"""
**Output:**
String: Hello, World! 123 @#$
Letters: 10
Digits: 3
Special Symbols (including spaces): 8
"""