#https://docs.python.org/3/tutorial/datastructures.html

numbers = [12,45,16,18,72,97,45,6]
numbers.append(28)
print(numbers)

numbers.insert(2, 78)
print(numbers)

numbers.pop(1)
print(numbers)

numbers.remove(6)
print(numbers)

index = numbers.index(45)
print(index)

sorted = numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)