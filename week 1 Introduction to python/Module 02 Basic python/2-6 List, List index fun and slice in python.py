#https://docs.python.org/3/tutorial/datastructures.html
numbers = [1,2,3,4,5,6,7,8,9,10,11,45]
#python ulta dik theke index count kore -1,-2,-3... kore

print(numbers[3], numbers[-3])

#list(start : end ) start from the start value and end just before the end value
print(numbers[2 : 5])
print(numbers[1 : 10])


# list(start : end : step)
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[1:7:3])
print(numbers[7:1:-3])
print(numbers[2:])
print(numbers[: 10])
print(numbers[:])#short cut to copy a list
print(numbers[: :-1])#short cut to reverse a list