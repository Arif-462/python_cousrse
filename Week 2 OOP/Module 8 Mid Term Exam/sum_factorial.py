
import math
class Result:
    def __init__(self, a, b ,c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def get_sum(self):
        sum = a + b + c
        return sum
    
    def get_factorial(self):
        return math.factorial(b)
       
a = 4
b = 5
c = 6
ans = Result(a, b, c)
print(ans.get_sum())
print(ans.get_factorial())