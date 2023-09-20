
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

class Laptop:
    def __init__(self,memory, ssd) -> None:
        self.memory = memory 
        self.ssd = ssd   
    
    def coding(self):
        return f'Learning python and practicing'
    
class phone:
    def __init__(self,dual_sim) -> None:        
        self.dual_sim = dual_sim
    
    def phone_call(self, number, text):
        return f'sending sms to : {number} with : {text}'

class Camera:
    def __init__(self, brand, price, color, pixel) -> None:
        self.prxel = pixel

    def lance(self):
        pass
    
        
        