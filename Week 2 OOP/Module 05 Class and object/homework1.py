class calculator:
    brand = 'Casio'
    type = 'scientific'
    origin = 'japan'

    def add(self, num1, num2):
        ans = num1 + num2
        return ans
    
    def deduct(self, num1, num2):
        ans = num1 - num2
        return ans
    def multiply(sesf, num1, num2):
        ans = num1 * num2
        return ans
    def divide(self, num1, num2):
        ans = num1 // num2
        return ans


my_divice = calculator()
print(my_divice)
print(my_divice.brand)

ans1 = my_divice.add(10, 2)
print(ans1)

ans2 = my_divice.deduct(10, 2)
print(ans2)

ans3 = my_divice.divide(10, 2)
print(ans3)

ans4 = my_divice.multiply(10, 2)
print(ans4)