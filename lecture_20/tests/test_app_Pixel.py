import pytest
from lecture_20.application.app_Pixel import Pixel
import sys
import re

#   In the lines of the document, I wrote the requirements for the Pixel class,
#   which were given in the homework for the lecture -> 14.
#   This file has 108 tests.


@pytest.mark.parametrize('pixel', [(1, 1, 1), (255, 255, 255), (0, 0, 0)])
def test_checks_creating_pixel(pixel):
    """
    1-> Create Pixel object with red, green and blue components."""
    assert Pixel(*pixel), 'Pixel is not created'


@pytest.mark.parametrize('pixel', [(1, 2, 255)])
def test_checks_len_pixel_object(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel."""
    assert sys.getsizeof(Pixel(*pixel)) == 56, 'Length Pixel is not 3 components'


@pytest.mark.parametrize('pixel', [(1, 255, 1), (255, 255, 0), (111, 2, 4)])
def test_checks_components_pixel_on_valid(pixel):
    """
    1-> Components of pixel are integer numbers in range [0 .. 255] (including boundaries)."""
    assert Pixel(*pixel).red() in range(256), 'Red component must be in the range [0 .. 255]'
    assert Pixel(*pixel).green() in range(256), 'Green component must be in the range [0 .. 255]'
    assert Pixel(*pixel).blue() in range(256), 'Blue component must be in the range [0 .. 255]'


@pytest.mark.parametrize('pixel', [(1, 255, 256), (-1, 255, 256), (111, 2, 256)])
def test_checks_components_pixel_on_invalid(pixel):
    """
    1-> When trying to create object with components out of this range, raise Value Error."""
    with pytest.raises(ValueError) as exc:
        Pixel(*pixel)
    assert str(exc.value) == 'Components must be in the range [0 .. 255]', 'Components Pixel is valid'
    assert isinstance(exc.value, ValueError), 'Components Pixel is valid'


###############################################################################################

@pytest.mark.parametrize('pixel', [(1, 255, 0), (0, 1, 255), (0, 1, 220)])
def test_checks_pixel_type(pixel):
    """
    1-> Pixel object is Pixel type."""
    assert isinstance(Pixel(*pixel), Pixel), 'Pixel is not Pixel object'


@pytest.mark.parametrize('pixel', [(1, 255, 1), (255, 255, 0), (111, 2, 4)])
def test_checks_components_on_valid_value_type(pixel):
    """
    1-> Components of pixel are integer numbers."""
    assert isinstance(Pixel(*pixel).red(), int), 'Red component is not a int type'
    assert isinstance(Pixel(*pixel).green(), int), 'Green component is not a int type'
    assert isinstance(Pixel(*pixel).blue(), int), 'Blue component is not a int type'


@pytest.mark.parametrize('pixel', [(1, 255, 10), (255, 255, 255), (0, 0, 0)])
def test_checks_components_on_valid_value(pixel):
    """
    1-> Components of pixel are integer numbers."""
    assert re.match(r'^\d+$', str(Pixel(*pixel).red())), 'Red component is not a digit'
    assert re.match(r'^\d+$', str(Pixel(*pixel).green())), 'Green component is not a digit'
    assert re.match(r'^\d+$', str(Pixel(*pixel).blue())), 'Blue component is not a digit'


##############################################################################################


@pytest.mark.parametrize('pixel', [(1, 1, 1), (2, 2, 2), (3, 3, 3)])
def test_checks_creating_valid_new_object_after_adding(pixel):
    """
    1-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum of corresponding components."""
    other_pixel = Pixel(1, 1, 1)
    new_pixel = Pixel(*pixel) + other_pixel
    assert isinstance(other_pixel, Pixel), f'{other_pixel} is not Pixel object'
    assert isinstance(new_pixel, Pixel), 'New object is not created after adding'
    assert new_pixel.red() == Pixel.red(Pixel(*pixel)) + other_pixel.red(), 'Red: The summation result does not meet the requirements'
    assert new_pixel.green() == Pixel.green(Pixel(*pixel)) + other_pixel.green(), 'Green: The summation result does not meet the requirements'
    assert new_pixel.blue() == Pixel.blue(Pixel(*pixel)) + other_pixel.blue(), 'Blue: The summation result does not meet the requirements'


@pytest.mark.parametrize('pixel', [(4, 4, 4), (5, 5, 5), (6, 6, 6)])
def test_checks_creating_valid_new_object_after_operation_radd(pixel):
    """
    1-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum of corresponding components."""
    other_pixel = Pixel(2, 2, 2)
    new_pixel = other_pixel + Pixel(*pixel)
    assert isinstance(other_pixel, Pixel), f'{other_pixel} is not Pixel object'
    assert isinstance(new_pixel, Pixel), 'New object is not created after adding'
    assert new_pixel.red() == other_pixel.red(), 'Red: The summation result does not meet the requirements'
    assert new_pixel.green() == other_pixel.green(), 'Green: The summation result does not meet the requirements'
    assert new_pixel.blue() == other_pixel.blue(), 'Blue: The summation result does not meet the requirements'


@pytest.mark.parametrize('pixel', [(7, 7, 7), (8, 8, 8), (9, 9, 9)])
def test_checks_creating_valid_new_object_after_subtracting(pixel):
    """
    1-> Adding/subtracting two pixels should result new Pixel object with components equal
    to difference of corresponding components."""
    other_pixel = Pixel(3, 3, 3)
    new_pixel = Pixel(*pixel) - other_pixel
    assert isinstance(other_pixel, Pixel), f'{other_pixel} is not Pixel object'
    assert isinstance(new_pixel, Pixel), 'New object is not created after subtracting'
    assert new_pixel.red() == Pixel.red(Pixel(*pixel)) - other_pixel.red(), 'Red: The subtraction result does not meet the requirements'
    assert new_pixel.green() == Pixel.green(Pixel(*pixel)) - other_pixel.green(), 'Green: The subtraction result does not meet the requirements'
    assert new_pixel.blue() == Pixel.blue(Pixel(*pixel)) - other_pixel.blue(), 'Blue: The subtraction result does not meet the requirements'


@pytest.mark.parametrize('pixel', [(10, 10, 10), (11, 11, 11), (12, 12, 12)])
def test_checks_creating_valid_new_object_after_operation_rsub(pixel):
    """
    1-> Adding/subtracting two pixels should result new Pixel object with components equal
    to difference of corresponding components."""
    other_pixel = Pixel(4, 4, 4)
    new_pixel = other_pixel - Pixel(*pixel)
    assert isinstance(other_pixel, Pixel), f'{other_pixel} is not Pixel object'
    assert isinstance(new_pixel, Pixel), 'New object is not created after subtracting'
    assert new_pixel.red() == other_pixel.red(), 'Red: The subtraction result does not meet the requirements'
    assert new_pixel.green() == other_pixel.green(), 'Green: The subtraction result does not meet the requirements'
    assert new_pixel.blue() == other_pixel.blue(), 'Blue: The subtraction result does not meet the requirements'

##############################################################################################


@pytest.fixture(params=[(2, 2, 2), (4, 4, 4), (6, 6, 6)])
def test_creating_pixel_object(request):
    return Pixel(*request.param)


def test_pixel_multiplied_by_valid_number_type_int(test_creating_pixel_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__.
    3-> New object should have all components multiplied/divided by number."""
    other = 2
    new_pixel = test_creating_pixel_object * other
    assert isinstance(other, int), f'{other} is not int'
    assert isinstance(new_pixel, Pixel), 'New object is not created after multiplying'
    assert new_pixel.red() == Pixel.red(test_creating_pixel_object), 'Red: Failed to multiply pixel components by number'
    assert new_pixel.green() == Pixel.green(test_creating_pixel_object), 'Green: Failed to multiply pixel components by number'
    assert new_pixel.blue() == Pixel.blue(test_creating_pixel_object), 'Blue: Failed to multiply pixel components by number'


def test_pixel_rmultiplied_by_valid_number_type_int(test_creating_pixel_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__.
    3-> New object should have all components multiplied/divided by number."""
    other = 3
    new_pixel = other * test_creating_pixel_object
    assert isinstance(other, int), f'{other} is not int '
    assert isinstance(new_pixel, Pixel), 'New object is not created after multiplying'
    assert new_pixel.red() == Pixel.red(test_creating_pixel_object), 'Red: Failed to multiply pixel components by number'
    assert new_pixel.green() == Pixel.green(test_creating_pixel_object), 'Green: Failed to multiply pixel components by number'
    assert new_pixel.blue() == Pixel.blue(test_creating_pixel_object), 'Blue: Failed to multiply pixel components by number'


def test_pixel_divided_by_valid_number_type_int(test_creating_pixel_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> New object should have all components multiplied/divided by number."""
    other = 1
    new_pixel = test_creating_pixel_object / other
    assert isinstance(other, int), f'{other} is not int'
    assert isinstance(new_pixel, Pixel), 'New object is not created after dividing'
    assert new_pixel.red() == Pixel.red(test_creating_pixel_object), 'Red: Failed to divide pixel components by number'
    assert new_pixel.green() == Pixel.green(test_creating_pixel_object), 'Green: Failed to divide pixel components by number'
    assert new_pixel.blue() == Pixel.blue(test_creating_pixel_object), 'Blue: Failed to divide pixel components by number'


def test_pixel_multiplied_by_valid_number_type_float(test_creating_pixel_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__.
    3-> New object should have all components multiplied/divided by number."""
    other = 2.7
    new_pixel = test_creating_pixel_object * other
    assert isinstance(other, float), f'{other} is not int or float'
    assert isinstance(new_pixel, Pixel), 'New object is not created after multiplying'
    assert new_pixel.red() == int(Pixel.red(test_creating_pixel_object)), 'Red: Failed to multiply pixel components by number'
    assert new_pixel.green() == int(Pixel.green(test_creating_pixel_object)), 'Green: Failed to multiply pixel components by number'
    assert new_pixel.blue() == int(Pixel.blue(test_creating_pixel_object)), 'Blue: Failed to multiply pixel components by number'


def test_pixel_rmultiplied_by_valid_number_type_float(test_creating_pixel_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__.
    3-> New object should have all components multiplied/divided by number."""
    other = 3.4
    new_pixel = other * test_creating_pixel_object
    assert isinstance(other, float), f'{other} is not int '
    assert isinstance(new_pixel, Pixel), 'New object is not created after multiplying'
    assert new_pixel.red() == int(Pixel.red(test_creating_pixel_object)), 'Red: Failed to multiply pixel components by number'
    assert new_pixel.green() == int(Pixel.green(test_creating_pixel_object)), 'Green: Failed to multiply pixel components by number'
    assert new_pixel.blue() == int(Pixel.blue(test_creating_pixel_object)), 'Blue: Failed to multiply pixel components by number'


def test_pixel_divided_by_valid_number_type_float(test_creating_pixel_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> New object should have all components multiplied/divided by number."""
    other = 1.1
    new_pixel = test_creating_pixel_object / other
    assert isinstance(other, float), f'{other} is not int'
    assert isinstance(new_pixel, Pixel), 'New object is not created after dividing'
    assert new_pixel.red() == int(Pixel.red(test_creating_pixel_object)), 'Red: Failed to divide pixel components by number'
    assert new_pixel.green() == int(Pixel.green(test_creating_pixel_object)), 'Green: Failed to divide pixel components by number'
    assert new_pixel.blue() == int(Pixel.blue(test_creating_pixel_object)), 'Blue: Failed to divide pixel components by number'


##############################################################################################


def test_pixel_multiplied_by_invalid_number_type(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = 'b'
    with pytest.raises(TypeError) as exc:
        test_creating_pixel_object * other
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


def test_pixel_multiplied_by_invalid_number_type_list(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = [1, 2, 3]
    with pytest.raises(TypeError) as exc:
        test_creating_pixel_object * other
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


def test_pixel_rmultiplied_by_invalid_number_type(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = '0'
    with pytest.raises(TypeError) as exc:
        other * test_creating_pixel_object
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


def test_pixel_rmultiplied_by_invalid_number_type_list(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = [5, 'h', 3]
    with pytest.raises(TypeError) as exc:
        other * test_creating_pixel_object
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


def test_pixel_divided_by_invalid_number_type(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = 'g'
    with pytest.raises(TypeError) as exc:
        test_creating_pixel_object / other
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


def test_pixel_divided_by_invalid_number_type_list(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = ['a', 2, (3, 5)]
    with pytest.raises(TypeError) as exc:
        test_creating_pixel_object / other
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


##############################################################################################


def test_pixel_multiplied_by_invalid_number_value_is_zero(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = 0
    with pytest.raises(ValueError) as exc:
        test_creating_pixel_object * other
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


def test_pixel_multiplied_by_invalid_number_value_less_than_zero(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = -1
    with pytest.raises(ValueError) as exc:
        test_creating_pixel_object * other
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


def test_pixel_rmultiplied_by_invalid_number_value_is_zero(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = 0
    with pytest.raises(ValueError) as exc:
        other * test_creating_pixel_object
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


def test_pixel_rmultiplied_by_invalid_number_value_less_than_zero(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = -1
    with pytest.raises(ValueError) as exc:
        other * test_creating_pixel_object
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


def test_pixel_divided_by_invalid_number_value_is_zero(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = 0
    with pytest.raises(ValueError) as exc:
        test_creating_pixel_object / other
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


def test_pixel_divided_by_invalid_number_value_less_than_zero(test_creating_pixel_object):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = -1
    with pytest.raises(ValueError) as exc:
        test_creating_pixel_object / other
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


##############################################################################################


@pytest.mark.parametrize('pixel', [(1, 1, 1)])
def test_check_the_resulting_component_for_type_after_multiplication(pixel):
    """
    1-> If resulting components are fractional, fractional part should be discarded"""
    other = 2.7
    new_pixel = Pixel(*pixel) * other
    assert isinstance(new_pixel.red(), int), 'Red component is not int'
    assert isinstance(new_pixel.green(), int), 'Green component is not int'
    assert isinstance(new_pixel.blue(), int), 'Blue component is not int'


@pytest.mark.parametrize('pixel', [(2, 2, 2)])
def test_check_the_resulting_component_for_type_after_rmultiplication(pixel):
    """
    1-> If resulting components are fractional, fractional part should be discarded"""
    other = 5.4
    new_pixel = other * Pixel(*pixel)
    assert isinstance(new_pixel.red(), int), 'Red component is not int'
    assert isinstance(new_pixel.green(), int), 'Green component is not int'
    assert isinstance(new_pixel.blue(), int), 'Blue component is not int'


@pytest.mark.parametrize('pixel', [(3, 3, 3)])
def test_check_the_resulting_component_for_type_after_division(pixel):
    """
    1-> If resulting components are fractional, fractional part should be discarded"""
    other = 1.1
    new_pixel = Pixel(*pixel) / other
    assert isinstance(new_pixel.red(), int), 'Red component is not int'
    assert isinstance(new_pixel.green(), int), 'Green component is not int'
    assert isinstance(new_pixel.blue(), int), 'Blue component is not int'


##############################################################################################


@pytest.mark.parametrize('pixel', [(4, 4, 4), (5, 5, 5), (6, 6, 6)])
def test_check_the_resulting_component_for_type_after_subtraction(pixel):
    """
    1-> If resulting component is less then zero, it should be set to 0."""
    other_pixel = Pixel(7, 7, 7)
    new_pixel = Pixel(*pixel) - other_pixel
    assert new_pixel.red() == 0, 'Red component is not 0'
    assert new_pixel.green() == 0, 'Green component is not 0'
    assert new_pixel.blue() == 0, 'Blue component is not 0'


@pytest.mark.parametrize('pixel', [(7, 7, 7), (8, 8, 8), (9, 9, 9)])
def test_check_the_resulting_component_for_type_after_division(pixel):
    """
    1-> If resulting component is less then zero, it should be set to 0."""
    other = 15
    new_pixel = Pixel(*pixel) / other
    assert new_pixel.red() == 0, 'Red component is not 0'
    assert new_pixel.green() == 0, 'Green component is not 0'
    assert new_pixel.blue() == 0, 'Blue component is not 0'


##############################################################################################


@pytest.fixture(params=[(255, 254, 253), (252, 251, 250), (240, 248, 247)])
def test_creating_pixel_object2(request):
    return Pixel(*request.param)


def test_check_the_resulting_component_for_type_after_adding(test_creating_pixel_object2):
    """
    1-> If resulting component is greater then 255, it should be set to 255."""
    other_pixel = Pixel(255, 250, 255)
    new_pixel = test_creating_pixel_object2 + other_pixel
    assert new_pixel.red() == 255, 'Red component is not 255'
    assert new_pixel.green() == 255, 'Green component is not 255'
    assert new_pixel.blue() == 255, 'Blue component is not 255'


def test_check_the_resulting_component_for_type_after_radding(test_creating_pixel_object2):
    """
    1-> If resulting component is greater then 255, it should be set to 255."""
    other_pixel = Pixel(255, 250, 255)
    new_pixel = other_pixel + test_creating_pixel_object2
    assert new_pixel.red() == 255, 'Red component is not 255'
    assert new_pixel.green() == 255, 'Green component is not 255'
    assert new_pixel.blue() == 255, 'Blue component is not 255'


def test_check_the_resulting_component_for_type_after_mul(test_creating_pixel_object2):
    """
    1-> If resulting component is greater then 255, it should be set to 255."""
    other = 2
    new_pixel = test_creating_pixel_object2 * other
    assert new_pixel.red() == 255, 'Red component is not 255'
    assert new_pixel.green() == 255, 'Green component is not 255'
    assert new_pixel.blue() == 255, 'Blue component is not 255'


def test_check_the_resulting_component_for_type_after_rmul(test_creating_pixel_object2):
    """
    1-> If resulting component is greater then 255, it should be set to 255."""
    other = 3
    new_pixel = other * test_creating_pixel_object2
    assert new_pixel.red() == 255, 'Red component is not 255'
    assert new_pixel.green() == 255, 'Green component is not 255'
    assert new_pixel.blue() == 255, 'Blue component is not 255'

##############################################################################################


@pytest.mark.parametrize('pixel', [(255, 254, 253)])
def test_checks_eq_two_object_type_pixel(pixel):
    """
    1-> Two objects with equal components considered to be equal."""
    other_pixel_true = Pixel(255, 254, 253)
    other_pixel_false = Pixel(255, 255, 255)
    assert Pixel(*pixel) == other_pixel_true, 'Objects are not equal'
    assert Pixel(*pixel) != other_pixel_false, 'Objects are equal'


##############################################################################################

@pytest.mark.parametrize('pixel', [(255, 0, 1)])
def test_checks_str_pixel_object(pixel):
    """
    1-> Method __str__ should return string like (\t - tabulation symbol"""
    assert re.match(r'^\tRed: \d+\n\tGreen: \d+\n\tBlue: \d+$', str(Pixel(*pixel))), 'String is not valid'


@pytest.mark.parametrize('pixel', [(255, 0, 1)])
def test_checks_repr_pixel_object(pixel):
    """
    1-> Method __repr__ should return string with constructor call."""
    assert re.match(r'^\d+, \d+, \d+$', repr(Pixel(*pixel))), 'String is not valid'
