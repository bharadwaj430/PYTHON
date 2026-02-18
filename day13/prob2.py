#BILL SPLITTER
total_bill = 1000
number_of_people = 4
#splitting the bill
rupees_per_person = total_bill // number_of_people
#left over change
leftover_rupees = total_bill % number_of_people
#print the results
print("Each person should pay: INR " + str(rupees_per_person))
print("Leftover change: INR " + str(leftover_rupees))