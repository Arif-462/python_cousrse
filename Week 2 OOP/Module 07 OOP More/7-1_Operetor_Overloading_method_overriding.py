class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print('Vat mango polau korma')
    def exersize(self):
        raise NotImplementedError

#over over riride
class Cricket(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

        # Override
    def eat(self):
        print('vegetibles')
    def exersize(self):
        print('Gyme poisa dia hudai gham jharay')

    # + over load
    def __add__(self, others):
        return self.age + others.age
    
    # Mul overload
    def __mul__(self, others):
        return self.weight * others.weight
    
    # len overload
    def __len__(self):
        return self.height
    
    def __gt__(self, others):
        return self.age > others.age

    

sakib = Cricket('sakib',28,59,60,'Bangladesh')
musi = Cricket('musi',35, 56, 65 , 'bangladesh')
print(sakib.eat())
print(sakib.exersize())

# print(sakib.__dir__())

print(4 + 5)
print('sakib' + ' rakib')
# print([12,5] + [5,6,7,8,9])
print(sakib + musi)
print(sakib * musi)
print(len(sakib))
print(sakib < musi)



