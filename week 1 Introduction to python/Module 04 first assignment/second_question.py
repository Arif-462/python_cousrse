def elements_to_remove(a):
    
    count = {}    
    list = [] 
    for num in a:
        count[num] = count.get(num , 0) + 1    
        
    for num, count in count.items():
        if count == num:
            continue
        elif count > num:
            list.append(count-num)
        elif count < num:
            list.append(count)  
    return list     
    


N = int(input())
a = list(map(int, input().split()))

ans = 0
result = elements_to_remove(a)
for i in result:
    ans += i
print(ans)

