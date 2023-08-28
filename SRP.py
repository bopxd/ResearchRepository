class car: #The class to handle the car object
    def __init__(self,name):
        self.name = name

class Driving(car): #class specifically for driving the car
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



