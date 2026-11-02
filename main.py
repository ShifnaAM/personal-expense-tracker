import math
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

# Keep the CSV path relative to this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
EXPENSES_FILE = os.path.join(DATA_DIR, "expenses.csv")
TEMP_FILE = os.path.join(DATA_DIR, "expenses_temp.csv")

FIELDNAMES = ["amount", "category", "date", "description"]

print("Welcome to Personal Expense Tracker!")

expenses = []
data_loaded = False


# Add a new expense
def add_expense():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if not math.isfinite(amount) or amount <= 0:
                print("Please enter a valid positive amount.")
            else:
                break   
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")

    while True:
        category = input("Enter category: ").strip()

        if category and category.lower() != "null":
            break

        print("Category cannot be empty or 'null'.")

    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date! Use YYYY-MM-DD.")

    while True:
        description = input("Enter description: ").strip()

        if description and description.lower() != "null":
            break

        print("Description cannot be empty or 'null'.")

    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    expenses.append(expense)

    print("\nExpense added successfully!")


# View all recorded expenses
def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n------ All Expenses ------")

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print(f"Amount: ₹{expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print(f"Date: {expense['date']}")
        print(f"Description: {expense['description']}")


# Generate expense reports
def generate_report():
    if not expenses:
        print("\nNo expenses available to generate reports.")
        return

    # Calculate total spending
    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)


    print("\n========== EXPENSE REPORT ==========")
    print(f"Total Amount Spent: ₹{total:.2f}")
    print(f"Average Expense: ₹{average:.2f}")

    # Calculate category-wise spending
    category_totals = {}
    # Calculate weekly spending
    weekly_totals = {}

    for item in expenses:
        date = datetime.strptime(item["date"], "%Y-%m-%d")
        year, week, day = date.isocalendar()

        week_key = f"{year}-Week {week}"

        weekly_totals[week_key] = (
        weekly_totals.get(week_key, 0) + item["amount"]
        )

    print("\nWeekly Spending:")

    for week, amount in weekly_totals.items():
        print(f"{week}: ₹{amount:.2f}")
        # Calculate monthly spending
    monthly_totals = {}

    for item in expenses:
        category = item["category"]
        month = item["date"][:7]

        category_totals[category] = (
            category_totals.get(category, 0) + item["amount"]
        )

        monthly_totals[month] = (
            monthly_totals.get(month, 0) + item["amount"]
        )

    print("\nCategory-wise Spending:")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")

    print("\nMonthly Spending:")

    for month, amount in monthly_totals.items():
        print(f"{month}: ₹{amount:.2f}")

    # Find the highest expense
    highest = max(expenses, key=lambda item: item["amount"])

    print("\nHighest Expense:")
    print(f"Amount: ₹{highest['amount']:.2f}")
    print(f"Category: {highest['category']}")
    print(f"Date: {highest['date']}")
    print(f"Description: {highest['description']}")


# Calculate category-wise expense totals
def get_category_totals():
    totals = {}

    for item in expenses:
        category = item["category"]

        totals[category] = (
            totals.get(category, 0) + item["amount"]
        )

    return totals


# Visualize category-wise expenses using a bar chart
def plot_category_expenses():
    if not expenses:
        print("\nNo expenses available to visualize.")
        return

    totals = get_category_totals()

    categories = list(totals.keys())
    amounts = list(totals.values())

    plt.figure(figsize=(8, 5))

    bars = plt.bar(categories, amounts)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"₹{height:.2f}",
            ha="center",
            va="bottom"
        )
    plt.title("Category-wise Expense Analysis")
    plt.xlabel("Expense Categories")
    plt.ylabel("Amount Spent (₹)")

    plt.tight_layout()
    plt.show()


# Visualize category-wise expenses using a pie chart
def plot_expense_pie_chart():
    if not expenses:
        print("\nNo expenses available to visualize.")
        return

    totals = get_category_totals()

    categories = list(totals.keys())
    amounts = list(totals.values())

    plt.figure(figsize=(7, 7))

    plt.pie(
        amounts,
        labels=categories,
        autopct=lambda percentage: f"{percentage:.1f}%\n₹{percentage * sum(amounts) / 100:.2f}",
        startangle=90
    )

    plt.title("Category-wise Expense Distribution")
    plt.axis("equal")

    plt.tight_layout()
    plt.show()

