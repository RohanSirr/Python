class Account:
    """Class to represent a bank account."""
    account_counter = 1001  # Class variable for unique account numbers

    def __init__(self, name, initial_deposit):
        self.account_no = Account.account_counter
        Account.account_counter += 1
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount}. New Balance: Rs{self.balance}")
        else:
            print("Amount should be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount should be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdraw Rs.{amount}. Remaining Balance Rs.{self.balance}")

    def check_balance(self):
        print(f"Current balance: Rs.{self.balance}")

    def account_details(self):
        print(f"Account No: {self.account_no}\nName: {self.name}\nBalance: ₹{self.balance}")


def show_menu():
    print("\n**** Bank Menu ****")
    print("1. Open new account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Balance check")
    print("5. Show all accounts")
    print("6. Exit")

def find_account(accounts, acc_no):
    for acc in accounts:
        if acc.account_no == acc_no:
            return acc
    return None

def main():
    accounts = []
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter Account Holder's name: ").strip()
            dep_input = input("Enter initial deposit amount: ").strip()
            if not dep_input.isdigit() or int(dep_input) < 0:
                print("Enter a valid positive amount.")
                continue
            initial_deposit = int(dep_input)
            new_acc = Account(name, initial_deposit)
            accounts.append(new_acc)
            print(f"Account opened! Account no: {new_acc.account_no}")

        elif choice == '2':
            acc_input = input("Enter account no. : ").strip()
            if not acc_input.isdigit():
                print("Invalid Account number.")
                continue
            acc_no = int(acc_input)
            acc = find_account(accounts, acc_no)
            if acc:
                dep_amount = input("Enter deposit amount: ").strip()
                if dep_amount.isdigit():
                    acc.deposit(int(dep_amount))
                else:
                    print("Please enter a valid deposit amount")
            else:
                print("Account not found.")

        elif choice == '3':
            acc_input = input("Enter account no. : ").strip()
            if not acc_input.isdigit():
                print("Invalid account no.")
                continue
            acc_no = int(acc_input)
            acc = find_account(accounts, acc_no)
            if acc:
                wd_amount = input("Enter withdrawal amount: ").strip()
                if wd_amount.isdigit():
                    acc.withdraw(int(wd_amount))
                else:
                    print("Please enter a valid withdrawal amount")
            else:
                print("Account not found.")

        elif choice == '4':
            acc_input = input("Enter account no. : ").strip()
            if not acc_input.isdigit():
                print("Invalid account no.")
                continue
            acc_no = int(acc_input)
            acc = find_account(accounts, acc_no)
            if acc:
                acc.check_balance()
            else:
                print("Account not found.")

        elif choice == '5':
            if not accounts:
                print("No accounts available.")
            else:
                for acc in accounts:
                    print("\n--------------------")
                    acc.account_details()

        elif choice == '6':
            print("\nExiting the Bank Management Program. Have a great day! ")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
