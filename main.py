from geopy.geocoders import Nominatim
import mpu
import sys

class DistanceCalculator:
	"""
	This is a class for calculating the distance between places.

	Attributes/Parameters:
			place1: coordinates of first place
			place2: coordinates of second place
	"""
	def __init__(self,
			place1,
			place2
			):
		self.place1=place1
		self.place2=place2

	def find_distance(self):
		"""Function that returns the distance in int."""
		dist=mpu.haversine_distance(self.place1, self.place2)
		return int(dist)

if __name__=='__main__':

	try:
		first = input(f'\nEnter the first Place: ')
		second = input('Enter the second Place: ')

		geolocator=Nominatim(user_agent='DistanceCalculator')

		location1 = geolocator.geocode(first)
		location2 = geolocator.geocode(second)

		dist=DistanceCalculator(place1=(location1.latitude, location1.longitude),
					place2=(location2.latitude, location2.longitude))
		distance = dist.find_distance()
		print(f"""
the distance between {first.capitalize()} and {second.capitalize()} is: {distance}km\n
{first.capitalize()}: {dist.place1}\n{second.capitalize()}: {dist.place2}
""")

	except AttributeError as e:
		sys.exit(f"\nsomething went wrong. Please try again\nError: {e}\n")
