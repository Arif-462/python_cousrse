class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000000

    def get_balance(self):
        return self.balance
    
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return f'fokira you can not wirhdraw below {self.min_withdraw}'
        elif amount > self.max_withdraw:
            return f'bank fokir hoye jabe, you can not withdraw than {self.max_withdraw}'
        else:
            self.balance -= amount
            return f'here is your money {amount} , your balcne is {self.get_balance()}'
            

brack = Bank(15000)
ans = brack.withdraw(50)
print(ans)
ans = brack.withdraw(10000008)
print(ans)
ans = brack.withdraw(14500)
print(ans)

tbl = Bank(1000)
tbl.deposite(500)
tbl.deposite(200)
print(tbl.get_balance())
