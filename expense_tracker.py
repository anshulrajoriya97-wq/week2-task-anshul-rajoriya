import csv
import os

FILE_NAME = "expenses.csv"

def add_record():
    record_type = input("Type (Income/Expense): ")
    amount = float(input("Amount: "))
    description = input("Description: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([record_type, amount, description])
    print("Record added!")

def summary():
    income, expense = 0, 0
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].lower() == "income":
                income += float(row[1])
            elif row[0].lower() == "expense":
                expense += float(row[1])
    print(f"Total Income: {income}")
    print(f"Total Expense: {expense}")
    print(f"Net Balance: {income - expense}")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Record")
        print("2. Summary")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_record()
        elif choice == "2":
            summary()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
