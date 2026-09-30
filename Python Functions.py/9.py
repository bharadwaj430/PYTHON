# Daily Expense Tracker

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")

    for expense in expenses:
        print(f"{expense['name']}: ₹{expense['amount']:.2f}")


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal expenses: ₹{total:.2f}")


def check_budget():
    budget = float(input("Enter your daily budget: "))

    total = sum(expense["amount"] for expense in expenses)
    balance = budget - total

    print(f"Budget: ₹{budget:.2f}")
    print(f"Spent: ₹{total:.2f}")

    if balance > 0:
        print(f"Money left: ₹{balance:.2f}")
    elif balance == 0:
        print("You have used your entire budget!")
    else:
        print(f"Budget exceeded by: ₹{abs(balance):.2f}")


# Main program
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Check Budget")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        check_budget()
    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Try again.")