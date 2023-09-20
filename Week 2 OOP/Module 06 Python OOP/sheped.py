from math import pi

class Shape:
    def __init__(self, name) -> None:
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)
    def area(self):
        return pi * self.radius * self.radius
    
class Square(Shape):
    def __init__(self, name, side) -> None:
        self.side = side
        super().__init__(name)

    def area(self):
        return self.side * self.side
        

rec = Rectangle('boro bhai', 50, 20)
print(rec.area())

cir = Circle('gol bhai', 5)
print(cir.area())

sq = Square('mejo bhai', 10)
print(sq.area())