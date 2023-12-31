class Food:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15
    
class Burger(Food):
    def __init__(self, name, price, meat, ingredients) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients

class Pizza(Food):
    def __init__(self, name, price, size, toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings

class Drinks(Food):
    def __init__(self, name, price, isCold = True) -> None:
        super().__init__(name, price)
        self.isCold = isCold

# Composition has a relation
class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []

    def add_menu_item(self, item_type, item):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'drinks':
            self.drinks.append(item)

    def remove_item(self, item):
        if item in self.pizzas:
            self.pizzas.remove(item)
        elif item in self.burgers:
            self.burgers.remove(item)
        elif self.drinks in self.drinks:
            self.drinks.remove(item)

    def show_menu(self):
        for pizza in self.pizzas:
            print(f'name : {pizza.name} || price: {pizza.price}')
        for burger in self.burgers:
            print(f'name : {burger.name} || price: {burger.price}')
        for drink in self.drinks:
            print(f'name : {drink.name} || price: {drink.price}')

        