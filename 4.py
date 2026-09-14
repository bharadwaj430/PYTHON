def calculate_discount(price: float, discount_percent: float = 10.0) -> tuple[float, float]:
    """Calculate the final price and the total amount saved."""
    savings = price * (discount_percent / 100)
    final_price = price - savings
    return final_price, savings


# Call using default discount (10%)
total, saved = calculate_discount(120.0)
print(f"Paid: ${total:.2f}, Saved: ${saved:.2f}")
# Output: Paid: $108.00, Saved: $12.00

# Call using keyword arguments and custom discount
total, saved = calculate_discount(price=200.0, discount_percent=25)
print(f"Paid: ${total:.2f}, Saved: ${saved:.2f}")
# Output: Paid: $150.00, Saved: $50.00