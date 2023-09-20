import random


class BankAccount:
    def __init__(self, account_number, account_holder, balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.loan_limit = 2 * self.balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            print(f"Deposited {amount} into account {self.account_number}.")
        else:
            print("Invalid deposit amount. Please deposit a positive value.")

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Withdrew {amount} from account {self.account_number}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            print("The bank is bankrupt.")

    def check_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")

    def transfer(self, other_account, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            other_account.balance += amount
            self.transaction_history.append(f"Transferred {amount} to Account {other_account.account_number}.")
            print(f"Transferred {amount} from account {self.account_number} to account {other_account.account_number}.")
        else:
            print("Insufficient funds or invalid transfer amount.")
            print("The bank is bankrupt.")

    def get_transaction_history(self):
        print(f"Transaction History for account {self.account_number}:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount):
        if amount <= self.loan_limit:
            self.balance += amount
            self.loan_limit -= amount
            self.transaction_history.append(f"Took a loan of {amount}")
            print(f"Took a loan of {amount} from the bank.")
        else:
            print("Loan amount exceeds the loan limit.")

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"


class BankManagementSystem:
    def __init__(self):
        self.accounts = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True

    def create_account(self, account_holder):
        account_number = random.randint(100000, 99999999)
        while account_number in self.accounts:
            account_number = random.randint(100000, 99999999)
        self.accounts[account_number] = self.accounts.get(account_number, account_holder)
        print(f"Account {account_number} created successfully.")
        return account_number

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def check_total_balance(self):
        self.total_balance = sum(account.balance for account in self.accounts.values())
        print(f"Total Available Balance in the bank: {self.total_balance}")

    def check_total_loan_amount(self):
        self.total_loan_amount = sum(account.loan_limit for account in self.accounts.values())
        print(f"Total Loan Amount in the bank: {self.total_loan_amount}")

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature
        state = "ON" if self.loan_feature else "OFF"
        print(f"Loan feature of the bank is now {state}.")

    def __str__(self):
        return f"Bank Management System: {len(self.accounts)} accounts"


if __name__ == "__main__":
    bank = BankManagementSystem()

    while True:
        print("\n===== Banking Management System =====")
        print("1. User - Create Account")
        print("2. User - Deposit")
        print("3. User - Withdraw")
        print("4. User - Transfer")
        print("5. User - Check Balance")
        print("6. User - Check Transaction History")
        print("7. User - Take a Loan")
        print("8. Admin - Create Account")
        print("9. Admin - Check Total Balance")
        print("10. Admin - Check Total Loan Amount")
        print("11. Admin - Toggle Loan Feature")
        print("12. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_holder = input("Enter Account Holder Name: ")
            account_number = bank.create_account(account_holder)

        elif choice == 2:
            account_number = int(input("Enter Account Number: "))
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter Amount to Deposit: "))
                account.deposit(amount)
            else:
                print(f"Account {account_number} does not exist.")

        elif choice == 3:
            account_number = int(input("Enter Account Number: "))
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter Amount to Withdraw: "))
                account.withdraw(amount)
            else:
                print(f"Account {account_number} does not exist.")

        elif choice == 4:
            account_number_1 = int(input("Enter Your Account Number: "))
            account_1 = bank.get_account(account_number_1)
            if account_1:
                account_number_2 = int(input("Enter Recipient's Account Number: "))
                account_2 = bank.get_account(account_number_2)
                if account_2:
                    amount = float(input("Enter Amount to Transfer: "))
                    account_1.transfer(account_2, amount)
                else:
                    print(f"Recipient's Account {account_number_2} does not exist.")
            else:
                print(f"Your Account {account_number_1} does not exist.")

        elif choice == 5:
            account_number = int(input("Enter Account Number: "))
            account = bank.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print(f"Account {account_number} does not exist.")

        elif choice == 6:
            account_number = int(input("Enter Account Number: "))
            account = bank.get_account(account_number)
            if account:
                account.get_transaction_history()
            else:
                print(f"Account {account_number} does not exist.")

        elif choice == 7:
            account_number = int(input("Enter Account Number: "))
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter Loan Amount: "))
                account.take_loan(amount)
            else:
                print(f"Account {account_number} does not exist.")

        elif choice == 8:
            account_holder = input("Enter Account Holder Name: ")
            bank.create_account(account_holder)

        elif choice == 9:
            bank.check_total_balance()

        elif choice == 10:
            bank.check_total_loan_amount()

        elif choice == 11:
            bank.toggle_loan_feature()

        elif choice == 12:
            print("Thank you for using the Banking Management")