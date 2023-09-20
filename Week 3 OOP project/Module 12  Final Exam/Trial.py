import random

class Bank:
    total_balance = 0
    total_loan_amount = 0 
    accounts = []
    loan_feature = True  

    def __init__(self, name) -> None:
        self.name = name

    def create_account_number(self, name):
        account_number = random.randint(1000, 9999999)
        self.accounts.append(account_number)
        print(f'Your account number is {account_number}')
        return account_number


class User:
    def __init__(self, balance, account_number) -> None:
        self.balance = balance
        self.account_number = account_number
        self.transaction_history = []
        self.total_loan = 0

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            Bank.total_balance += amount
            self.transaction_history.append(f'Deposited :{amount}')
            print(f'Deposite :{amount}')

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            Bank.total_balance -= amount
            self.transaction_history.append(f'Withdraw :{amount}')
            print(f'withdraw :{amount}')

    def check_balance(self):
        print(f'Your current balance is {self.balance}')
        return self.balance
    
    def transfer_money(self, receipent, amount):
        if amount < self.balance:
            # receipent.balance += amount
            self.balance -= amount 
            self.transaction_history.append(f'Transfer {amount} to {receipent}') 

    def get_loan(self, amount):
        if amount < self.balance * 2:
            self.balance += amount
            Bank.total_loan_amount += amount
            Bank.total_balance -= amount
            self.transaction_history.append(f'received loan :{amount}')      

admin = Bank('Jamuna')
# admin.create_account_number('arif')
user = User(5000, admin.create_account_number('arif'))
user.deposite(1200)
user.withdraw(200)
user.transfer_money(admin.create_account_number('shorif'), 500)
user.get_loan(1000)

print(f'total bank balance is{admin.total_balance}')
print(f'total loan is {admin.total_loan_amount}')



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


    
    
        