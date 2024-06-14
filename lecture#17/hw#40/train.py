"""Calculate the distance between points for a train on the ground"""

import datetime
import random
from geopy.geocoders import Nominatim
from haversine import haversine, Unit


class Train:

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def get_coordinates(self):
        """Get coordinates for start and end points."""
        geolocator = Nominatim(user_agent="train_app")
        location_start = geolocator.geocode(self.start_point)
        location_end = geolocator.geocode(self.end_point)
        return location_start, location_end

    def create_route(self):
        """Create route for a train."""
        start_point, end_point = self.get_coordinates()
        start_point_address = start_point.address
        end_point_address = end_point.address
        return f'{start_point_address} -> {end_point_address}'

    def calculate_distance(self):
        """Calculate the distance between points for a train on the ground.
        Distance can to change because of random speed."""
        start_point, end_point = self.get_coordinates()
        start_point_coordinates = (start_point.latitude, start_point.longitude)
        end_point_coordinates = (end_point.latitude, end_point.longitude)
        distance = haversine(start_point_coordinates, end_point_coordinates, unit=Unit.KILOMETERS)
        return round(distance, 2)

    @staticmethod
    def calculate_speed():
        """Calculate speed for a train."""
        speed = random.randint(140, 200)
        return speed

    def calculate_time(self):
        """Calculate time for a train to drive from start to end points."""
        time = self.calculate_distance() / self.calculate_speed()
        time = datetime.timedelta(hours=time)
        return time

    def the_train_departed(self):
        """Return information about the train."""
        return f'Route: {self.create_route()}\n' \
               f'Distance: {self.calculate_distance()} km\n' \
               f'Speed: {self.calculate_speed()} km/h\n' \
               f'Travel duration: {self.calculate_time()}\n'



