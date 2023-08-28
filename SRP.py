class Driving:
    def drive(self,name):
        print(f"{name} is moving")

class Refuel:
    def fuel(self,name):
        print(f"{name} is moving")

class Parking:
    def park(self,name):
        print(f"{name} is parked")

def drive(self):
    self.Driving.drive(self.name)
def fuel(self):
    self.refueling.fuel(self.name)
def park(self):
    self.parking.park(self.name)

class car:
    def __init__(self,name):
        self.name = name
        self.driving = Driving()
        self.refuel = Refuel()
        self.parking = Parking()

car()

