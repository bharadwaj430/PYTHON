price1 = float(input("price of product 1:"))
price2 = float(input("price of product 2: "))
price3 = float(input("price of product 3: "))
price4 = float(input("price of product 4: "))
price5 = float(input("price of product 5: "))

total_price = price1 + price2 + price3 +  price4 + price5
average_of_prices = total_price / 5


print("\n --------Shopping Bill--------")
print("total price of products:",total_price)
print("average of prices of products:", average_of_prices)


"""
output:

price of product 1:450
price of product 2: 360
price of product 3: 900
price of product 4: 1200
price of product 5: 2000

 --------Shopping Bill--------
total price of products: 4910.0
average of prices of products: 982.0
"""

