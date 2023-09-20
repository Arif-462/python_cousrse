
def split_strings(s):    
    l = 0
    r = 0
    cnt = 0

    balanced_strings = []

    for char in s:
        if char == 'L':
            l += 1
        else:
            r += 1       
        if l == r:
            balanced_strings.append(s[:l + r])
            cnt += 1
            s = s[l + l :]
            l = 0
            r = 0
    print(cnt)
    return balanced_strings

str = input().strip()
ans = split_strings(str)

print(*ans, sep="\n")

