
# base class, parent class or common attribute + functionality class
# derived class, child class, uncommon attribute + functionality calss

class Gadget:
    def __init__(self, brand, price, color,origin) -> None:
        self.color = color
        self.brand = brand
        self.price = price
        self.origin = origin
    def run(self):
        return f'Running Device: {self.brand}'    

class Laptop(Gadget):
    def __init__(self,memory, ssd) -> None:
        self.memory = memory 
        self.ssd = ssd   
    
    def coding(self):
        return f'Learning python and practicing'
    
class Phone(Gadget):
    def __init__(self,brand, price, color, origin, dual_sim) -> None:        
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
    
    def phone_call(self, number, text):
        return f'sending sms to : {number} with : {text}'
    
    def __repr__(self) -> str:
        return f'phone : {self.brand} {self.price} {self.color} {self.dual_sim} {self.origin}'

class Camera:
    def __init__(self, brand, price, color, pixel) -> None:
        self.prxel = pixel

    def lance(self):
        pass
    
# inheritance
my_phone = Phone('Iphone:', 100000, 'silver,', 'made in china', 'dual sim,')
# my_phone.phone_call()
print(my_phone.brand)
print(my_phone)
        