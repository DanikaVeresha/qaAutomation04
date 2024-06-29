"""Create a pixel application that will be used in the tests below."""
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")
logger = logging.getLogger(__name__)


class Pixel:

    def __init__(self, red, green, blue):
        """Initialize the pixel with red, green and blue components."""
        if not 0 <= red <= 255 or not 0 <= green <= 255 or not 0 <= blue <= 255:
            logger.info(f'Exs(ValueError): Components must be in the range [0 .. 255]')
            raise ValueError('Components must be in the range [0 .. 255]')
        self.__red = red if isinstance(red, int) else int(red)
        self.__green = green if isinstance(green, int) else int(green)
        self.__blue = blue if isinstance(blue, int) else int(blue)
        logger.info(f'Pixel object created Pixel [{self.__red}, {self.__green}, {self.__blue}]')

    def red(self):
        """Return value the red component of the pixel."""
        logger.info(f'Function red returned value [{self.__red}]')
        return self.__red

    def green(self):
        """Return value the green component of the pixel."""
        logger.info(f'Function green returned value [{self.__green}]')
        return self.__green

    def blue(self):
        """Return value the blue component of the pixel."""
        logger.info(f'Function blue returned value [{self.__blue}]')
        return self.__blue

    def __add__(self, other):
        """Add the components of one pixel to the components of another pixel."""
        if not isinstance(other, Pixel):
            logger.info(f'Result __add__ -> Exs(TypeError): Object "other" -> "{other}" is not a Pixel object')
            raise TypeError(f'Object "other" -> "{other}" is not a Pixel object')
        self.__red = 255 if self.__red + other.__red >= 255 else self.__red + other.__red or \
            0 if self.__red + other.__red <= 0 else self.__red + other.__red
        self.__green = 255 if self.__green + other.__green >= 255 else self.__green + other.__green or \
            0 if self.__green + other.__green <= 0 else self.__green + other.__green
        self.__blue = 255 if self.__blue + other.__blue >= 255 else self.__blue + other.__blue or \
            0 if self.__blue + other.__blue <= 0 else self.__blue + other.__blue
        logger.info(f'Result __add__ -> {self.__red}, {self.__green}, {self.__blue} ')
        return Pixel(self.__red, self.__green, self.__blue)

    def __radd__(self, other):
        """Add the components of one pixel to the components of another pixel."""
        logger.info(f'Result __radd__ -> {self.__red}, {self.__green}, {self.__blue} ')
        return other.__add__(self)

    def __sub__(self, other):
        """Subtract the components of one pixel with the components of another pixel"""
        if not isinstance(other, Pixel):
            logger.info(f'Result __sub__ -> Exs(TypeError): Object "other" -> "{other}" is not a Pixel object')
            raise TypeError(f'Object "other" -> "{other}" is not a Pixel object')
        self.__red = 0 if self.__red - other.__red <= 0 else self.__red - other.__red or \
            255 if self.__red - other.__red >= 255 else self.__red - other.__red
        self.__green = 0 if self.__green - other.__green <= 0 else self.__green - other.__green or \
            255 if self.__green - other.__green >= 255 else self.__green - other.__green
        self.__blue = 0 if self.__blue - other.__blue <= 0 else self.__blue - other.__blue or \
            255 if self.__blue - other.__blue >= 255 else self.__blue - other.__blue
        logger.info(f'Result __sub__ -> {self.__red}, {self.__green}, {self.__blue} ')
        return Pixel(self.__red, self.__green, self.__blue)

    def __rsub__(self, other):
        """Subtract the components of one pixel with the components of another pixel"""
        logger.info(f'Result __rsub__ -> {self.__red}, {self.__green}, {self.__blue} ')
        return other.__sub__(self)

    def __mul__(self, other):
        """Multiplying pixel components with any value > 0"""
        if not isinstance(other, (int, float)):
            logger.info(f'Result __mul__ -> Exs(TypeError): Object "other" -> "{other}" is not type of int or float')
            raise TypeError(f'Object "other" -> "{other}" is not type of int or float')
        if other <= 0:
            logger.info(f'Result __mul__ -> Exs(ValueError): Object "other" -> "{other}" must be greater than 0')
            raise ValueError(f'Value "other" -> "{other}" must be greater than 0')
        self.__red = 255 if self.__red * other >= 255 else self.__red * other or \
            0 if self.__red * other <= 0 else self.__red * other
        self.__green = 255 if self.__green * other >= 255 else self.__green * other or \
            0 if self.__green * other <= 0 else self.__green * other
        self.__blue = 255 if self.__blue * other >= 255 else self.__blue * other or \
            0 if self.__blue * other <= 0 else self.__blue * other
        logger.info(f'Result __mul__ -> {self.__red}, {self.__green}, {self.__blue} ')
        return Pixel(self.__red, self.__green, self.__blue)

    def __rmul__(self, other):
        """Multiplying pixel components with any value > 0"""
        logger.info(f'Result __rmul__ -> {self.__red}, {self.__green}, {self.__blue} ')
        return self.__mul__(other)

    def __truediv__(self, other):
        """Divide pixel components by any value > 0"""
        if not isinstance(other, (int, float)):
            logger.info(f'Result __truediv__ -> Exs(TypeError): Object "other" -> "{other}" is not type of int or float')
            raise TypeError(f'Object "other" -> "{other}" is not type of int or float')
        if other <= 0:
            logger.info(f'Result __truediv__ -> Exs(ValueError): Value "other" -> "{other}" must be greater than 0')
            raise ValueError(f'Value "other" -> "{other}" must be greater than 0')
        self.__red = 0 if self.__red / other <= 0 else self.__red / other or \
            255 if self.__red / other >= 255 else self.__red / other
        self.__green = 0 if self.__green / other <= 0 else self.__green / other or \
            255 if self.__green / other >= 255 else self.__green / other
        self.__blue = 0 if self.__blue / other <= 0 else self.__blue / other or \
            255 if self.__blue / other >= 255 else self.__blue / other
        logger.info(f'Result __truediv__ -> {self.__red}, {self.__green}, {self.__blue} ')
        return Pixel(self.__red, self.__green, self.__blue)

    def __eq__(self, other):
        """Compare the components of two pixels for equality"""
        if not isinstance(other, Pixel):
            logger.info(f'Result __eq__ -> Exs(TypeError): Object "other" -> "{other}" is not a Pixel object')
            raise TypeError(f'Object "other" -> "{other}" is not a Pixel object')
        logger.info(f'Result __eq__ -> {self.__red == other.__red and self.__green == other.__green and self.__blue == other.__blue}')
        return self.__red == other.__red and self.__green == other.__green and self.__blue == other.__blue

    def __str__(self):
        """Return the pixel object in string format."""
        return f'\tRed: {self.__red}\n' \
               f'\tGreen: {self.__green}\n' \
               f'\tBlue: {self.__blue}' \


    def __repr__(self):
        """Return the pixel object."""
        return f'{self.__red}, {self.__green}, {self.__blue}'


