from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self, company_name) -> None:
       self.company_name = company_name
       self.riders = []
       self.drivers = []
       self.rides = []


    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.company_name}, with riders: {len(self.riders)}, and drivers: {len(self.drivers)}'


class User(ABC):
    def __init__(self, name, email,  NID) -> None:
        self.name = name
        self.email = email
        # TODO: set user dynamically
        self.__id = 0 
        self.__nid = NID
        self.walet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplemented
    
class Rider(User):
    def __init__(self, name, email, NID, current_location, initial_amount) -> None:
        self.current_ride = None
        self.walet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, NID)

    def display_profile(self):
        print(f'Rider name: {self.name} and email: {self.email}')
    
    def load_cash(self, amount):
        if amount > 0:
            self.walet += amount

    def update_location(self, current_location):
        self.current_location = current_location


    def request_ride(self, ride_sharing , destination ):
        if not self.current_ride:  
            print('Looking a ride')          
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)
            print('got the ride yay', ride)
            self.current_ride = ride
        
    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, NID, current_location) -> None:
        super().__init__(name, email, NID)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f'Driver name: {self.name} and email:{self.email}')

    def accept_ride(self, ride):
        ride.set_driver(self)

class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.stat_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()
    
    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.walet -= self.estimated_fare
        self.driver.walet += self.estimated_fare

    def __repr__(self) -> str:
        return f'Ride details. Started : {self.start_location} to the {self.end_location}'


class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location

class Ride_matching:
    def __init__(self, drivers) -> None:
        self.available_driver = drivers
    
    def find_driver(self, ride_request):
        if len(self.available_driver) > 0:
            # TODO:find the closest of the rider
            print('Looing for a driver')
            driver = self.available_driver[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        



class Vehicle(ABC):
    speed = {
        'car' : 50,
        'bike' : 60,
        'cng' : 15
    }
    def __init__(self, vehicle_type, licence_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.licence_plate = licence_plate
        self.rate = rate
        self.status = 'Avilable'


    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate) -> None:
        super().__init__(vehicle_type, licence_plate, rate)

    def start_drive(self):
        self.status = 'unavailble'

    

class Bike(Vehicle):
    def __init__(self, vehicle_type, licence_plate, rate) -> None:
        super().__init__(vehicle_type, licence_plate, rate)

def start_driver(self):
    self.status = 'unavailble'

# rider and driver add to the rideshare
# Check the class intergation
niye_jaw = Ride_Sharing('Niye jaow')
sakib = Rider('Arif', 'emil.com', 12345, 'sirajgonj', 12000)
niye_jaw.add_rider(sakib)
kalapakhi = Driver('kala pakhi', 'driver@gmail.com', 123, 'mirpur' )
niye_jaw.add_driver(kalapakhi)
print(niye_jaw)

#ride request
sakib.request_ride(niye_jaw, 'Uttara')






