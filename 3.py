# Shopping Cart using Python Lists (Arrays)

cart = ["Laptop", "Mouse", "Keyboard"]

print("Items in cart:", cart)

# Add an item
cart.append("Headphones")

# Remove an item
cart.remove("Mouse")

# Update an item
cart[1] = "Mechanical Keyboard"

# Display all items
print("\nUpdated Cart:")

for item in cart:
    print("-", item)

# Check if an item exists
if "Laptop" in cart:
    print("\nLaptop is in your cart.")

# Number of items
print("Total items:", len(cart))