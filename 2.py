# Simple Food Ordering System

print("=== FOOD ORDERING SYSTEM ===")

item = input("Enter food item (pizza/burger/biryani): ").lower()
quantity = int(input("Enter quantity: "))

# Decide price using match
match item:
    case "pizza":
        price = 250
    case "burger":
        price = 150
    case "biryani":
        price = 200
    case _:
        price = 0

# Check whether the item is valid
if price == 0:
    print("Sorry, this item is not available.")

else:
    total = price * quantity

    # Apply discount using if / elif / else
    if total >= 1000:
        discount = total * 0.20
    elif total >= 500:
        discount = total * 0.10
    else:
        discount = 0

    final_amount = total - discount

    print("\n--- ORDER SUMMARY ---")
    print("Item:", item)
    print("Quantity:", quantity)
    print("Price per item: ₹", price)
    print("Total: ₹", total)
    print("Discount: ₹", discount)
    print("Final Amount: ₹", final_amount)

    # Additional decision
    if final_amount >= 800:
        print("Free delivery!")
    else:
        print("Delivery charge: ₹50")