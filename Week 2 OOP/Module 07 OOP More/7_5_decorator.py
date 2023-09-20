import math
import time
def timer(func):
    print('i am timer')
    def inner(*args, **kwargs):
        print('time started')
        start = time.time()
        # print(func)
        func(*args, **kwargs)
        print ('time finished')
        end = time.time()
        result = end - start
        print(result)
    return inner

# timer()
# timer()()

@timer # decorator of a function k timere undere nia jay
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'factorial of {n} is {result}')

get_factorial(5)
# get_factorial(n=10)

# vajaila way to decorator
# timer(get_factorial)()
