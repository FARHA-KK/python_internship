import json
from datetime import datetime


def log_call(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write(
                f"{datetime.now()} - {func.__name__} - Args:{args} {kwargs}\n"
            )
        return func(*args, **kwargs)

    return wrapper


def load_expenses() -> list:
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses: list) -> None:
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)


@log_call
def add_expense(category: str, amount: float) -> None:
    expenses = load_expenses()

    expenses.append(
        {
            "category": category,
            "amount": amount
        }
    )

    save_expenses(expenses)

    print("Expense added successfully.")


@log_call
def get_summary() -> dict:
    expenses = load_expenses()

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        summary[category] = summary.get(category, 0) + amount

    return summary


@log_call
def view_all() -> None:
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f"Category: {expense['category']}, Amount: {expense['amount']}"
        )


def read_logs() -> None:
    counts = {}

    try:
        with open("log.txt", "r") as f:
            for line in f:
                parts = line.split(" - ")

                if len(parts) >= 2:
                    function_name = parts[1]

                    counts[function_name] = (
                        counts.get(function_name, 0) + 1
                    )

        print("\nFunction Call Counts:")

        for func, count in counts.items():
            print(f"{func}: {count}")

    except FileNotFoundError:
        print("No logs found.")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Summary")
    print("3. View All Expenses")
    print("4. Read Logs")
    print("5. Exit")

    choice: str = input("Enter your choice: ")

    if choice == "1":
        category: str = input("Enter category: ")
        amount: float = float(input("Enter amount: "))
        add_expense(category, amount)

    elif choice == "2":
        summary: dict = get_summary()

        if not summary:
            print("No expenses found.")
        else:
            print("\nExpense Summary:")
            for category, total in summary.items():
                print(f"{category}: {total}")

    elif choice == "3":
        view_all()

    elif choice == "4":
        read_logs()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")