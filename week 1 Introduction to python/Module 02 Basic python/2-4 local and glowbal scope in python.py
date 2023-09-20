balance = 3000#glowbal variable

def buy_things(item, price):
    # can access global variable define glowbal keyword
    global balance
    #balance = 500 #local variable
    print(f'Previous balance', balance)
    balance = balance-price

    print(f'balance after buying  {item}', balance)

buy_things('sunglasss' , 1000)
print('glowbal balance after buy' , balance)