# Visualize weekly expenses using a bar chart
def plot_weekly_expenses():
    if not expenses:
        print("\nNo expenses available to visualize.")
        return

    weekly_totals = {}

    for item in expenses:
        date = datetime.strptime(item["date"], "%Y-%m-%d")
        year, week, day = date.isocalendar()

        week_key = f"{year}-Week {week}"

        weekly_totals[week_key] = (
            weekly_totals.get(week_key, 0) + item["amount"]
        )

    weeks = list(weekly_totals.keys())
    amounts = list(weekly_totals.values())

    plt.figure(figsize=(8, 5))

    bars = plt.bar(weeks, amounts)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"₹{height:.2f}",
            ha="center",
            va="bottom"
        )

    plt.title("Weekly Expense Analysis")
    plt.xlabel("Weeks")
    plt.ylabel("Amount Spent (₹)")

    plt.tight_layout()
    plt.show()

# Visualize monthly expenses using a bar chart
def plot_monthly_expenses():
    if not expenses:
        print("\nNo expenses available to visualize.")
        return

    monthly_totals = {}

    for item in expenses:
        date = datetime.strptime(item["date"], "%Y-%m-%d")
        month = date.strftime("%Y-%m")

        monthly_totals[month] = (
            monthly_totals.get(month, 0) + item["amount"]
        )

    months = list(monthly_totals.keys())
    amounts = list(monthly_totals.values())

    plt.figure(figsize=(8, 5))

    bars = plt.bar(months, amounts)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"₹{height:.2f}",
            ha="center",
            va="bottom"
        )

    plt.title("Monthly Expense Analysis")
    plt.xlabel("Months")
    plt.ylabel("Amount Spent (₹)")

    plt.tight_layout()
    plt.show()


# Save expenses to CSV file
def save_expenses():
    if not data_loaded:
        print("\nCannot save because expense data was not loaded successfully.")
        return
    try:
        os.makedirs(DATA_DIR, exist_ok=True)

        with open(
            TEMP_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=FIELDNAMES
            )

            writer.writeheader()
            writer.writerows(expenses)
        
        os.replace(TEMP_FILE, EXPENSES_FILE)

        print("\nExpenses saved successfully!")

    except (OSError, csv.Error) as error:
        print(f"\nError saving expenses: {error}")
        try:
            if os.path.exists(TEMP_FILE):
                os.remove(TEMP_FILE)
        except OSError:
            pass


# Load previously saved expenses
def load_expenses():
    global data_loaded
    
    if not os.path.exists(EXPENSES_FILE):
        print("No previous expense records found.")
        data_loaded = True
        return

    try:
        with open(
            EXPENSES_FILE,
            "r",
            newline="",
            encoding="utf-8-sig"
        ) as file:

            reader = csv.DictReader(file)

            # Validate CSV headers
            if not reader.fieldnames or not all(
                field in reader.fieldnames
                for field in FIELDNAMES
            ):
                print("Invalid CSV file format!")
                return
            
            loaded_count = 0
            loaded_expenses = []

            for row in reader:
                try:
                    amount = float(row["amount"])

                    category = row["category"].strip()
                    date_text = row["date"].strip()
                    description = row["description"].strip()

                    # Validate date
                    datetime.strptime(date_text, "%Y-%m-%d")

                    # Validate expense data
                    if (
                        not math.isfinite(amount) 
                        or amount <= 0
                        or not category
                        or not description
                        or category.lower() == "null"
                        or description.lower() == "null"
                    ):
                        print("Skipping an invalid expense record.")
                        continue

                    expense = {
                        "amount": amount,
                        "category": category,
                        "date": date_text,
                        "description": description
                    }

                    loaded_expenses.append(expense)
                    loaded_count += 1

                except (
                    ValueError,
                    TypeError,
                    AttributeError,
                    KeyError
                ):
                    print("Skipping an invalid expense record.")
            expenses.extend(loaded_expenses)
            data_loaded = True
            print(
                f"{loaded_count} expense records loaded successfully!"
            )

    except (OSError, csv.Error) as error:
        print(f"Error loading expenses: {error}")


# Main menu
def main():
    while True:
        print("\n========== PERSONAL EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Generate Reports")
        print("4. Visualize Expenses")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            generate_report()

        elif choice == "4":
            plot_category_expenses()
            plot_expense_pie_chart()
            plot_weekly_expenses()
            plot_monthly_expenses()

        elif choice == "5":
            save_expenses()

            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 5.")


# Start the application
if __name__ == "__main__":
    load_expenses()
    main()