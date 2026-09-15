def calculate_discount(price: float, discount_percent: float = 10.0) -> float:
    """Calculate the final price after applying a percentage discount."""
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be between 0 and 100.")

    discount_amount = price * (discount_percent / 100)
    return round(price - discount_amount, 2)


# Function calls
print(calculate_discount(100.0))        # Uses default 10% -> 90.0
print(calculate_discount(50.0, 20.0))   # Overrides default with 20% -> 40.0