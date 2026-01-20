expenses = []

def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                expenses.append({
                    "name": name,
                    "amount": float(amount)
                })
    except FileNotFoundError:
        pass

def save_expenses():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['name']},{expense['amount']}\n")

def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total")
    print("4. Exit")

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    expenses.append({"name": name, "amount": amount})
    save_expenses()
    print("Expense added.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\n--- Expense List ---")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['name']} - {expense['amount']}")

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
        view_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

