class Transportation(object):
   """Abstract base class"""

   def __init__( self, start, end, distance ):
      if self.__class__ == Transportation:
         raise NotImplementedError
      self.start = start
      self.end = end
      self.distance = distance

   def find_cost( self ):
      """Abstract method; derived classes must override"""
      raise NotImplementedError


class Walk( Transportation ):

   def __init__( self, start, end, distance ):
      Transportation.__init__( self, start, end, distance)

   def find_cost( self ):
      return 0
   
class Train( Transportation ):

   def __init__( self, start, end, distance ):
      self.stations = ["Bang Sue", "Chatuchak Park", "Phahon Yothin", "Ladkrabang Station","Payathai Station"]
      Transportation.__init__( self, start, end, distance)

   def find_cost( self ):
      base_fare = 35
      cost_per_km = 5
      station_cost = 5 * (len(self.stations) - 1)  # Subtracting 1 for the starting station
      return (cost_per_km * self.distance) + station_cost
   
class Taxi( Transportation ):

   def __init__( self, start, end, distance ):
      Transportation.__init__( self, start, end, distance)

   def find_cost( self ):
      cost_per_kilo = 40
      return self.distance * cost_per_kilo


   
# main program

travel_cost = 0

trip = [ Walk("KMITL","KMITL SCB Bank",0.6),
         Taxi("KMITL SCB Bank","Ladkrabang Station",5),
         Train("Ladkrabang Station","Payathai Station",6),
         Taxi("Payathai Station","The British Council",3) ]

for travel in trip:
   travel_cost += travel.find_cost()
   print(travel_cost)
