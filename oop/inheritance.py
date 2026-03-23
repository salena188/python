#Inheritance
class Ride:
    def __init__(self, user, distance):
        self.user = user
        self.distance = distance
    def fare(self):
        print(self.distance)
        print("this is for calculation of fare ")

class BikeRide(Ride): #inheritance
    def __init__(self, user, distance):
        super().__init__(user, distance)
    def fare(self):
        print("this is bike fare ",self.distance * 50)

class CarRide(Ride):
    def __init__(self, user, distance):
        super().__init__(user, distance)

    def fare(self):
        print("this is car fare ",self.distance * 100)
        #print(self.distance * 100)

r1 = BikeRide("Salina", 10)
r1.fare()
r2= CarRide("Ben", 20)
r2.fare()