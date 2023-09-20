class Bank:
    def __init__(self,holder_name, initial_deposite) -> None:
        self.holder_name = holder_name # public inheritance
        self._branch = 'Banani 12'      # Protected inheritance
        self.__balance = initial_deposite # Private Inheritance
        
    def deposite(self, amont):
        self.__balance += amont

    def get_balance(self):
        return self.__balance 
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return f'Your avilable balance : {self.__balance}'
        else:
            return f'Sorry you have not enough money'

Rafsan = Bank('Arif bhai', 2000)
print(Rafsan.holder_name)
Rafsan.deposite(4500)
print(Rafsan.get_balance())
print(Rafsan._branch)
Rafsan.withdraw(7500)
print(Rafsan.get_balance())
print(Rafsan.withdraw(7500))
print(Rafsan.withdraw(6400))
print(dir(Rafsan))
print(Rafsan._Bank__balance)