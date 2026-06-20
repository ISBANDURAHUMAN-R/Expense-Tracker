import csv
import os

FILE_NAME = "expenses.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])


def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense Added Successfully!")


def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n----- Expense Records -----")
        for row in reader:
            print("{:<15} {:<15} {:<10}".format(*row))


def total_expense():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[2])

    print(f"\nTotal Expense: ₹{total}")


def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            category = row[1]
            amount = float(row[2])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    print("\n----- Category Summary -----")
    for category, amount in summary.items():
        print(f"{category}: ₹{amount}")


def main():
    create_file()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
