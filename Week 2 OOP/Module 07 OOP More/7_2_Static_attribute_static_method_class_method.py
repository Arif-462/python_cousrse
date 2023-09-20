# static attibute (class attribute)
# static mathod @staticmethod
# class method @classmethod
# Differences between static method and class method

class Shopping:
    cart = [] # class attribute / static attribute
    origin = 'China'

    def __init__(self, name, location) -> None:
        self.name = 'jamuna city'  #instance attribute
        self.location = 'jamer matha'


    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def multiply(a, b):
        result = a * b
        print(result)

    @classmethod
    def hudai_dekhi(self, item):
        print(f'hudain dekhi kintu kinbo na', item)

basundhara = Shopping('basu', 'not popular')
# basundhara.purchase('lungi', 500, 1000)
basundhara.hudai_dekhi('shirt')

# Shopping.purchase( 2, 3, 3)
Shopping.hudai_dekhi('lungi')

Shopping.multiply(2,3) #static method use should not instance
basundhara.multiply(4,5)
