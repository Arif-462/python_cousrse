class Laptop:
    def __init__(self,brand, price, color, memory) -> None:
        self.color = color
        self.brand = brand
        self.price = price
        self.memory = memory

    def run(self):
        return f'Running laptop: {self.brand}'
    
    def coding(self):
        return f'Learning python and practicing'
    
class phone:
    def __init__(self, brand, price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim
    def run(self):
        return f'Phone saradin ki koro'
    def phone_call(self, number, text):
        return f'sending sms to : {number} with : {text}'

class Camera:
    def __init__(self, brand, price, color, pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.prxel = pixel

    def run(self):
        pass
    def lance(self):
        pass
        
        