
    
n = int(input())

num1 = 0
num2 = 1
next = 0
count = 1

while count<= n:
    print(next, end=" ")
    count +=1
    num1 = num2
    num2 = next
    next = num1+num2
