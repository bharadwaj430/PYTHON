#walrus operator ====> :=,
"""
name = input("")

if len(name)>5:
    print("name:", name)
"""

if (name:=input("enter ur name: ")) and (len(name)>5):
    print("name:", name)