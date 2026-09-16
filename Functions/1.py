# Online Food Ordering System

def calculate_bill(item_prices, quantity):
    total = sum(item_prices) * quantity

    if total >= 500:
        discount = total * 0.10
    elif total >= 300:
        discount = total * 0.05
    else:
        discount = 0

    final_amount = total - discount
    return total, discount, final_amount


def display_order(name, item, quantity, prices):
    total, discount, final_amount = calculate_bill(prices, quantity)

    print("\n----- ORDER SUMMARY -----")
    print("Customer :", name)
    print("Item     :", item)
    print("Quantity :", quantity)
    print("Total    : ₹", total)
    print("Discount : ₹", discount)
    print("Final Bill: ₹", final_amount)

    if final_amount >= 500:
        print("Status   : Free Delivery")
    else:
        print("Status   : Delivery Charge Applicable")


# Main program
name = input("Enter your name: ")

menu = ["Pizza", "Burger", "Biryani"]
prices = [250, 150, 300]

print("\n----- MENU -----")
for i in range(len(menu)):
    print(i + 1, menu[i], "₹", prices[i])

choice = int(input("Choose an item (1-3): "))
quantity = int(input("Enter quantity: "))

if choice >= 1 and choice <= 3 and quantity > 0:
    item = menu[choice - 1]
    price = prices[choice - 1]

    # Create a list containing the price for each ordered item
    ordered_prices = [price]

    display_order(name, item, quantity, ordered_prices)
else:
    print("Invalid order!")