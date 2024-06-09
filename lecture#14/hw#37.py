"""Task 37."""
from __future__ import division


class Pixel:

    def __init__(self, red, green, blue):
        if not 0 <= red <= 255 or not 0 <= green <= 255 or not 0 <= blue <= 255:
            raise ValueError('Components must be in the range [0 .. 255]')
        self.__red = red if isinstance(red, int) else int(red)
        self.__green = green if isinstance(green, int) else int(green)
        self.__blue = blue if isinstance(blue, int) else int(blue)

    @property
    def red(self):
        """Getter for red component."""
        return self.__red

    @property
    def green(self):
        """Getter for green component."""
        return self.__green

    @property
    def blue(self):
        """Getter for blue component."""
        return self.__blue

    def __add__(self, other):
        """Sum of two pixels."""
        self.__red = 255 if self.__red + other.__red > 255 else self.__red + other.__red
        self.__green = 255 if self.__green + other.__green > 255 else self.__green + other.__green
        self.__blue = 255 if self.__blue + other.__blue > 255 else self.__blue + other.__blue

        return Pixel(self.__red, self.__green, self.__blue)

    def __sub__(self, other):
        """Subtraction of two pixels."""
        self.__red = 0 if self.__red - other.__red < 0 else self.__red - other.__red
        self.__green = 0 if self.__green - other.__green < 0 else self.__green - other.__green
        self.__blue = 0 if self.__blue - other.__blue < 0 else self.__blue - other.__blue

        return Pixel(self.__red, self.__green, self.__blue)

    def __mul__(self, other):
        """Multiplication of a pixel by a number."""
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError('The number must be greater than zero')
            self.__red = 255 if self.__red * other > 255 else self.__red * other
            self.__green = 255 if self.__green * other > 255 else self.__green * other
            self.__blue = 255 if self.__blue * other > 255 else self.__blue * other

            return Pixel(self.__red, self.__green, self.__blue)
        raise TypeError('The number must be an integer or a floating point number')

    def __rmul__(self, other):
        """Multiplication of a pixel by a number."""
        return self.__mul__(other)

    def __truediv__(self, other):
        """Division of a pixel by a number."""
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError('The number must be greater than zero')
            elif self.__red == 0 or self.__green == 0 or self.__blue == 0:
                raise ValueError('The pixel components must be greater than zero')
            elif self.__red / other > 255 or self.__green / other > 255 or self.__blue / other > 255:
                return Pixel(255, 255, 255)

            return Pixel(self.__red / other, self.__green / other, self.__blue / other)
        raise TypeError('The number must be an integer or a floating point number')

    def __rtruediv__(self, other):
        """Division of a number by pixel."""
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError('The number must be greater than zero')
            elif self.__red == 0 or self.__green == 0 or self.__blue == 0:
                raise ValueError('The pixel components must be greater than zero')
            elif other / self.__red > 255 or other / self.__green > 255 or other / self.__blue > 255:
                return Pixel(255, 255, 255)

            return Pixel(other / self.__red, other / self.__green, other / self.__blue)

    def __eq__(self, other):
        """Comparison of two pixels."""
        if not isinstance(other, Pixel):
            return False
        return self.__red == other.__red and self.__green == other.__green and self.__blue == other.__blue

    def __str__(self):
        """String representation of a pixel."""
        return f'\tRed: {self.__red}\n' \
               f'\tGreen: {self.__green}\n' \
               f'\tBlue: {self.__blue}' \


    def __repr__(self):
        """Representation of a pixel."""
        return f'Pixel({self.__red}, {self.__green}, {self.__blue})'


# Tests
pixel1 = Pixel(255.00, 0, 0)
pixel2 = Pixel(255.00, 0, 0)

pixel3 = Pixel(255, 0, 187.78)
pixel4 = Pixel(0.9999, 10, 80)

pixel5 = Pixel(102, 103, 0)

pixel6 = Pixel(255, 255, 10)

pixel7 = Pixel(1, 2, 0)
pixel8 = Pixel(10.01, 11, 12)
pixel9 = Pixel(10.01, 11, 12)

print('--------------------str object-------------')
print(str(pixel1))
print('--------------------repr object------------')
print(repr(pixel2))
print(repr(pixel3))
print(repr(pixel4))
print(repr(pixel5))
print(repr(pixel6))
print(repr(pixel7))
print(repr(pixel8))
print(repr(pixel9))
print('--------------------sum--------------------')
print(repr(pixel1 + pixel2))
print('--------------------sub--------------------')
print(repr(pixel3 - pixel4))
print('--------------------mul--------------------')
print(repr(pixel5 * 2.5))
print(repr(2.5 * pixel5))
print('--------------------mul--------------------')
# print(repr('b' * pixel5))
print('--------------------div--------------------')
print(repr(pixel6 / 255))
print(repr(255 / pixel6))
print('--------------------eq---------------------')
print(repr(pixel7 == pixel8))
print(repr(pixel8 == pixel9))
print(repr(pixel1 == 'pixel2'))
print(repr(pixel1 == 123))
print('-------------------------------------------')
# print(repr(id(pixel5)))
# print(repr(id(pixel5 * 2.5)))
