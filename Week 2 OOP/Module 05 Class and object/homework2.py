class pen:
    manufacture = 'bangladesh'
    brand = 'matador'
    color = 'Blue'
    price = 5.00

    def __init__(self, owner, brand, price, color):
        self.owner = owner
        self.brand = brand
        self.price = price
        self.color = color



my_pen = pen('Ariful islam', 'matador', 5.00, 'yello')
print(my_pen.manufacture)
print(my_pen.owner, my_pen.brand, my_pen.price, my_pen.color)

your_pen = pen('sadia afrin', 'econo', 6.00, 'red')
print(your_pen.owner, your_pen.brand, your_pen.price, your_pen.color)