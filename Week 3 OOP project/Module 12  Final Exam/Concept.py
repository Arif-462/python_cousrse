"""
User
cutomer
voult
    deposite
    withdraw
    check balance
    check trnafer history
    take loan from bank

Admin
    create an account
    check the total available balance
    check the total loan
    on or ff the loan feacher of this bank
"""

class Bank:
    total_balance = 0
    total_loan_amount = 0
    loan_feature_enabled = True

class User:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        Bank.total_balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            Bank.total_balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
        else:
            print("Insufficient balance. Bank is bankrupt.")

    def check_balance(self):
        return self.balance

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
        else:
            print("Insufficient balance. Bank is bankrupt.")

    def take_loan(self):
        if Bank.loan_feature_enabled and self.balance > 0:
            loan_amount = min(self.balance * 2, Bank.total_balance)
            self.balance += loan_amount
            Bank.total_balance += loan_amount
            Bank.total_loan_amount += loan_amount
            self.transaction_history.append(f"Took a loan: {loan_amount}")
            return loan_amount
        else:
            print("Unable to take a loan at the moment.")

    def check_transaction_history(self):
        return self.transaction_history

class Admin:
    def __init__(self):
        self.name = "Admin"

    def check_total_balance(self):
        return Bank.total_balance

    def check_total_loan_amount(self):
        return Bank.total_loan_amount

    def enable_loan_feature(self):
        Bank.loan_feature_enabled = True
        print("Loan feature is enabled.")

    def disable_loan_feature(self):
        Bank.loan_feature_enabled = False
        print("Loan feature is disabled.")

# Example usage:

if __name__ == "__main__":
    # Creating the admin
    admin = Admin()

    # Enabling loan feature by the admin
    admin.enable_loan_feature()

    # Creating users and their initial balances
    user1 = User("John", 1000)
    user2 = User("Alice", 500)

    # Depositing and withdrawing money for users
    user1.deposit(500)
    user2.deposit(300)
    user1.withdraw(200)
    user2.withdraw(600)  # This should print "Insufficient balance. Bank is bankrupt."

    # Transferring money between users
    user1.transfer(user2, 300)

    # Taking a loan for a user
    user1.take_loan()

    # Checking account balance, total balance, and transaction history for a user
    print(user1.name, "Balance:", user1.check_balance())
    print(user2.name, "Balance:", user2.check_balance())
    print("Total Bank Balance:", admin.check_total_balance())
    print("Total Loan Amount:", admin.check_total_loan_amount())
    print("Transaction History for", user1.name, ":", user1.check_transaction_history())