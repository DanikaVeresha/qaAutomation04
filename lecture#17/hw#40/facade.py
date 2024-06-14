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
        return (self._airplane.the_plane_took_off(),
                self._car.the_car_started(),
                self._train.the_train_departed())


if __name__ == '__main__':
    facade = Facade()
    for info in facade.get_all_info():
        print(info)
        print('----------------------------------------------------------------------------------')
