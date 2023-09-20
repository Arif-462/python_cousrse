#super class
class Gadget:
    def __init__(self, brand, price, color,origin) -> None:
        self.color = color
        self.brand = brand
        self.price = price
        self.origin = origin
    def run(self):
        return f'Running Device: {self.brand}'    
# derived class1
class Laptop(Gadget):
    def __init__(self,memory, ssd) -> None:
        self.memory = memory 
        self.ssd = ssd   
    
    def coding(self):
        return f'Learning python and practicing'

# derived class2  
class Phone(Gadget):
    def __init__(self,brand, price, color, origin, dual_sim) -> None:        
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
    
    def phone_call(self, number, text):
        return f'sending sms to : {number} with : {text}'
    
    def __repr__(self) -> str:
        return f'phone : {self.brand} {self.price} {self.color} {self.dual_sim} {self.origin}'



    
# multilevel inheritance
my_phone = Phone('Iphone:', 100000, 'silver,', 'made in china', 'dual sim,')
print(my_phone.brand)
print(my_phone)
