# poly ---> many(multiple)
# morphy--->shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name
        
    def make_sound(self):
        print('animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Ghew Ghew')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('vhaa vhaa vhaa')


don = Cat('Real don')
don.make_sound()

Shepard = Dog('Local Shepard')
Shepard.make_sound()

goat = Goat('Black bengl')
goat.make_sound()

red = Goat('tam tam')
red.make_sound()

animals = [don, Shepard, goat, red]
for animal in animals:
    animal.make_sound()