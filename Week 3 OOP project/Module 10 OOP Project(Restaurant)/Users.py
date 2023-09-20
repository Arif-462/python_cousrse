
from abc import ABC, abstractclassmethod

class User:
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address, money) -> None:
        self.wallet = money
        self.__order = None
        self.due_amount = 0
        super().__init__(name, phone, email, address)    
    

    @property # Gatter hisebe kaj korbe
    def order(self):
        return self.__order
    
    @order.setter # setter use kora hoice
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        self.due_amount += order.bill
        print(f'{self.name} placed on order {order.bill}')


    def eat_food(self, order):
        print(f'This {self.name} is best {self.items} for ever')


    def pay_for_order(self, amount):
        # TODO: pay for money to manager
        pass

    def give_tips(self, tips):
        #TODO: pay tips to the relate server
        pass

    def write_review(self, stars):
        # TODO: Give fidback to the retuarent
        pass

class Employe(User):
    def __init__(self, name, phone, email, address, salary, startint_date, department) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.due = salary
        self.starting_date = startint_date
        self.department = department

    def receive_salary(self):
        self.due = 0


class Chef(Employe):
    def __init__(self, name, phone, email, address, salary, startint_date, department, cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, startint_date, department)
        self.cooking_item = cooking_item

class Sever(Employe):
    def __init__(self, name, phone, email, address, salary, startint_date, department) -> None:
        self.tips_earning = 0
        super().__init__(name, phone, email, address, salary, startint_date, department)


    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_food(self, order):
        pass
    def receiving_tips(self, amount):
        self.tips_earning += amount

class Manager(Employe):
    def __init__(self, name, phone, email, address, salary, startint_date, department) -> None:
        super().__init__(name, phone, email, address, salary, startint_date, department)



