# 📚 Library Management System

books = [
    {"name": "Python Basics", "author": "John Smith", "available": True},
    {"name": "AI Fundamentals", "author": "David Lee", "available": True},
    {"name": "Data Structures", "author": "Robert Martin", "available": True}
]


def display_books():
    print("\n========== LIBRARY BOOKS ==========")

    for book in books:
        if book["available"]:
            status = "Available"
        else:
            status = "Borrowed"

        print(book["name"], "-", book["author"], "-", status)


def borrow_book(book_name):
    for book in books:
        if book["name"].lower() == book_name.lower():

            if book["available"]:
                book["available"] = False
                print("\nBook borrowed successfully!")
            else:
                print("\nSorry, this book is already borrowed.")

            return

    print("\nBook not found.")


def return_book(book_name):
    for book in books:
        if book["name"].lower() == book_name.lower():

            if not book["available"]:
                book["available"] = True
                print("\nBook returned successfully!")
            else:
                print("\nThis book was not borrowed.")

            return

    print("\nBook not found.")


# Main Program

print("📚 Welcome to the Library!")

while True:

    print("\n1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_books()

    elif choice == "2":
        book_name = input("Enter the book name: ")
        borrow_book(book_name)

    elif choice == "3":
        book_name = input("Enter the book name: ")
        return_book(book_name)

    elif choice == "4":
        print("Thank you for using the library!")
        break

    else:
        print("Invalid choice. Try again.")