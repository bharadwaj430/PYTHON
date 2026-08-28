def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    total = calculate_total(marks)
    return total / len(marks)


def check_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


# Student marks
marks = [78, 85, 69, 92, 74]

total = calculate_total(marks)
average = calculate_average(marks)
result = check_result(average)

print("Total Marks:", total)
print("Average Marks:", average)
print("Result:", result)