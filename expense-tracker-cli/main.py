import json
from datetime import date

expenses = []

def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

    except FileNotFoundError:
        pass

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Edit expense")
    print("5. View total")
    print("6. Exit")

def add_expense():
    name = input("Expense name: ").strip()
    amount = float(input("Amount: "))

    today = date.today().isoformat()

    expense = {
        "name" : name,
        "amount" : amount,
        "date" : today
    }
    expenses.append(expense)
    save_expenses()

    print("Expense added successfully.")

def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to delete: "))
        index = choice - 1

        if index < 0 or index >= len(expenses):
            print("Invalid expense number.")
            return

        deleted = expenses.pop(index)
        save_expenses()

        print(f"Deleted expense: {deleted['name']} - Rp {deleted['amount']}")

    except ValueError:
        print("Please enter a valid number.")

def edit_expense():
    if not expenses:
        print("No expenses to edit.")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to edit: "))
        index = choice - 1

        if index < 0 or index >= len(expenses):
            print("Invalid expense number.")
            return

        expense = expenses[index]

        print("\nPress Enter to keep current value")

        new_name = input(f"New name [{expense['name']}]: ").strip()
        new_amount = input(f"New amount [{expense['amount']}]: ").strip()
        new_date = input(f"New date [{expense['date']}]: ").strip()

        if new_name:
            expense['name'] = new_name

        if new_amount:
            expense['amount'] = float(new_amount)

        if new_date:
            expense['date'] = new_date

        save_expenses()
        print("Expense updated successfully!")

    except ValueError:
        print("Please enter valid numbers.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n=== Expense List ===")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} | {expense['name']} | Rp {expense['amount']}")

def view_total():
    total = sum(expense["amount"] for expense in expenses)
    print("\nTotal expense:", total)

load_expenses()

while True:
    show_menu()
    choice = input("Choose menu: ").strip()
   
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()    
    elif choice == "4":
        edit_expense()
    elif choice == "5":
        view_total()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

