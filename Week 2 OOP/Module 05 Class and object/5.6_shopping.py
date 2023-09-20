class shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'product_name':item, 'price':price, 'quantity':quantity}
        self.cart.append(product)

        
    #home work for removing item from the list
    def remove_item(self, item):
        for item in self.cart:
            self.cart.remove(item)
            

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            print(item)
            total += item['price'] * item['quantity']
        print('total price', total)
        if amount < total:
            print(f'please provide also {total - amount} more.')
        else:
            extra = amount - total
            print(f'here is your items and extra money {extra}')
        

myself = shopping('ariful islam')
myself.add_to_cart('alu', 40, 2)
myself.add_to_cart('dal', 50, 5)
print(myself.cart)
myself.checkout(500)
myself.checkout(300)
myself.remove_item('alu')
ans = myself.cart
print(ans)
