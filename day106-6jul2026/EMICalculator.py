loan_amount  = float(input("enter the amount taken:"))
interest = float(input("the interest rate the loan given:"))
duration = float(input("no of months that the loan is took:"))

simple_interest = loan_amount *duration*interest /100
print("the simple interest  calculated is:")

total_payable_amount = loan_amount + simple_interest
print("the final amount to be paid:" , total_payable_amount)


