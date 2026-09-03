def check_balance(balance):
    print(f"💰 Current Balance: ₹{balance}")


def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"✅ ₹{amount} deposited successfully!")
    else:
        print("❌ Invalid amount!")
    return balance


def withdraw(balance, amount):
    if amount <= 0:
        print("❌ Invalid amount!")
    elif amount > balance:
        print("❌ Insufficient balance!")
    else:
        balance -= amount
        print(f"✅ ₹{amount} withdrawn successfully!")
    return balance


def atm():
    balance = 5000

    while True:
        print("\n--- SMART ATM ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount: ₹"))
            balance = deposit(balance, amount)

        elif choice == "3":
            amount = int(input("Enter withdrawal amount: ₹"))
            balance = withdraw(balance, amount)

        elif choice == "4":
            print("👋 Thank you for using Smart ATM!")
            break

        else:
            print("❌ Invalid choice!")


atm()