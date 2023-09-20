class Animal:
    def __init__(self, name) -> None:
        self.name = name
        
    def make_sound(self):
        print('animal making some sound')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Ghew Ghew')


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow')




Shepard = Dog('Local Shepard')
Shepard.make_sound()

don = Cat('Real don')
don.make_sound()