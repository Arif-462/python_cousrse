# abstract base method(ABC)
from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod # enforce all derived class to have a method
    
    def eat(self):
        print('mama ki kola khaba')
    @abstractclassmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name
        self.catagory = 'Monkey'
        super().__init__()
    def eat(self):
        print('mama kola khaba')

    def move(self):
        print('hanging on tree')

lyka = Monkey('Lucky')
lyka.eat()
lyka.move()