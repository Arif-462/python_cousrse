# readonly -> you can not set the value. value can not be change
# getter -> get a value of a property throuh a method. Most of the time you wiil get ith value of a private attribute.
# setter -> set the value of property throuh a method. Most of the time. you will set the value of a private property.

class User:
    def __init__(self, name , age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    # getter without is readonly attribute
    @property # @ maks function is called decoretor
    def age(self):
        return self._age
    

    # getter without is readonly attribute
    @property
    def salary(self):
        return self.__money
    

    @salary.setter
    def salary(self, value):
        if value < 0:
            print('salary can not be negative')
        self.__money += value


sumsu = User('kopa', 25, 12000)
# print(sumsu.__money)
# print(sumsu.age())

print(sumsu.age)
# print(sumsu.salary())

print(sumsu.salary)

sumsu.salary = 4000
print(sumsu.salary) # getter and setter


        