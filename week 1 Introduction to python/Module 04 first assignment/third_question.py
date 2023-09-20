def max_operations(num_list):
    count = 0
    while all(num % 2 == 0 for num in num_list):
        num_list = [num // 2 for num in num_list]
        count += 1
    return count

N = int(input())
A = list(map(int, input().split()))
ans = max_operations(A)
print(ans)

