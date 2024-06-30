import pytest
from lecture_20.application.app_Pixel import Pixel
import re

#   In the lines of the document, I wrote the requirements for the Pixel class,
#   which were given in the homework for the lecture -> 14.
#   This file has 123 tests.


@pytest.mark.parametrize('pixel', [(0, 1, 255)])
def test_creating_pixel(pixel):
    """
    1-> Create Pixel object with red, green and blue components."""
    assert Pixel(*pixel) == Pixel(0, 1, 255), 'Pixel object is not created'
    assert isinstance(Pixel(*pixel), Pixel), 'Pixel is not Pixel object'


@pytest.mark.parametrize('pixel', [(1, 2, 255)])
def test_len_pixel_object(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel."""
    assert len(Pixel(*pixel).__dict__) == 3, 'Pixel object does not have 3 components'


@pytest.mark.parametrize('pixel', [(255, 255, 0)])
def test_presence_of_red_green_blue_component_in_the_object(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel."""
    assert Pixel(*pixel).__dict__ == {'_Pixel__red': 255, '_Pixel__green': 255, '_Pixel__blue': 0}, \
        'Pixel object does not have red, green, blue components'


@pytest.mark.parametrize('pixel', [(-1, 256, -10), (257, 288, 310)])
def test_components_pixel_in_range_0_255(pixel):
    """
    1-> When trying to create object with components out of this range, raise Value Error."""
    with pytest.raises(ValueError) as exc:
        Pixel(*pixel)
    assert str(exc.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is valid'


################################################################################################

@pytest.fixture(params=[(1, 255, 0), (180, 11, 56), (111, 2, 4)])
def pixel_object_for_testing_components_type(request):
    return Pixel(*request.param)


def test_components_are_int_type(pixel_object_for_testing_components_type):
    """
    1-> Components of pixel are integer numbers."""
    assert isinstance(pixel_object_for_testing_components_type.red(), int), \
        'Red component is not int'
    assert isinstance(pixel_object_for_testing_components_type.green(), int), \
        'Green component is not int'
    assert isinstance(pixel_object_for_testing_components_type.blue(), int), \
        'Blue component is not int'


def test_components_are_numbers(pixel_object_for_testing_components_type):
    """
    1-> Components of pixel are integer numbers."""
    assert re.match(r'^\d+$', str(pixel_object_for_testing_components_type.red())), \
        'Red component is not number'
    assert re.match(r'^\d+$', str(pixel_object_for_testing_components_type.green())), \
        'Green component is not number'
    assert re.match(r'^\d+$', str(pixel_object_for_testing_components_type.blue())), \
        'Blue component is not number'

###############################################################################################


@pytest.mark.parametrize('pixel', [(0, 0, 0)])   # Limit values
@pytest.mark.parametrize('other_pixel', [(0, 0, 0)])
def test_operation_adding_limit_values_0(pixel, other_pixel):
    """
    1-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum of corresponding components.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__."""
    pixel_result = Pixel(*pixel) + Pixel(*other_pixel)
    assert pixel_result.red() == 0, \
        f'Red component not in range [0-255] -> {pixel_result.red() != 0}'
    assert pixel_result.green() == 0, \
        f'Green component not in range [0-255] -> {pixel_result.green() != 0}'
    assert pixel_result.blue() == 0, \
        f'Blue component not in range [0-255] -> {pixel_result.blue() != 0}'


@pytest.mark.parametrize('pixel', [(128, 4, 1)])  # Limit values
@pytest.mark.parametrize('other_pixel', [(127, 251, 254)])
def test_operation_adding_limit_values_255(pixel, other_pixel):
    """
    1-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum of corresponding components.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__."""
    pixel_result = Pixel(*pixel) + Pixel(*other_pixel)
    assert pixel_result.red() == 255, \
        f'Red component not in range [0-255] -> {pixel_result.red() != 255}'
    assert pixel_result.green() == 255, \
        f'Green component not in range [0-255] -> {pixel_result.green() != 255}'
    assert pixel_result.blue() == 255, \
        f'Blue component not in range [0-255] -> {pixel_result.blue() != 255}'


@pytest.mark.parametrize('pixel', [(1, 130, 255)])  # Equivalence partitioning
@pytest.mark.parametrize('other_pixel', [(255, 128, 2)])
def test_operation_adding_equivalence_partitioning(pixel, other_pixel):
    """
    1-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum of corresponding components.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__."""
    pixel_result = Pixel(*pixel) + Pixel(*other_pixel)
    assert pixel_result.red() == 255, \
        f'Red component out of range [0-255] -> {pixel_result.red() != 255}'
    assert pixel_result.green() == 255, \
        f'Green component out of range [0-255] -> {pixel_result.green() != 255}'
    assert pixel_result.blue() == 255, \
        f'Blue component out of range [0-255] -> {pixel_result.blue() != 255}'


@pytest.mark.parametrize('pixel', [(0, 0, 0)])  # Limit values
@pytest.mark.parametrize('other_pixel', [(0, 0, 0)])
def test_operation_subtracting_limit_value_0(pixel, other_pixel):
    """
    1-> Adding/subtracting two pixels should result new Pixel object with components equal
    to difference of corresponding components.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__."""
    pixel_result = Pixel(*pixel) - Pixel(*other_pixel)
    assert pixel_result.red() == 0, \
        f'Red component not in range [0-255] -> {pixel_result.red() != 0}'
    assert pixel_result.green() == 0, \
        f'Green component not in range [0-255] -> {pixel_result.green() != 0}'
    assert pixel_result.blue() == 0, \
        f'Blue component not in range [0-255] -> {pixel_result.blue() != 0}'


@pytest.mark.parametrize('pixel', [(255, 255, 255)])  # Limit values
@pytest.mark.parametrize('other_pixel', [(10, 111, 181)])
def test_operation_subtracting_limit_value_255(pixel, other_pixel):
    """
    1-> Adding/subtracting two pixels should result new Pixel object with components equal
    to difference of corresponding components.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__."""
    pixel_result = Pixel(*pixel) - Pixel(*other_pixel)
    assert pixel_result.red() == 245, \
        f'Red component not in range [0-255] -> {pixel_result.red() != 245}'
    assert pixel_result.green() == 144, \
        f'Green component not in range [0-255] -> {pixel_result.green() != 245}'
    assert pixel_result.blue() == 74, \
        f'Blue component not in range [0-255] -> {pixel_result.blue() != 245}'


@pytest.mark.parametrize('pixel', [(0, 0, 0)])  # Equivalence partitioning
@pytest.mark.parametrize('other_pixel', [(111, 224, 218)])
def test_operation_subtracting_equivalence_partitioning(pixel, other_pixel):
    """
    1-> Adding/subtracting two pixels should result new Pixel object with components equal
    to difference of corresponding components.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__."""
    pixel_result = Pixel(*pixel) - Pixel(*other_pixel)
    assert pixel_result.red() == 0, \
        f'Red component out of range [0-255] -> {pixel_result.red() != 0}'
    assert pixel_result.green() == 0, \
        f'Green component out of range [0-255] -> {pixel_result.green() != 0}'
    assert pixel_result.blue() == 0, \
        f'Blue component out of range [0-255] -> {pixel_result.blue() != 0}'


###############################################################################################


@pytest.fixture(params=[(0, 0, 0), (5, 1, 187), (255, 255, 255)])
def test_pixel_object_for_testing_other_object(request):
    return Pixel(*request.param)


def test_operation_multiply_object_type_int(test_pixel_object_for_testing_other_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__.
    3-> New object should have all components multiplied/divided by number."""
    other = 2
    new_pixel = test_pixel_object_for_testing_other_object * other
    assert isinstance(other, int), f'{other} is not int'
    assert new_pixel.red() == test_pixel_object_for_testing_other_object.red(), \
        f'Red: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.red()} != {test_pixel_object_for_testing_other_object.red()}'
    assert new_pixel.green() == test_pixel_object_for_testing_other_object.green(), \
        f'Green: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.green()} != {test_pixel_object_for_testing_other_object.green()}'
    assert new_pixel.blue() == test_pixel_object_for_testing_other_object.blue(), \
        f'Blue: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.blue()} != {test_pixel_object_for_testing_other_object.blue()}'


def test_operation_rmultiply_object_type_int(test_pixel_object_for_testing_other_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__.
    3-> New object should have all components multiplied/divided by number."""
    other = 3
    new_pixel = other * test_pixel_object_for_testing_other_object
    assert isinstance(other, int), f'{other} is not int '
    assert new_pixel.red() == test_pixel_object_for_testing_other_object.red(), \
        f'Red: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.red()} != {test_pixel_object_for_testing_other_object.red()}'
    assert new_pixel.green() == test_pixel_object_for_testing_other_object.green(), \
        f'Green: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.green()} != {test_pixel_object_for_testing_other_object.green()}'
    assert new_pixel.blue() == test_pixel_object_for_testing_other_object.blue(), \
        f'Blue: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.blue()} != {test_pixel_object_for_testing_other_object.blue()}'


def test_operation_divide_object_type_int(test_pixel_object_for_testing_other_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> New object should have all components multiplied/divided by number."""
    other = 15
    new_pixel = test_pixel_object_for_testing_other_object / other
    assert isinstance(other, int), f'{other} is not int'
    assert new_pixel.red() == test_pixel_object_for_testing_other_object.red(), \
        f'Red: Failed to divide pixel components by number {other} -> ' \
        f'{new_pixel.red()} != {test_pixel_object_for_testing_other_object.red()}'
    assert new_pixel.green() == test_pixel_object_for_testing_other_object.green(), \
        f'Green: Failed to divide pixel components by number {other} -> ' \
        f'{new_pixel.green()} != {test_pixel_object_for_testing_other_object.green()}'
    assert new_pixel.blue() == test_pixel_object_for_testing_other_object.blue(), \
        f'Blue: Failed to divide pixel components by number {other} -> ' \
        f'{new_pixel.blue()} != {test_pixel_object_for_testing_other_object.blue()}'


def test_operation_multiply_object_type_float(test_pixel_object_for_testing_other_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__.
    3-> New object should have all components multiplied/divided by number."""
    other = 2.5
    new_pixel = test_pixel_object_for_testing_other_object * other
    assert isinstance(other, float), f'{other} is not float'
    assert new_pixel.red() == test_pixel_object_for_testing_other_object.red(), \
        f'Red: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.red()} != {test_pixel_object_for_testing_other_object.red()}'
    assert new_pixel.green() == test_pixel_object_for_testing_other_object.green(), \
        f'Green: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.green()} != {test_pixel_object_for_testing_other_object.green()}'
    assert new_pixel.blue() == test_pixel_object_for_testing_other_object.blue(), \
        f'Blue: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.blue()} != {test_pixel_object_for_testing_other_object.blue()}'


def test_operation_rmultiply_object_type_float(test_pixel_object_for_testing_other_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> Class Pixel should implement operator overloading for +, -, * (left and right),
    /, == and overload methods __str and __repr__.
    3-> New object should have all components multiplied/divided by number."""
    other = 10.5
    new_pixel = other * test_pixel_object_for_testing_other_object
    assert isinstance(other, float), f'{other} is not float '
    assert new_pixel.red() == test_pixel_object_for_testing_other_object.red(), \
        f'Red: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.red()} != {test_pixel_object_for_testing_other_object.red()}'
    assert new_pixel.green() == test_pixel_object_for_testing_other_object.green(), \
        f'Green: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.green()} != {test_pixel_object_for_testing_other_object.green()}'
    assert new_pixel.blue() == test_pixel_object_for_testing_other_object.blue(), \
        f'Blue: Failed to multiply pixel components by number {other} -> ' \
        f'{new_pixel.blue()} != {test_pixel_object_for_testing_other_object.blue()}'


def test_operation_divide_object_type_float(test_pixel_object_for_testing_other_object):
    """
    1-> Operator *(/) should allow multiply/divide Pixel object by integer or float
    number greater than zero.
    2-> New object should have all components multiplied/divided by number."""
    other = 7.8
    new_pixel = test_pixel_object_for_testing_other_object / other
    assert isinstance(other, float), f'{other} is not float'
    assert new_pixel.red() == test_pixel_object_for_testing_other_object.red(), \
        f'Red: Failed to divide pixel components by number {other} -> ' \
        f'{new_pixel.red()} != {test_pixel_object_for_testing_other_object.red()}'
    assert new_pixel.green() == test_pixel_object_for_testing_other_object.green(), \
        f'Green: Failed to divide pixel components by number {other} -> ' \
        f'{new_pixel.green()} != {test_pixel_object_for_testing_other_object.green()}'
    assert new_pixel.blue() == test_pixel_object_for_testing_other_object.blue(), \
        f'Blue: Failed to divide pixel components by number {other} -> ' \
        f'{new_pixel.blue()} != {test_pixel_object_for_testing_other_object.blue()}'


###############################################################################################


def test_operation_multiply_by_str(test_pixel_object_for_testing_other_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = 'b'
    with pytest.raises(TypeError) as exc:
        test_pixel_object_for_testing_other_object * other
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


def test_operation_multiply_by_list(test_pixel_object_for_testing_other_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = [1, 2, 3]
    with pytest.raises(TypeError) as exc:
        test_pixel_object_for_testing_other_object * other
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


def test_rmultiply_by_str(test_pixel_object_for_testing_other_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = '0'
    with pytest.raises(TypeError) as exc:
        other * test_pixel_object_for_testing_other_object
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


def test_rmultiply_by_list(test_pixel_object_for_testing_other_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = [5, 'h', 3]
    with pytest.raises(TypeError) as exc:
        other * test_pixel_object_for_testing_other_object
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


def test_divide_by_istr(test_pixel_object_for_testing_other_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = 'g'
    with pytest.raises(TypeError) as exc:
        test_pixel_object_for_testing_other_object / other
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


def test_divide_by_list(test_pixel_object_for_testing_other_object):
    """
    1-> When trying multiply/divide by not integer or float numbers, TypeError exception
    should be raised."""
    other = ['a', 2, (3, 5)]
    with pytest.raises(TypeError) as exc:
        test_pixel_object_for_testing_other_object / other
    assert str(exc.value) == f'Object "other" -> "{other}" is not type of int or float', 'Type is valid'
    assert isinstance(exc.value, TypeError), 'Type is valid'


###############################################################################################


@pytest.fixture(params=[(0, 0, 0), (255, 255, 255), (0, 1, 255), (1, 2, 3), (4, 255, 127), (119, 0, 255)])
def test_pixel_object_for_multiply_divide_by_zero(request):
    return Pixel(*request.param)


def test_operation_multiply_by_zero(test_pixel_object_for_multiply_divide_by_zero):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = 0
    with pytest.raises(ValueError) as exc:
        test_pixel_object_for_multiply_divide_by_zero * other
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


def test_operation_multiplied_by_value_less_than_zero(test_pixel_object_for_multiply_divide_by_zero):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = -1
    with pytest.raises(ValueError) as exc:
        test_pixel_object_for_multiply_divide_by_zero * other
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


def test_operation_rmultiply_by_zero(test_pixel_object_for_multiply_divide_by_zero):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = 0
    with pytest.raises(ValueError) as exc:
        other * test_pixel_object_for_multiply_divide_by_zero
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


def test_operation_rmultiply_by_value_less_than_zero(test_pixel_object_for_multiply_divide_by_zero):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = -2
    with pytest.raises(ValueError) as exc:
        other * test_pixel_object_for_multiply_divide_by_zero
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


def test_operation_divide_by_zero(test_pixel_object_for_multiply_divide_by_zero):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = 0
    with pytest.raises(ValueError) as exc:
        test_pixel_object_for_multiply_divide_by_zero / other
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


def test_operation_divide_by_value_less_than_zero(test_pixel_object_for_multiply_divide_by_zero):
    """
    1-> When trying multiply/divide by 0 or number less than zero, ValueError exception
    should be raised."""
    other = -5
    with pytest.raises(ValueError) as exc:
        test_pixel_object_for_multiply_divide_by_zero / other
    assert str(exc.value) == f'Value "other" -> "{other}" must be greater than 0', 'Value is valid'
    assert isinstance(exc.value, ValueError), 'Value is valid'


###############################################################################################


@pytest.fixture(params=[(0, 0, 0), (255, 255, 255), (1, 127, 255)])
def test_pixel_object_for_get_components_type_int(request):
    return Pixel(*request.param)


def test_operation_multiply_by_numeric_float(test_pixel_object_for_get_components_type_int):
    """
    1-> If resulting components are fractional, fractional part should be discarded"""
    other = 2.7
    new_pixel = test_pixel_object_for_get_components_type_int * other
    assert isinstance(new_pixel.red(), int), 'Red component is not int'
    assert isinstance(new_pixel.green(), int), 'Green component is not int'
    assert isinstance(new_pixel.blue(), int), 'Blue component is not int'


def test_operation_rmultiply_by_numeric_float(test_pixel_object_for_get_components_type_int):
    """
    1-> If resulting components are fractional, fractional part should be discarded"""
    other = 5.4
    new_pixel = other * test_pixel_object_for_get_components_type_int
    assert isinstance(new_pixel.red(), int), 'Red component is not int'
    assert isinstance(new_pixel.green(), int), 'Green component is not int'
    assert isinstance(new_pixel.blue(), int), 'Blue component is not int'


def test_operation_divide_by_numeric_float(test_pixel_object_for_get_components_type_int):
    """
    1-> If resulting components are fractional, fractional part should be discarded"""
    other = 1.1
    new_pixel = test_pixel_object_for_get_components_type_int / other
    assert isinstance(new_pixel.red(), int), 'Red component is not int'
    assert isinstance(new_pixel.green(), int), 'Green component is not int'
    assert isinstance(new_pixel.blue(), int), 'Blue component is not int'


###############################################################################################


@pytest.fixture(params=[(0, 0, 0), (255, 255, 255), (10, 20, 104)])
def test_pixel_object_for_get_components_eq_value_0(request):
    return Pixel(*request.param)


def test_operation_sub_eq_0(test_pixel_object_for_get_components_eq_value_0):
    """
    1-> If resulting component is less then zero, it should be set to 0."""
    other_pixel = Pixel(255, 255, 255)
    new_pixel = test_pixel_object_for_get_components_eq_value_0 - other_pixel
    assert new_pixel.red() == 0, 'Red component is not 0'
    assert new_pixel.green() == 0, 'Green component is not 0'
    assert new_pixel.blue() == 0, 'Blue component is not 0'


def test_operation_multiply_eq_0(test_pixel_object_for_get_components_eq_value_0):
    """
    1-> If resulting component is less then zero, it should be set to 0."""
    other = 0.0000000009
    new_pixel = test_pixel_object_for_get_components_eq_value_0 * other
    assert new_pixel.red() == 0, 'Red component is not 0'
    assert new_pixel.green() == 0, 'Green component is not 0'
    assert new_pixel.blue() == 0, 'Blue component is not 0'


def test_operation_rmultiply_eq_0(test_pixel_object_for_get_components_eq_value_0):
    """
    1-> If resulting component is less then zero, it should be set to 0."""
    other = 0.0000000009
    new_pixel = other * test_pixel_object_for_get_components_eq_value_0
    assert new_pixel.red() == 0, 'Red component is not 0'
    assert new_pixel.green() == 0, 'Green component is not 0'
    assert new_pixel.blue() == 0, 'Blue component is not 0'


def test_operation_divide_eq_0(test_pixel_object_for_get_components_eq_value_0):
    other = 255.0005
    new_pixel = test_pixel_object_for_get_components_eq_value_0 / other
    assert new_pixel.red() == 0, 'Red component is not 0'
    assert new_pixel.green() == 0, 'Green component is not 0'
    assert new_pixel.blue() == 0, 'Blue component is not 0'


###############################################################################################


@pytest.mark.parametrize('pixel', [(255, 255, 255), (0, 0, 0), (240, 112, 5)])
def test_operation_add_eq_255(pixel):
    """
    1-> If resulting component is greater then 255, it should be set to 255."""
    other_pixel = Pixel(255, 255, 255)
    new_pixel = Pixel(*pixel) + other_pixel
    assert new_pixel.red() == 255, 'Red component is not 255'
    assert new_pixel.green() == 255, 'Green component is not 255'
    assert new_pixel.blue() == 255, 'Blue component is not 255'


@pytest.fixture(params=[(255, 255, 255), (240, 112, 205)])
def test_pixel_object_for_get_components_eq_value_255(request):
    return Pixel(*request.param)


def test_operation_multiply_eq_255(test_pixel_object_for_get_components_eq_value_255):
    """
    1-> If resulting component is greater then 255, it should be set to 255."""
    other = 255
    new_pixel = test_pixel_object_for_get_components_eq_value_255 * other
    assert new_pixel.red() == 255, 'Red component is not 255'
    assert new_pixel.green() == 255, 'Green component is not 255'
    assert new_pixel.blue() == 255, 'Blue component is not 255'


def test_operation_rmultiply_eq_255(test_pixel_object_for_get_components_eq_value_255):
    """
    1-> If resulting component is greater then 255, it should be set to 255."""
    other = 255
    new_pixel = other * test_pixel_object_for_get_components_eq_value_255
    assert new_pixel.red() == 255, 'Red component is not 255'
    assert new_pixel.green() == 255, 'Green component is not 255'
    assert new_pixel.blue() == 255, 'Blue component is not 255'


def test_operation_divide_eq_255(test_pixel_object_for_get_components_eq_value_255):
    """
    1-> If resulting component is greater then 255, it should be set to 255."""
    other = 0.0000589631
    new_pixel = test_pixel_object_for_get_components_eq_value_255 / other
    assert new_pixel.red() == 255, 'Red component is not 255'
    assert new_pixel.green() == 255, 'Green component is not 255'
    assert new_pixel.blue() == 255, 'Blue component is not 255'


# ##############################################################################################


@pytest.mark.parametrize('pixel', [(255, 254, 253)])
def test_eq_two_pixel_true(pixel):
    """
    1-> Two objects with equal components considered to be equal."""
    other_pixel = Pixel(255, 254, 253)
    assert Pixel(*pixel) == other_pixel, 'Objects are not equal'


@pytest.mark.parametrize('pixel', [(248, 0, 12)])
def test_eq_two_pixel_false(pixel):
    """
    1-> Two objects with equal components considered to be equal."""
    other_pixel = Pixel(255, 255, 255)
    assert Pixel(*pixel) != other_pixel, 'Objects are equal'


# ##############################################################################################

@pytest.mark.parametrize('pixel', [(255, 0, 1)])
def test_checks_str_pixel_object(pixel):
    """
    1-> Method __str__ should return string like (\t - tabulation symbol"""
    assert re.match(r'^\tRed: \d+\n\tGreen: \d+\n\tBlue: \d+$', str(Pixel(*pixel))), 'String is not valid'


@pytest.mark.parametrize('pixel', [(154, 254, 100)])
def test_checks_repr_pixel_object(pixel):
    """
    1-> Method __repr__ should return string with constructor call."""
    assert re.match(r'^\d+, \d+, \d+$', repr(Pixel(*pixel))), 'String is not valid'
