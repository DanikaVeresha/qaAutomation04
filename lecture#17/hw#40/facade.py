"""This module contains the Facade class."""

from airplane import Airplane
from car import Car
from train import Train


class Facade:

    def __init__(self):
        self._airplane = Airplane('New York', 'Los Angeles')
        self._car = Car('New York', 'Los Angeles')
        self._train = Train('New York', 'Los Angeles')

    def get_all_info(self):
        """Get all information about transportation."""
        return (
            self._airplane.execute_the_request.__doc__,
            self._airplane.execute_the_request(),
            self._car.execute_the_request.__doc__,
            self._car.execute_the_request(),
            self._train.execute_the_request.__doc__,
            self._train.execute_the_request()
        )

if __name__ == '__main__':
    facade = Facade()
    for info in facade.get_all_info():
        print(info)
        print('----------------------------------------------------------------------------------')
