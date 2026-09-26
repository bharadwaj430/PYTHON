# Student Expense Tracker

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: ₹"))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.\n")
    else:
        print("\n--- Your Expenses ---")

        for expense in expenses:
            print(f"{expense['name']} : ₹{expense['amount']:.2f}")

        print()


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total expenses: ₹{total:.2f}\n")


def check_budget():
    budget = float(input("Enter your monthly budget: ₹"))

    total = 0
    for expense in expenses:
        total += expense["amount"]

    remaining = budget - total

    print(f"Monthly budget: ₹{budget:.2f}")
    print(f"Total spent: ₹{total:.2f}")

    if remaining > 0:
        print(f"Money remaining: ₹{remaining:.2f}\n")
    elif remaining == 0:
        print("You have used your entire budget!\n")
    else:
        print(f"Budget exceeded by ₹{abs(remaining):.2f}\n")


def main():
    while True:
        print("===== STUDENT EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Check Budget")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            check_budget()
        elif choice == "5":
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.\n")


main()