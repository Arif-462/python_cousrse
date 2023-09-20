class Restaurant:
    def __init__(self, name, rent,  menu = []) -> None:
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.orders = []
        self.rent = rent
        self.menu = menu
        self.expense = 0
        self.revenue = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee

    def add_order(self, order):
        self.orders.append(order)


    def receive_payment(self, order, amount, cutomer):
        if amount >= order.bill:
            print(amount, order.bill)
            self.revenue += order.bill
            self.balance += order.bill
            self.due_amount = 0
            return amount - order.bill
        else:
            print(f'your tk {amount} is not sufficient')
        
    def pay_expanse(self, amount, descripstion):
        if amount <= self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expanse {amount} for {descripstion}')
        else:
            print(f'Not enough money to pay {amount}')

    def pay_salay(self, employee):
        print(f'paying salary for {employee.name}, salary: {employee.salary} ')
        if employee.salary < self.balance:
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receive_salary()

    def pay_rent(self, amount, rent_type):
        if amount <= self.balance:
            self.balance -= amount
            self.expense += amount
            print(f'Expense : {amount} for {rent_type}')


    def show_employees(self):
        if self.chef is not None:
            print(f'Chef: {self.chef.name} || salary: {self.chef.salary}')
        if self.server is not None:
            print(f'server: {self.server.name} || salary: {self.server.salary}')
        
        if self.manager is not None:
            print(f'manager: {self.manager.name} || salary: {self.manager.salary}')

        
        