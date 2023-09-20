# set : unique item colllection
numbers = [12,45,78,13,48,95]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)

numbers_set.add(180)
print(numbers_set)

# print(numbers_set[2])
numbers_set.remove(180)

print(numbers_set)

for item in numbers_set:
    print(item)

if 95 in numbers_set:
    print ('exists')

A = {1,4,5,8}
B = {11,4,8,9}
print(A & B)
print(A | B)

