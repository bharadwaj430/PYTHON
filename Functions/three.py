# Real-Time Example: ATM System

balance = 10000


def check_balance():
    print("\nCurrent Balance: ₹", balance)


def deposit_money():
    global balance

    amount = int(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance += amount
        print("₹", amount, "deposited successfully.")
        print("Updated Balance: ₹", balance)
    else:
        print("Invalid amount.")


def withdraw_money():
    global balance

    amount = int(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance -= amount
        print("Please collect your cash.")
        print("₹", amount, "withdrawn successfully.")
        print("Remaining Balance: ₹", balance)


def atm_menu():
    while True:
        print("\n========== ATM ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("=========================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit_money()

        elif choice == 3:
            withdraw_money()

        elif choice == 4:
            print("\nThank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")


# Main program

print("Welcome to ABC Bank ATM")

pin = int(input("Enter your PIN: "))

if pin == 1234:
    print("Login successful!")
    atm_menu()
else:
    print("Incorrect PIN.")