pix1 = Pixel(0, 0, 0)
pix2 = Pixel(1, 1, 1)

pix3 = Pixel(2, 2, 2)
pix4 = Pixel(3, 3, 3)

pix5 = Pixel(4, 4, 4)
pix6 = Pixel(5, 5, 5)

pix7 = Pixel(6, 6, 6)
pix8 = Pixel(7, 7, 7)

pix9 = Pixel(8, 8, 8)
pix10 = Pixel(9, 9, 9)

pix11 = Pixel(10, 10, 10)
pix12 = Pixel(11, 11, 11)

pix13 = Pixel(12, 12, 12)

pix14 = Pixel(255, 255, 255)


print(f'Pixel 1:\t\n{pix1}')
print(f'Pixel 2:\n\t{repr(pix2)}')

print(f'__add__/pix1, pix2/: -> {repr(pix1 + pix2)}')
print(f'__radd__/pix3, pix4/: -> {repr(pix4 + pix3)}')
print(f'__sub__/pix5, pix6/: -> {repr(pix5 - pix6)}')
print(f'__rsub__/pix7, pix8/: -> {repr(pix8 - pix7)}')

print(f'__mul__/pix9, 2/: -> {repr(pix9 * 2)}')
print(f'__rmul__/2, pix10/: -> {repr(2 * pix10)}')
# print(f'__mul__/pix9, b/: -> {repr(pix9 * "b")}') # TypeError
# print(f'__rmul__/b, pix10/: -> {repr("b" * pix10)}') # TypeError
# print(f'__mul__/pix11, 0/: -> {repr(pix11 * 0)}') # ValueError
# print(f'__rmul__/2, pix12/: -> {repr(0 * pix12)}') # ValueError

print(f'__truediv__/pix13, 2/: -> {repr(pix13 / 2)}')
# print(f'__truediv__/pix11, b/: -> {repr(pix11 / "b")}') # TypeError

print(f'__eq__/pix14, [1, 1, 1]/: -> {repr(pix14 == Pixel(1, 1, 1))}')
print(f'__eq__/pix14, [255, 255, 255]/: -> {repr(pix14 == Pixel(255, 255, 255))}')
# print(f'__eq__/pix1, 1/: -> {repr(pix1 == 1)}') # TypeError

print(f'__add__/pix1, pix14/: -> {repr(pix1 + pix14)}')
print(f'__radd__/pix14, pix1/: -> {repr(pix14 + pix1)}')

print(f'__sub__/pix1, pix14/: -> {repr(pix1 - pix14)}')
print(f'__rsub__/pix2, pix14/: -> {repr(pix2 - pix14)}')

print(f'__mul__/pix14, 2/: -> {repr(pix14 * 2)}')
print(f'__rmul__/2, pix14/: -> {repr(2 * pix14)}')




