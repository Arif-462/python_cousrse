def multiple():
    return 3, 4

print(multiple())

things = 'pen','tripod', 'water bottle','phone', 'charger'
print(things)
print(things[0])
print(things[-2])
print(things[2:5])
if 'phone' in things:
    print('exists')

for item in things:
    print (item)

print(len(things))

mega = ([2,3,5,4,8,7,8],[1,2,4,7,8,9])
print(type(mega))

print(mega[0])
mega[0][1] = 1245
print(mega)
