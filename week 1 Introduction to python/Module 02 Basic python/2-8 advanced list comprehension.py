numbers = [45,12,47,87,16,34,52,18,19,91,95]
odds = []
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)

print(odds)

odd_nums = [num % 2 == 1 and num % 5 == 0]
print(odd_nums)


players = ['sakib', 'musfiq','mustafij', 'tamim', 'taskin']
ages = [25,30,19,28,24]
age_comb = []
for player in players:
    print(player)
    for age in ages:
        print(player ,age)
        age_comb.append([player, age])
print(age_comb)
age_comb2 = [[player, age] for player in players for age in ages]
print(age_comb2)


numbers =[7,6,5,3,3,2,1]
print(numbers[-4])