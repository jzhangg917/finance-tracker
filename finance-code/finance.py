import datetime
import json

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, description, amount):
        self.transactions.append({
            'date': date,
            'description': description,
            'amount': amount
        })

    def get_balance(self):
        balance = sum(transaction['amount'] for transaction in self.transactions)
        return balance

    def show_transactions(self):
        for idx, transaction in enumerate(self.transactions, start=1):
            print(f"{idx}. {transaction['date']} - {transaction['description']} - ${transaction['amount']:.2f}")

    def save_transactions_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.transactions, file, default=str)

    def load_transactions_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.transactions = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No data found or invalid data in the file.")

def get_valid_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_valid_float_input(prompt):
    while True:
        try:
            amount = float(input(prompt))
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")

def main():
    tracker = FinanceTracker()

    while True:
        print("\nFinance Tracker")
        print("1. Add Transaction")
        print("2. Show Transactions")
        print("3. Show Balance")
        print("4. Save Transactions")
        print("5. Load Transactions")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nEnter Transaction Details:")
            date = get_valid_date_input("Date (YYYY-MM-DD): ")
            description = input("Description: ")
            amount = get_valid_float_input("Amount: ")
            tracker.add_transaction(date, description, amount)
            print("Transaction added successfully!")

        elif choice == '2':
            print("\nAll Transactions:")
            tracker.show_transactions()

        elif choice == '3':
            balance = tracker.get_balance()
            print(f"Current Balance: ${balance:.2f}")

        elif choice == '4':
            filename = input("Enter filename to save (e.g., data.json): ")
            tracker.save_transactions_to_file(filename)
            print("Transactions saved to file.")

        elif choice == '5':
            filename = input("Enter filename to load from (e.g., data.json): ")
            tracker.load_transactions_from_file(filename)
            print("Transactions loaded from file.")

        elif choice == '6':
            print("Exiting Finance Tracker...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
