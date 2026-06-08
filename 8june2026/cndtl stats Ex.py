"""
grade students based on marks

marks >=90 - grade A 
90 > marks > = 80  -- grade B
80> marks > = 70 ---grade c
70> marks - grade D
"""
marks = int(input("enter student marks:"))

if(marks>=90):
  grade = "A"
elif(marks >= 80 and marks < 90):
  grade = "B"
elif(marks >= 70 and marks < 80):
  grade = "c"
else:
  grade = "D"
print("grade of the student ->",grade)




