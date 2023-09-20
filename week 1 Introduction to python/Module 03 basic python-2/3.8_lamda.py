# lambda

def double(x):
    return x*2

doubled = lambda num : num * num
result = double(44)
mult = lambda num: num*2
output = doubled(3)


# print(result, output)

add = lambda x,y : x + y
sum = add(11,44)
print (sum)

numbers = [1,2,4,3,7,8,9,5,4]
double_nums = map(doubled, numbers)
double_nums = map(lambda x: x*2, numbers)
squared = map(lambda x: x*x, numbers)
print(numbers)
print(list(double_nums))
print(list(squared))





actors = [
    {'name': 'sabana', 'age': 65},
    {'name': 'arifa', 'age': 45},
    {'name': 'srabonti', 'age': 35},
    {'name': 'taposi', 'age': 18},
    {'name': 'sabnur', 'age': 35}
]

juniors = filter(lambda actor: actor['age'] < 40, actors)
fivers = filter(lambda actors: actors['age'] % 5 == 0, actors)
print(list(juniors))
print(list(fivers))
    

num = lambda a:a*a
print(num(2**2))
