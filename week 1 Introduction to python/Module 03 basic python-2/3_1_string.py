name1 = 'sakib\'s khan'
name2 = "sakib khan"
#multiline character
name3="""
sakib khan
number one
"""

print(name1)

#string in a sequence of character
for char in name2:
    print (char)

print (name2[3])
print(name2[2:5])



print(name2[-3])
print(name2[::-1])
#string mutable means changeabel
# immutable means you can not change it
# name2[0] = 'R'

print(name2)

if 'khan' in name2:
    print ("exists")

print(name2.upper())
print(name2.lower())
print(name2.capitalize())
print(name2.split())
print(name2.count('k'))
# print(name2.find('sakib'))


