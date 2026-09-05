# Food Ordering System using Functions

menu = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 180,
    "Coffee": 100
}

def display_menu():
    print("\n----- MENU -----")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")


def calculate_bill(order):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total


def apply_discount(total):
    if total >= 500:
        return total * 0.90       # 10% discount
    return total


def place_order():
    order = {}

    while True:
        item = input("\nEnter item (or 'done' to finish): ").title()

        if item == "Done":
            break

        if item not in menu:
            print("Item not available!")
            continue

        quantity = int(input("Enter quantity: "))
        order[item] = order.get(item, 0) + quantity

    return order


# Main program
display_menu()

order = place_order()

if order:
    bill = calculate_bill(order)
    final_bill = apply_discount(bill)

    print("\n----- BILL -----")
    for item, quantity in order.items():
        print(f"{item} x {quantity} = ₹{menu[item] * quantity}")

    print(f"Original Bill : ₹{bill:.2f}")
    print(f"Final Bill    : ₹{final_bill:.2f}")

    if bill >= 500:
        print("10% discount applied!")
else:
    print("No items ordered.")