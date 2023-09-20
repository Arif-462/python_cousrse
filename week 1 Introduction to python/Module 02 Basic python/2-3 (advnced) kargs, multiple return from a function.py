def full_name(first, last):
    name = f'full name is: {first}, {last}'
    return name

#take parameters in order
#name = full_name('alu', 'kodu')
name = full_name(last='kadu', first='alu')
print(name)

#def famous (**kargs)
def famous_name(first, last, **additional):
    name = f'{first}, {last}'
    print(additional)
    #print(additional['title'])
    for key, value in additional.items():
        print(key, value)
    return name

name = famous_name(first='tahere', last='ali', title='hujur', additional='jkir', title2 ='jamjam', title3='madani')
print(name)

#def function_name(num1, num2, *args, **kargs)

def a_lot(num1, num2):
    sum = num1 + num2
    mult= num1*num2
    remain = num1 - num2
    return sum, mult, remain
everything = a_lot(55, 21)
print(everything)