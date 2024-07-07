"""Generate a factory method for creating routes for vehicles: airplane, car, train"""

from abc import ABC, abstractmethod
from airplane import Airplane
from car import Car
from train import Train


class AbstractCreatingRoute(ABC):
    @abstractmethod
    def create_route(self, message, start_point, end_point):
        """Create route for a vehicle"""
        pass


class AirplaneFactory(AbstractCreatingRoute):
    def __init__(self):
        self.mapping = {
            'AirLine': Airplane,
            'AmericanAirlines': Airplane,
            'UnitedAirlines': Airplane,
            'DeltaAirlines': Airplane,
        }

    def create_route(self, message, start_point, end_point):
        """Create route for an airplane. Distance can to change because of random speed."""
        return self.mapping.get(message, Airplane)(start_point, end_point).the_plane_took_off(), message


class CarFactory(AbstractCreatingRoute):
    def __init__(self):
        self.mapping = {
            'Toyota': Car,
            'Ford': Car,
            'Chevrolet': Car,
            'Audi': Car,
            'BMW': Car,
            'Mercedes': Car,
            'Tesla': Car,
            'Hyundai': Car,
            'Kia': Car,
            'Nissan': Car,
            'Honda': Car,
            'Mazda': Car,
            'Subaru': Car,
            'Volkswagen': Car,
            'Jeep': Car
        }

    def create_route(self, message, start_point, end_point):
        """Create route for a car. Distance can to change because of random speed."""
        return self.mapping.get(message, Car)(start_point, end_point).the_car_started(), message


class TrainFactory(AbstractCreatingRoute):

    def __init__(self):
        self.mapping = {
            'Amtrak': Train,
            'UnionPacific': Train,
            'BNSF': Train,
            'NorfolkSouthern': Train,
            'CSX': Train,
            'CanadianNational': Train,
            'CanadianPacific': Train,
            'KansasCitySouthern': Train,
            'Ferromex': Train,
            'FloridaEastCoast': Train
        }

    def create_route(self, message, start_point, end_point):
        """Create route for a train. Distance can to change because of random speed."""
        return self.mapping.get(message, Train)(start_point, end_point).the_train_departed(), message


class FactoryProducer:
    def __init__(self):
        self.mapping = {
            'airplane': AirplaneFactory,
            'car': CarFactory,
            'train': TrainFactory,
        }

    def get_factory(self, message):
        """Get factory"""
        return self.mapping.get(message, CarFactory)()


factory_producer = FactoryProducer()
factory = factory_producer.get_factory('car')
print(factory.create_route('Audi', 'Kyiv', 'Dnipropetrovsk'))
print(factory.create_route('car', 'Kyiv', 'Dnipropetrovsk'))
print('----------------------------------------------------------------------------------')
factory = factory_producer.get_factory('train')
print(factory.create_route('Amtrak', 'Kyiv', 'Dnipropetrovsk'))
print(factory.create_route('train', 'Kyiv', 'Dnipropetrovsk'))
print('----------------------------------------------------------------------------------')
factory = factory_producer.get_factory('airplane')
print(factory.create_route('AmericanAirlines', 'Kyiv', 'Dnipropetrovsk'))
print(factory.create_route('airplane', 'Kyiv', 'Dnipropetrovsk'))
print('----------------------------------------------------------------------------------')
factory = factory_producer.get_factory('diesh')
print(factory.create_route('diesh', 'Kyiv', 'Dnipropetrovsk'))


