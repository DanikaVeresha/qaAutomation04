"""Create a pixel application that will be used in the tests below."""


class Pixel:

    def __init__(self, red, green, blue):
        """Initialize the pixel with red, green and blue components."""
        if not 0 <= red <= 255 or not 0 <= green <= 255 or not 0 <= blue <= 255:
            raise ValueError('Components must be in the range [0 .. 255]')
        self.__red = red if isinstance(red, int) else int(red)
        self.__green = green if isinstance(green, int) else int(green)
        self.__blue = blue if isinstance(blue, int) else int(blue)

    def red(self):
        """Return value the red component of the pixel."""
        return self.__red

    def green(self):
        """Return value the green component of the pixel."""
        return self.__green

    def blue(self):
        """Return value the blue component of the pixel."""
        return self.__blue

    def __add__(self, other):
        """Add the components of one pixel to the components of another pixel."""
        if not isinstance(other, Pixel):
            return f'Object "other" -> "{other}" is not a Pixel object'
        self.__red = 255 if self.__red + other.__red > 255 else self.__red + other.__red
        self.__green = 255 if self.__green + other.__green > 255 else self.__green + other.__green
        self.__blue = 255 if self.__blue + other.__blue > 255 else self.__blue + other.__blue

        return Pixel(self.__red, self.__green, self.__blue)

    def __sub__(self, other):
        """Subtract the components of one pixel with the components of another pixel"""
        if not isinstance(other, Pixel):
            return f'Object "other" -> "{other}" is not a Pixel object'
        self.__red = 0 if self.__red - other.__red <= 0 else self.__red - other.__red
        self.__green = 0 if self.__green - other.__green <= 0 else self.__green - other.__green
        self.__blue = 0 if self.__blue - other.__blue <= 0 else self.__blue - other.__blue

        return Pixel(self.__red, self.__green, self.__blue)

    def __mul__(self, other):
        """Multiplying pixel components with any value > 0"""
        if not isinstance(other, (int, float)):
            return f'Object "other" -> "{other}" is not type of int or float'
        if other <= 0:
            return f'Value "other" -> "{other}" must be greater than 0'
        self.__red = 255 if self.__red * other > 255 else self.__red * other
        self.__green = 255 if self.__green * other > 255 else self.__green * other
        self.__blue = 255 if self.__blue * other > 255 else self.__blue * other

        return Pixel(self.__red, self.__green, self.__blue)

    def __rmul__(self, other):
        """Multiply by any value > 0 with pixel components"""
        return self.__mul__(other)

    def __truediv__(self, other):
        """Divide pixel components by any value > 0"""
        if not isinstance(other, (int, float)):
            return f'Object "other" -> "{other}" is not type of int or float'
        if other <= 0:
            return f'Value "other" -> "{other}" must be greater than 0'
        self.__red = 255 if self.__red / other > 255 else self.__red / other
        self.__green = 255 if self.__green / other > 255 else self.__green / other
        self.__blue = 255 if self.__blue / other > 255 else self.__blue / other

        return Pixel(self.__red, self.__green, self.__blue)

    def __rtruediv__(self, other):
        """Divide by any value > 0 with pixel components"""
        if not isinstance(other, (int, float)):
            return f'Object "other" -> "{other}" is not type of int or float'
        elif other <= 0:
            return f'Value "other" -> "{other}" must be greater than 0'
        elif self.__red == 0 or self.__green == 0 or self.__blue == 0:
            return f'Some pixel component is zero'
        self.__red = 255 if other / self.__red > 255 else other / self.__red
        self.__green = 255 if other / self.__green > 255 else other / self.__green
        self.__blue = 255 if other / self.__blue > 255 else other / self.__blue

        return Pixel(self.__red, self.__green, self.__blue)

    def __eq__(self, other):
        """Compare the components of two pixels for equality"""
        if not isinstance(other, Pixel):
            return f'Object "other" -> "{other}" is not a Pixel object'
        return self.__red == other.__red and self.__green == other.__green and self.__blue == other.__blue

    def __str__(self):
        """Return the pixel object in string format."""
        return f'\tRed: {self.__red}\n' \
               f'\tGreen: {self.__green}\n' \
               f'\tBlue: {self.__blue}' \


    def __repr__(self):
        """Return the pixel object."""
        return f'{self.__red}, {self.__green}, {self.__blue}'


pix1 = Pixel(0, 0, 255)
pix2 = Pixel(255, 0, 0)
pix3 = Pixel(1, 255, 1)

print(f'Pixel 1:\t\n{pix1}')
print(f'Pixel 2:\n\t{repr(pix2)}')
print(f'Pixel 3:\n\t{repr(pix3)}')

print(f'__add__/pix1, pix2/: -> {repr(pix1 + pix2)}')
print(f'__sub__/pix1, pix2/: -> {repr(pix1 - pix2)}')

print(f'__mul__/pix1, 2/: -> {repr(pix1 * 2)}')
print(f'__rmul__/2, pix1/: -> {repr(2 * pix1)}')
print(f'__mul__/pix1, b/: -> {repr(pix1 * "b")}')
print(f'__rmul__/b, pix1/: -> {repr("b" * pix1)}')

print(f'__truediv__/pix2, 2/: -> {repr(pix2 / 2)}')
print(f'__rtruediv__/2, pix2/: -> {repr(2 / pix2)}')
print(f'__truediv__/pix2, b/: -> {repr(pix2 / "b")}')
print(f'__rtruediv__/b, pix2/: -> {repr("b" / pix2)}')
print(f'__rtruediv__/2, pix3/: -> {repr(2 / pix3)}')

print(f'__eq__/pix1, pix2/: -> {repr(pix1 == pix2)}')
print(f'__eq__/pix1, pix1/: -> {repr(pix1 == Pixel(0, 0, 255))}')
print(f'__eq__/pix1, 1/: -> {repr(pix1 == 1)}')




