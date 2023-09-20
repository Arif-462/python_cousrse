def sumOfequation(x,y):
    base = x
    exponent = y-1
    ans = 1
    a = x*y    
    while exponent != 0:
        ans = ans * base
        exponent -= 1
        sum = int(ans)
    return sum + a

x,y = map(int, input().split())

print(sumOfequation(x,y))

# base = 5
# exponent = 4
# ans = 1
# while exponent != 0:
#     ans *= base
#     exponent -= 1
# print (str(ans))