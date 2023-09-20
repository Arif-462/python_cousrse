class company:
    def __init__(self, name, office_address, phone) -> None:
        self.name = name
        self.office_address = office_address
        self.phone = phone
        self.bus = []
        self.drivers = []
        self.routes = []
        self.counter = []
        self.manager = []
        self.supervisor = []
        self.engineer = []
        self.fare = []


class Driver:
    def __init__(self, name, address, licence, phone, age) -> None:
        self.name = name
        self.address = address
        self.licence = licence
        self.phone = phone
        self.age = age

class Counter:
    def __init__(self) -> None:
        pass
    def purchage_a_ticket(self, start, destination):
        pass

class Routes:
    def __init__(self) -> None:
        pass

class Passenger:
    def __init__(self) -> None:
        pass

class Supervisor:
    def __init__(self) -> None:
        pass


Red_mia = Driver('Md Ariful Islam', 'Sirajgonj', 123, 123458, 30)
print(Red_mia)