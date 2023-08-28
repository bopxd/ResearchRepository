class car: #The class to handle the car object such as the cars colour, brand, make year etc
    def __init__(self,name):
        self.name = name

class Driving(car): #class specifically for driving the car, is only called when the car is moving
    def __init__(self,name):
        self.name = name
    def drive(self,name):
        return(f"{name} is moving")

class Refuel(car): #class specifically for refueling the car
    def __init__(self,name):
        self.name = name
    def fuel(self,name):
        return(f"{name} is refueling")

class Parking(car): #class specifically for parking the car
    def __init__(self,name):
        self.name = name
    def park(self,name):
        return(f"{name} is parked")

#single responsibility means for one section of code to handle one thing and one thing only
#E.G the parking class handles only the parking of the car is not called if the car is moving or refuel
#Letting me change the parking class and object without affecting when the car is going to drive or refuel