class phone:
    manufacture = 'china'

    #constructor define
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price


     
    def send_sms(sesf, phone, sms):
        text = f'sendin to :{phone} {sms}'
        print(text)

#calling function from main class
my_phone = phone('ariful islam', 'samsung', 20000)
print(my_phone.owner, my_phone.brand, my_phone.price)
 
# calling function from main class
her_phone = phone('anik','symphony',15000)
print(her_phone.owner, her_phone.brand, her_phone.price)

