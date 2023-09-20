
def differentValues(x,y):
    z=1
    for i in range(x):
        for j in range(y):
            if y-i-j >= 0 and y-i-j <= x:
                z += 1
    return z

k , s = map(int, input().split())
print (differentValues(k,s))
