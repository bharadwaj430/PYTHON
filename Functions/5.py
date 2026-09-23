# Smart Grocery Billing System

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: ₹"))
    quantity = int(input("Enter quantity: "))

    return {
        "name": name,
        "price": price,
        "quantity": quantity,
        "total": price * quantity
    }


def calculate_bill(items):
    subtotal = 0

    for item in items:
        subtotal += item["total"]

    # Discount
    if subtotal >= 2000:
        discount = subtotal * 0.10
    elif subtotal >= 1000:
        discount = subtotal * 0.05
    else:
        discount = 0

    # GST after discount
    taxable_amount = subtotal - discount
    gst = taxable_amount * 0.05

    final_amount = taxable_amount + gst

    return subtotal, discount, gst, final_amount


# Main program
items = []

print("================================")
print("     SMART GROCERY BILLING")
print("================================")

while True:
    choice = input("\nDo you want to add an item? (yes/no): ").lower()

    if choice == "yes":
        item = add_item()
        items.append(item)
        print(f"{item['name']} added successfully!")

    elif choice == "no":
        break

    else:
        print("Please enter yes or no.")


# Generate bill
if len(items) == 0:
    print("\nNo items purchased.")

else:
    subtotal, discount, gst, final_amount = calculate_bill(items)

    print("\n================================")
    print("           FINAL BILL")
    print("================================")

    for item in items:
        print(
            f"{item['name']} - "
            f"₹{item['price']} × {item['quantity']} = "
            f"₹{item['total']:.2f}"
        )

    print("--------------------------------")
    print(f"Subtotal       : ₹{subtotal:.2f}")
    print(f"Discount       : ₹{discount:.2f}")
    print(f"GST (5%)       : ₹{gst:.2f}")
    print("--------------------------------")
    print(f"FINAL AMOUNT   : ₹{final_amount:.2f}")
    print("================================")
    print("       Thank you for shopping!")
    print("================================")