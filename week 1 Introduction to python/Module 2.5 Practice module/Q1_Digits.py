
def digit_reverse(num):
    digits = []
    while num > 0:
        r = num % 10
        digits.append(r)
        num = num // 10
    return digits

test = int(input())


for _ in range(test):
    N = int(input())
    rev = digit_reverse(N)
    #print(rev)
    for i in rev:
        print(i, end = " " )