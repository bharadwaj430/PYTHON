from datetime import date, timedelta

# Smart Fridge Expiry Tracker

fridge = [
    {"name": "Milk", "expiry": "2026-10-02", "quantity": 1},
    {"name": "Eggs", "expiry": "2026-10-05", "quantity": 6},
    {"name": "Spinach", "expiry": "2026-10-01", "quantity": 2},
    {"name": "Cheese", "expiry": "2026-10-10", "quantity": 1},
    {"name": "Yogurt", "expiry": "2026-10-03", "quantity": 3}
]


def check_expiry(item):
    expiry_date = date.fromisoformat(item["expiry"])
    today = date.today()
    days_left = (expiry_date - today).days

    if days_left < 0:
        return "EXPIRED"
    elif days_left == 0:
        return "EXPIRES TODAY"
    elif days_left <= 3:
        return f"EXPIRING SOON ({days_left} days left)"
    else:
        return f"FRESH ({days_left} days left)"


def display_fridge():
    print("\n====== SMART FRIDGE REPORT ======")

    for item in fridge:
        status = check_expiry(item)

        print(f"\nFood: {item['name']}")
        print(f"Quantity: {item['quantity']}")
        print(f"Expiry: {item['expiry']}")
        print(f"Status: {status}")


def recommend_food():
    today = date.today()

    # Find food expiring within the next 3 days
    urgent_items = []

    for item in fridge:
        expiry_date = date.fromisoformat(item["expiry"])
        days_left = (expiry_date - today).days

        if 0 <= days_left <= 3:
            urgent_items.append(item)

    # Recommend the food expiring first
    urgent_items.sort(key=lambda item: item["expiry"])

    print("\n====== CONSUME THESE FIRST ======")

    if urgent_items:
        for item in urgent_items:
            print(f"-> {item['name']} (Expires: {item['expiry']})")
    else:
        print("No urgent items. Your fridge is looking good!")


def main():
    display_fridge()
    recommend_food()


main()