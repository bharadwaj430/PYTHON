"""
Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
"""
def create_new_string(s1, s2):
    # Get the first, middle, and last characters of s1
    first_s1 = s1[0]
    middle_s1 = s1[len(s1) // 2]
    last_s1 = s1[-1]

    # Get the first, middle, and last characters of s2
    first_s2 = s2[0]
    middle_s2 = s2[len(s2) // 2]
    last_s2 = s2[-1]

    # Combine the characters to create the new string
    new_string = first_s1 + middle_s1 + last_s1 + first_s2 + middle_s2 + last_s2

    return new_string
# Example usage
s1 = "computer science"  
s2 = "artificial intelligence"
result = create_new_string(s1, s2)
print(result)