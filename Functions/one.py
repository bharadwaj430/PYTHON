# Python Functions Example

def calculate_total(price, quantity):
    total = price * quantity
    return total


def display_bill(item, price, quantity):
    total = calculate_total(price, quantity)
    print("Item:", item)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)


# Function call
display_bill("Laptop", 50000, 2)