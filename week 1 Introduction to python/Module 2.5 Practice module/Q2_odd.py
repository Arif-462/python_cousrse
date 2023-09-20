def sumOfOddNum(x, y):    
    total = 0
    for i in range(x,y):
        if i % 2 == 1:
            total += i
    return total

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    ans = sumOfOddNum(x, y)
    print(ans)