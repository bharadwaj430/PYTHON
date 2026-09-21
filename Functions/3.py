def calculate_fare(distance, cab_type, waiting_time):
    # Base fare
    if cab_type == "mini":
        base_fare = 50
        per_km = 12
    elif cab_type == "sedan":
        base_fare = 80
        per_km = 16
    elif cab_type == "suv":
        base_fare = 120
        per_km = 20
    else:
        return "Invalid cab type"

    # Distance charge
    distance_charge = distance * per_km

    # Waiting charge
    waiting_charge = waiting_time * 2

    # Total fare
    total_fare = base_fare + distance_charge + waiting_charge

    # Apply discount
    if total_fare >= 500:
        discount = total_fare * 0.10
    else:
        discount = 0

    final_fare = total_fare - discount

    return final_fare


# Customer details
customers = [
    {"name": "Rahul", "distance": 12, "cab": "mini", "waiting": 5},
    {"name": "Priya", "distance": 25, "cab": "sedan", "waiting": 10},
    {"name": "Arjun", "distance": 8, "cab": "suv", "waiting": 2}
]

# Generate bills
for customer in customers:
    fare = calculate_fare(
        customer["distance"],
        customer["cab"],
        customer["waiting"]
    )

    print("Customer:", customer["name"])
    print("Cab Type:", customer["cab"])
    print("Distance:", customer["distance"], "km")
    print("Final Fare: ₹", fare)
    print("-" * 30)