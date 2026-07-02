
"""
CURRENCY CONVERTER

Input amount in INR.

Convert into:

USD
EUR
GBP

Store exchange rates as variables.
"""


inr = float(input("enter the amount in Indian Rupees  /-"))

usd_rate = 85.50 #1 US Dollar = ₹85.50
eur_rate = 100.20 #1 Euro = ₹100.20
gbp_rate =117.80

usd = inr / usd_rate
eur = inr / eur_rate
gbp = inr / gbp_rate

print("\n-------- Currency Converter --------")
print(f"Indian Rupees : ₹{inr}")
print(f"US Dollars    : ${usd:.2f}")
print(f"Euros         : €{eur:.2f}")
print(f"British Pounds: £{gbp:.2f}") #:.2f --- returns 2 decimal(float) after point


