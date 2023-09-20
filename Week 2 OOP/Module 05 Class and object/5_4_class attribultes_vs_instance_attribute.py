class shop:

    cart = [] # this is a class attribute

    def __init__(self, buyer):
        self.buyer = buyer


    def add_to_cart(self, item):
        self.cart.append(item)


mehzabeen = shop('meh  zabeen')
mehzabeen.add_to_cart('chall')
mehzabeen.add_to_cart('dall')
print(mehzabeen.cart)  


nisho = shop('nisho')
nisho.add_to_cart('wrist watch')
nisho.add_to_cart('cap')
print(nisho.cart)
