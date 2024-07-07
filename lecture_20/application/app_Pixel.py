"""Create a pixel application that will be used in the tests below."""

import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")
logger = logging.getLogger(__name__) # or __file__


class Pixel:

    def __init__(self, red, green, blue):
        """Initialize the pixel with red, green and blue components."""
        if not 0 <= red <= 255 or not 0 <= green <= 255 or not 0 <= blue <= 255:
            logger.info(f'Exs(ValueError): Components must be in the range [0 .. 255]')
            raise ValueError('Components must be in the range [0 .. 255]')
        self.__red = red if isinstance(red, int) else int(red)
        self.__green = green if isinstance(green, int) else int(green)
        self.__blue = blue if isinstance(blue, int) else int(blue)

    def red(self):
        """Return value the red component of the pixel."""
        return int(self.__red)

    def green(self):
        """Return value the green component of the pixel."""
        return int(self.__green)

    def blue(self):
        """Return value the blue component of the pixel."""
        return int(self.__blue)

    def __add__(self, other):
        """Add the components of one pixel to the components of another pixel."""
        logger.info(f'Args(for__add__: [{repr(self)} | {repr(other)}]')
        if not isinstance(other, Pixel):
            logger.info(f'Result __add__ -> Exs(TypeError): Object "other" -> "{other}" is not a Pixel object')
            raise TypeError(f'Object "other" -> "{other}" is not a Pixel object')
        logger.info(
            f'Result __add__ -> {self.__red + other.__red if self.__red + other.__red <= 255 else 255}, '
            f'{self.__green + other.__green if self.__green + other.__green <= 255 else 255}, '
            f'{self.__blue + other.__blue if self.__blue + other.__blue <= 255 else 255}'
        )
        return Pixel(
            self.__red + other.__red if self.__red + other.__red <= 255 else 255,
            self.__green + other.__green if self.__green + other.__green <= 255 else 255,
            self.__blue + other.__blue if self.__blue + other.__blue <= 255 else 255
        )

    def __radd__(self, other):
        """Reflective addition of components of two images"""
        return self.__add__(other)

    def __sub__(self, other):
        """Subtract the components of one pixel with the components of another pixel"""
        logger.info(f'Args(for__sub__: [{repr(self)} | {repr(other)}]')
        if not isinstance(other, Pixel):
            logger.info(f'Result __sub__ -> Exs(TypeError): Object "other" -> "{other}" is not a Pixel object')
            raise TypeError(f'Object "other" -> "{other}" is not a Pixel object')
        logger.info(
            f'Result __sub__ -> {self.__red - other.__red if self.__red - other.__red >= 0 else 0}, '
            f'{self.__green - other.__green if self.__green - other.__green >= 0 else 0}, '
            f'{self.__blue - other.__blue if self.__blue - other.__blue >= 0 else 0}'
        )
        return Pixel(
            self.__red - other.__red if self.__red - other.__red >= 0 else 0,
            self.__green - other.__green if self.__green - other.__green >= 0 else 0,
            self.__blue - other.__blue if self.__blue - other.__blue >= 0 else 0
        )

    def __rsub__(self, other):
        """Reflective addition of components of two images"""
        return self.__sub__(other)

    def __mul__(self, other):
        """Multiplying pixel components with any value > 0"""
        logger.info(f'Args(for__mul__: [{repr(self)} | {repr(other)}]')
        if not isinstance(other, (int, float)):
            logger.info(f'Result __mul__ -> Exs(TypeError): Object "other" -> "{other}" is not type of int or float')
            raise TypeError(f'Object "other" -> "{other}" is not type of int or float')
        if other <= 0:
            logger.info(f'Result __mul__ -> Exs(ValueError): Object "other" -> "{other}" must be greater than 0')
            raise ValueError(f'Value "other" -> "{other}" must be greater than 0')
        logger.info(
            f'Result __mul__ -> {int(self.__red * other) if self.__red * other <= 255 else 255}, '
            f'{int(self.__green * other) if self.__green * other <= 255 else 255}, '
            f'{int(self.__blue * other) if self.__blue * other <= 255 else 255}'
        )
        return Pixel(
            self.__red * other if self.__red * other <= 255 else 255,
            self.__green * other if self.__green * other <= 255 else 255,
            self.__blue * other if self.__blue * other <= 255 else 255
        )

    def __rmul__(self, other):
        """Multiplying pixel components with any value > 0"""
        return self.__mul__(other)

    def __truediv__(self, other):
        """Divide pixel components by any value > 0"""
        logger.info(f'Args(for__truediv__: [{repr(self)} | {repr(other)}]')
        if not isinstance(other, (int, float)):
            logger.info(f'Result __truediv__ -> Exs(TypeError): Object "other" -> "{other}" is not type of int or float')
            raise TypeError(f'Object "other" -> "{other}" is not type of int or float')
        if other <= 0:
            logger.info(f'Result __truediv__ -> Exs(ValueError): Value "other" -> "{other}" must be greater than 0')
            raise ValueError(f'Value "other" -> "{other}" must be greater than 0')
        logger.info(
            f'Result __truediv__ -> {int(self.__red / other) if self.__red / other <= 255 else 255}, '
            f'{int(self.__green / other) if self.__green / other <= 255 else 255}, '
            f'{int(self.__blue / other) if self.__blue / other <= 255 else 255}'
        )
        return Pixel(
            self.__red / other if self.__red / other <= 255 else 255,
            self.__green / other if self.__green / other <= 255 else 255,
            self.__blue / other if self.__blue / other <= 255 else 255
        )

    def __eq__(self, other):
        """Compare the components of two pixels for equality"""
        logger.info(f'Args(for__eq__: [{repr(self)} | {repr(other)}]')
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


pix1 = Pixel(255, 255, 100)
pix2 = Pixel(1, 2, 4)

print(repr(pix1 + pix2))
print(repr(pix2 + pix1))
print(repr(pix1 - pix2))
print(repr(pix2 - pix1))
print(repr(pix1 * 2))
print(repr(2 * pix1))
print(repr(pix1 / 2))
print(repr(pix1 / 0.00009))
print(repr(pix2 / 9))
print(repr(pix1 == pix2))
print(repr(pix1 == pix1))


