"""
Seconds to Minutes Converter
Goal: Practice multi-step math and variable updates.

The Scenario: You have a timer that ran for 385 seconds.

The Task: 1. Create a variable total_seconds = 385.
2. Calculate how many whole minutes are in those seconds.
3. Calculate the remaining seconds after those minutes are taken out.
4. Print the result in a format like: 6 minutes and 25 seconds.
"""
#code
total_seconds = 385
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
print("time taken:")
print(minutes, "minutes and", remaining_seconds, "seconds")

#output : 6 minutes and 25 seconds