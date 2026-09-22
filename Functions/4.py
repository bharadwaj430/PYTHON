# Online Shopping Bill Generator

def calculate_bill(cart):
    total = 0

    print("----- SHOPPING BILL -----")

    for item, details in cart.items():
        price = details["price"]
        quantity = details["quantity"]

        item_total = price * quantity
        total += item_total

        print(f"{item} x {quantity} = ₹{item_total}")

    # Discount
    if total >= 5000:
        discount = total * 0.20
    elif total >= 2000:
        discount = total * 0.10
    else:
        discount = 0

    # Delivery charge
    if total >= 1000:
        delivery = 0
    else:
        delivery = 50

    final_amount = total - discount + delivery

    print("-------------------------")
    print(f"Subtotal       : ₹{total:.2f}")
    print(f"Discount       : ₹{discount:.2f}")
    print(f"Delivery       : ₹{delivery:.2f}")
    print(f"Final Amount   : ₹{final_amount:.2f}")
    print("-------------------------")

    return final_amount


# Customer's shopping cart
cart = {
    "Laptop": {"price": 45000, "quantity": 1},
    "Mouse": {"price": 800, "quantity": 2},
    "Keyboard": {"price": 1500, "quantity": 1}
}

amount = calculate_bill(cart)

print(f"Amount to Pay: ₹{amount:.2f}")