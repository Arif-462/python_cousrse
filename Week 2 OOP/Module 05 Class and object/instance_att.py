class shop:
    shopping_mall = 'Jamuna'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is a instance attribute


    def add_to_cart(self, item):
        self.cart.append(item)


mehzabeen = shop('meh jabeen')
mehzabeen.add_to_cart('shoe')
mehzabeen.add_to_cart('phone')
print(mehzabeen.cart)

nisho = shop('nishi rater nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)

apurvo = shop('ja purbe dekha jay ni')
apurvo.add_to_cart('chiruni')
print(apurvo.cart)


        
        