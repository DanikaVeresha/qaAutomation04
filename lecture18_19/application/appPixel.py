"""Create a pixel application that, based on the entered number of pixels,
will determine the color of the pixel"""


class Pixel:
    """Initialize the application."""

    def __init__(self, x, y, z):
        """Initialize the application."""
        self.x = x
        self.y = y
        self.z = z
        self.pixels = []

    @staticmethod
    def list_pixels():
        """List the pixels."""
        pixel = {
            '255, 255, 0': 'red',
            '0, 0, 255': 'blue',
            '0, 255, 0': 'green',
            '0, 0, 0': 'black',
            '255, 255, 255': 'white'
        }
        return pixel

    def get_color(self):
        """Get the color of the pixel."""
        for item in self.list_pixels():
            if item == f'{self.x}, {self.y}, {self.z}':
                self.pixels.append(f'{self.list_pixels()[item]} -> {item}')
                return self.list_pixels()[item]
        return 'Unknown color'


# obj1 = Pixel('0', '0', '255')
# obj2 = Pixel('255', '255', '0')
# obj3 = Pixel('0', '255', '0')
# obj4 = Pixel('0', '0', '0')
# obj5 = Pixel('255', '255', '255')
# obj6 = Pixel('255', '255', '256')
#
# print(obj1.get_color())
# print(obj2.get_color())
# print(obj3.get_color())
# print(obj4.get_color())
# print(obj5.get_color())
# print(obj6.get_color())
#
# print(obj1.pixels)
# print(obj2.pixels)
