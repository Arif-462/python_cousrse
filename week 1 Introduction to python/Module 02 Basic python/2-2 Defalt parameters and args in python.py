def sum(num1, num2, num3=0, num4=0, num5=0):
    result = num1 + num2 + num3
    return result
#total = sum(99, 11)

#print(total)

#args

def all_sum(num1, num2, *numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum = sum + num
    return sum

total = all_sum(55, 50, 80, 98, 110)
print('all sum is = ', total)
    