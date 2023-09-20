def call():
    print('calling someone i dont know')
    return 'call done'


class phone:
    name = 'samsung'
    color = 'mejenta'
    price = 20000
    feature = ['camera','speaker','hamer']

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'sending sms to:{phone} and message: {sms}'
        return text


my_phone = phone()
print(my_phone.feature)
my_phone.call()
ans = my_phone.send_sms(+96596757224, 'I love python!')
print(ans)


