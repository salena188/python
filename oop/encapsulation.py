class Ride:
   def __init__(self, user, distance):
       self.user = user
       self.__distance = distance #private used for encapsulation
   def get_distance(self):
       return self.__distance
   def set_distance(self, distance):
       if distance > 0: self.__distance = distance
r = Ride("jagriti", 5)
r.set_distance(10)
print(r.get_distance())