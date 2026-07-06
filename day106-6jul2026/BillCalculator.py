"""
BILL CALCULATOR
Input
Price
GST percentage

Calculate
GST amount
Final amount
"""
#inputs
price = float(input("enter the price:"))
GST_percentage = float(input("enter the percentage of tax:"))  


#formulas
GST_amount = (GST_percentage * price) / 100
final_amount = price + GST_amount


print("/n -----------Bill----------")
print("Price of the product:", price)
print("GST Percentage:",GST_percentage )
print("The GST amount is :",GST_amount)
print("The final amount i.e bill:",final_amount )


"""
enter the price:1000
enter the percentage of tax:5
/n -----------Bill----------
Price of the product: 1000.0
GST Percentage: 5.0
The GST amount is : 50.0
The final amount i.e bill: 1050.0
"""






