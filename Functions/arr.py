# Find the second largest number in an array

numbers = [25, 10, 45, 30, 60, 15]

largest = numbers[0]
second_largest = float('-inf')

for num in numbers[1:]:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Array:", numbers)
print("Largest:", largest)
print("Second Largest:", second_largest)