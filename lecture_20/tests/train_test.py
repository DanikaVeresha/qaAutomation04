import pytest
from lecture_20.application.app_Pixel import Pixel
import re

#   In the lines of the document, I wrote the requirements for the Pixel class,
#   which were given in the homework for the lecture -> 14.
#   This file has 60 tests.


@pytest.mark.parametrize('pixel1', [(Pixel(0, 0, 0))])
@pytest.mark.parametrize('pixel2', [(Pixel(255, 255, 255))])
@pytest.mark.parametrize('pixel3', [(Pixel(128, 127, 140))])
def test_P_pixel_len_all_the_components_is_valid(pixel1, pixel2, pixel3):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> Components of pixel are in the range [0 .. 255].
    -> Positive test cases:
    """
    assert len(pixel1.__dict__) == 3, 'Length of pixel1 is not 3'
    assert len(pixel2.__dict__) == 3, 'Length of pixel2 is not 3'
    assert len(pixel3.__dict__) == 3, 'Length of pixel3 is not 3'


@pytest.mark.parametrize('pixel1', [(Pixel(0, 0, 0))])
@pytest.mark.parametrize('pixel2', [(Pixel(255, 255, 255))])
@pytest.mark.parametrize('pixel3', [(Pixel(128, 127, 140))])
def test_P_pixel_components_all_the_components_is_valid(pixel1, pixel2, pixel3):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> Components of pixel are in the range [0 .. 255].
    -> Positive test cases:
    """
    assert pixel1.__dict__ == {'_Pixel__red': 0, '_Pixel__green': 0, '_Pixel__blue': 0}, \
        'Components isn`t red: 0, green: 0, blue: 0'
    assert pixel2.__dict__ == {'_Pixel__red': 255, '_Pixel__green': 255, '_Pixel__blue': 255}, \
        'Components isn`t red: 255, green: 255, blue: 255'
    assert pixel3.__dict__ == {'_Pixel__red': 128, '_Pixel__green': 127, '_Pixel__blue': 140}, \
        'Components isn`t red: 128, green: 127, blue: 140'


@pytest.mark.parametrize('pixel1', [(Pixel(0, 0, 0))])
@pytest.mark.parametrize('pixel2', [(Pixel(255, 255, 255))])
@pytest.mark.parametrize('pixel3', [(Pixel(1, 194, 211))])
def test_P_components_is_int_type(pixel1, pixel2, pixel3):
    """
    1-> 1-> Components of pixel are integer numbers.
    2-> Components of pixel are in the range [0 .. 255].
    -> Positive test cases:
    """
    assert all(isinstance(i, int) for i in pixel1.__dict__.values()), 'Components is not int type'
    assert all(isinstance(i, int) for i in pixel2.__dict__.values()), 'Components is not int type'
    assert all(isinstance(i, int) for i in pixel3.__dict__.values()), 'Components is not int type'


@pytest.mark.parametrize('pixel', [(0.125, 254.7, 127.5)])
def test_P_components_is_int_type_if_start_values_is_float(pixel):
    """
    1-> 1-> Components of pixel are integer numbers.
    2-> Components of pixel are in the range [0 .. 255].
    -> Positive test cases:
    """
    assert Pixel(*pixel).__dict__ == {'_Pixel__red': 0, '_Pixel__green': 254, '_Pixel__blue': 127}, \
        f'Components isn`t int type {Pixel(*pixel).__dict__}'


@pytest.mark.parametrize('pixel1', [(Pixel(0, 0, 0))])
@pytest.mark.parametrize('pixel2', [(Pixel(255, 255, 255))])
@pytest.mark.parametrize('pixel3', [(Pixel(2, 58, 140))])
def test_P_components_is_in_range(pixel1, pixel2, pixel3):
    """
    1-> Components of pixel are in the range [0 .. 255].
    -> Positive test cases:
    """
    assert all(0 <= i <= 255 for i in pixel1.__dict__.values()), 'Components is not in range [0 .. 255]'
    assert all(0 <= i <= 255 for i in pixel2.__dict__.values()), 'Components is not in range [0 .. 255]'
    assert all(0 <= i <= 255 for i in pixel3.__dict__.values()), 'Components is not in range [0 .. 255]'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 10, 40)])
def test_P_adding_two_valid_pixels(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is greater then 255, it should be set to 255.
    -> Positive test cases:
    """
    other_pixel = Pixel(1, 10, 100)
    new_pixel1 = pixel1 + other_pixel
    new_pixel2 = pixel2 + other_pixel
    new_pixel3 = pixel3 + other_pixel
    assert new_pixel1 == Pixel(1, 10, 100), \
        'Sum of pixel1 and other_pixel is not equal to Pixel(1, 10, 100)'
    assert new_pixel2 == Pixel(255, 255, 255), \
        'Sum of pixel2 and other_pixel is not equal to Pixel(255, 255, 255)'
    assert new_pixel3 == Pixel(2, 20, 140), \
        'Sum of pixel3 and other_pixel is not equal to Pixel(2, 20, 140)'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(2, 4, 118)])
def test_P_creating_new_object_after_adding_two_valid_pixels(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is greater then 255, it should be set to 255.
    -> Positive test cases:
    """
    other_pixel = Pixel(0, 5, 2)
    new_pixel1 = pixel1 + other_pixel
    new_pixel2 = pixel2 + other_pixel
    new_pixel3 = pixel3 + other_pixel
    assert isinstance(new_pixel1, Pixel), 'New object is not Pixel type'
    assert isinstance(new_pixel2, Pixel), 'New object is not Pixel type'
    assert isinstance(new_pixel3, Pixel), 'New object is not Pixel type'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(2, 4, 118)])
def test_P_radding_two_valid_pixels(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is greater then 255, it should be set to 255.
    -> Positive test cases:
    """
    other_pixel = Pixel(0, 1, 255)
    new_pixel1 = other_pixel + pixel1
    new_pixel2 = other_pixel + pixel2
    new_pixel3 = other_pixel + pixel3
    assert new_pixel1 == Pixel(0, 1, 255), \
        'Sum of pixel1 and other_pixel is not equal to Pixel(0, 1, 255)'
    assert new_pixel2 == Pixel(255, 255, 255), \
        'Sum of pixel2 and other_pixel is not equal to Pixel(255, 255, 255)'
    assert new_pixel3 == Pixel(2, 5, 255), \
        'Sum of pixel3 and other_pixel is not equal to Pixel(2, 5, 255)'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(127, 125, 0)])
def test_P_creating_new_object_after_radding_two_valid_pixels(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is greater then 255, it should be set to 255.
    -> Positive test cases:
    """
    other_pixel = Pixel(0, 127, 255)
    new_pixel1 = other_pixel + pixel1
    new_pixel2 = other_pixel + pixel2
    new_pixel3 = other_pixel + pixel3
    assert isinstance(new_pixel1, Pixel), 'New object is not Pixel type'
    assert isinstance(new_pixel2, Pixel), 'New object is not Pixel type'
    assert isinstance(new_pixel3, Pixel), 'New object is not Pixel type'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(127, 125, 0)])
def test_P_subtracting_two_valid_pixels(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is less then zero, it should be set to 0.
    -> Positive test cases:
    """
    other_pixel = Pixel(0, 127, 255)
    new_pixel1 = pixel1 - other_pixel
    new_pixel2 = pixel2 - other_pixel
    new_pixel3 = pixel3 - other_pixel
    assert new_pixel1 == Pixel(0, 0, 0), \
        'Subtract of pixel1 and other_pixel is not equal to Pixel(0, 0, 0)'
    assert new_pixel2 == Pixel(255, 128, 0), \
        'Subtract of pixel2 and other_pixel is not equal to Pixel(255, 128, 0)'
    assert new_pixel3 == Pixel(127, 0, 0), \
        'Subtract of pixel3 and other_pixel is not equal to Pixel(127, 0, 0)'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 1, 1)])
def test_P_creating_new_object_after_subtracting_two_valid_pixels(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is greater then 255, it should be set to 255.
    -> Positive test cases:
    """
    other_pixel = Pixel(0, 127, 255)
    new_pixel1 = other_pixel + pixel1
    new_pixel2 = other_pixel + pixel2
    new_pixel3 = other_pixel + pixel3
    assert isinstance(new_pixel1, Pixel), 'New object is not Pixel type'
    assert isinstance(new_pixel2, Pixel), 'New object is not Pixel type'
    assert isinstance(new_pixel3, Pixel), 'New object is not Pixel type'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 2, 3)])
def test_P_rsubtracting_two_valid_pixel(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is less then zero, it should be set to 0.
    -> Positive test cases:
    """
    other_pixel = Pixel(0, 127, 255)
    new_pixel1 = other_pixel - pixel1
    new_pixel2 = other_pixel - pixel2
    new_pixel3 = other_pixel - pixel3
    assert new_pixel1 == Pixel(0, 127, 255), \
        'Subtract of pixel1 and other_pixel is not equal to Pixel(0, 127, 255)'
    assert new_pixel2 == Pixel(0, 0, 0), \
        'Subtract of pixel2 and other_pixel is not equal to Pixel(0, 0, 0)'
    assert new_pixel3 == Pixel(0, 125, 252), \
        'Subtract of pixel3 and other_pixel is not equal to Pixel(0, 125, 252)'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(100, 200, 30)])
def test_P_creating_new_object_after_rsubtracting_two_valid_pixel(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is less then zero, it should be set to 0.
    -> Positive test cases:
    """
    other_pixel = Pixel(0, 5, 255)
    new_pixel1 = other_pixel - pixel1
    new_pixel2 = other_pixel - pixel2
    new_pixel3 = other_pixel - pixel3
    assert isinstance(new_pixel1, Pixel), 'New object is not Pixel type'
    assert isinstance(new_pixel2, Pixel), 'New object is not Pixel type'
    assert isinstance(new_pixel3, Pixel), 'New object is not Pixel type'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 127, 255)])
def test_P_multiply_pixel_by_valid_value_type_int(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    -> Positive test cases:
    """
    new_pixel1 = pixel1 * 2
    new_pixel2 = pixel2 * 2
    new_pixel3 = pixel3 * 2
    assert new_pixel1 == Pixel(0, 0, 0), \
        'Multiply of pixel1 and 2 is not equal to Pixel(0, 0, 0)'
    assert new_pixel2 == Pixel(255, 255, 255), \
        'Multiply of pixel2 and 2 is not equal to Pixel(255, 255, 255)'
    assert new_pixel3 == Pixel(2, 254, 255), \
        'Multiply of pixel3 and 2 is not equal to Pixel(2, 254, 255)'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 249, 25)])
def test_P_multiply_pixel_by_valid_value_type_float(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    -> Positive test cases:
    """
    new_pixel1 = pixel1 * 2.5
    new_pixel2 = pixel2 * 2.5
    new_pixel3 = pixel3 * 2.5
    assert new_pixel1 == Pixel(0, 0, 0), \
        'Multiply of pixel1 and 2.5 is not equal to Pixel(0, 0, 0)'
    assert new_pixel2 == Pixel(255, 255, 255), \
        'Multiply of pixel2 and 2.5 is not equal to Pixel(255, 255, 255)'
    assert new_pixel3 == Pixel(2, 255, 62), \
        'Multiply of pixel3 and 2.5 is not equal to Pixel(2, 255, 62)'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 127, 149)])
def test_P_divide_pixel_by_valid_value_type_int(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    -> Positive test cases:
    """
    new_pixel1 = pixel1 / 2
    new_pixel2 = pixel2 / 2
    new_pixel3 = pixel3 / 2
    assert new_pixel1 == Pixel(0, 0, 0), \
        'Divide of pixel1 and 2 is not equal to Pixel(0, 0, 0)'
    assert new_pixel2 == Pixel(127, 127, 127), \
        'Divide of pixel2 and 2 is not equal to Pixel(127, 127, 127)'
    assert new_pixel3 == Pixel(0, 63, 74), \
        'Divide of pixel3 and 2 is not equal to Pixel(0, 63, 74)'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 55, 250)])
def test_P_divide_pixel_by_valid_value_type_float(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    5-> If resulting component is less then zero, it should be set to 0.
    -> Positive test cases:
    """
    new_pixel1 = pixel1 / 0.0009
    new_pixel2 = pixel2 / 255.0005
    new_pixel3 = pixel3 / 0.0009
    assert new_pixel1 == Pixel(0, 0, 0), \
        'Divide of pixel1 and 0.0009 is not equal to Pixel(0, 0, 0)'
    assert new_pixel2 == Pixel(0, 0, 0), \
        'Divide of pixel2 and 0.0009 is not equal to Pixel(255, 255, 255)'
    assert new_pixel3 == Pixel(255, 255, 255), \
        'Divide of pixel3 and 0.0009 is not equal to Pixel(255, 255, 255)'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 55, 129)])
def test_P_eq_two_valid_pixel(pixel1, pixel2, pixel3):
    """
    1-> Two objects with equal components considered to be equal.
    """
    assert pixel1 == Pixel(0, 0, 0), 'Pixel1 is not equal to Pixel(0, 0, 0)'
    assert pixel2 == Pixel(255, 255, 255), 'Pixel2 is not equal to Pixel(255, 255, 255)'
    assert pixel3 == Pixel(1, 55, 129), 'Pixel3 is not equal to Pixel(1, 55, 129)'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 55, 129)])
def test_P_str_valid_pixel(pixel1, pixel2, pixel3):
    """
    1-> Method __str__ should return string like (\t - tabulation symbol
    """
    assert re.match(r'\tRed: \d+\n\tGreen: \d+\n\tBlue: \d+', str(pixel1)), \
        'String representation of pixel1 is not correct'
    assert re.match(r'\tRed: \d+\n\tGreen: \d+\n\tBlue: \d+', str(pixel2)), \
        'String representation of pixel2 is not correct'
    assert re.match(r'\tRed: \d+\n\tGreen: \d+\n\tBlue: \d+', str(pixel3)), \
        'String representation of pixel3 is not correct'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 55, 129)])
def test_P_repr_valid_pixel(pixel1, pixel2, pixel3):
    """
    1-> Method __repr__ should return string like Pixel(0, 0, 0)
    """
    assert re.match(r'^\d+, \d+, \d+$', repr(pixel1)), \
        'String representation of pixel1 is not correct'
    assert re.match(r'^\d+, \d+, \d+$', repr(pixel2)), \
        'String representation of pixel2 is not correct'
    assert re.match(r'^\d+, \d+, \d+$', repr(pixel3)), \
        'String representation of pixel3 is not correct'


##############################################################################################


@pytest.mark.parametrize('pixel1', [(0, 255)])
@pytest.mark.parametrize('pixel2', [(255, 255, 255, 255)])
def test_N_pixel_len_when_pixel_components_is_not_three(pixel1, pixel2):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    -> Negative test cases:
    """
    with pytest.raises(TypeError):
        assert len(Pixel(*pixel1).__dict__) == 2, 'Length of pixel1 must be 3'
        assert len(Pixel(*pixel2).__dict__) == 4, 'Length of pixel2 must be 3'




@pytest.mark.parametrize('pixel', [(-1, 310, 257)])
def test_N_pixel_len_all_the_components_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert len(Pixel(*pixel).__dict__) == 3, 'Length of pixel1 is not 3'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel', [(-8, 0, 255), (259, 1, 251)])
def test_N_pixel_len_if_only_red_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert len(Pixel(*pixel).__dict__) == 3, 'Length of pixel is not 3'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel', [(1, -5, 255), (254, 311, 251)])
def test_N_pixel_len_if_only_green_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert len(Pixel(*pixel).__dict__) == 3, 'Length of pixel is not 3'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel', [(1, 56, -255), (254, 190, 444)])
def test_N_pixel_len_if_only_blue_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert len(Pixel(*pixel).__dict__) == 3, 'Length of pixel is not 3'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel', [(0, -8, 258), (255, 300, -1)])
def test_N_pixel_len_if_green_and_blue_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert len(Pixel(*pixel).__dict__) == 3, 'Length of pixel is not 3'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel', [(260, -12, 0), (-11, 271, 24)])
def test_N_pixel_len_if_red_and_green_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert len(Pixel(*pixel).__dict__) == 3, 'Length of pixel is not 3'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel', [(260, 255, -1), (-1, 255, 444)])
def test_N_pixel_len_if_red_and_blue_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert len(Pixel(*pixel).__dict__) == 3, 'Length of pixel is not 3'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel', [(258, -19, 1024)])
def test_N_pixel_components_all_the_components_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert Pixel(*pixel).__dict__ == {'_Pixel__red': 258, '_Pixel__green': -19, '_Pixel__blue': 1024}, \
            'Components isn`t red: 258, green: -19, blue: 1024'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel1', [(258, 0, 250)])
@pytest.mark.parametrize('pixel2', [(-1, 255, 251)])
def test_N_pixel_components_if_red_is_invalid(pixel1, pixel2):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert Pixel(*pixel1).__dict__ == {'_Pixel__red': 258, '_Pixel__green': 0, '_Pixel__blue': 250}, \
            'Components isn`t red: 258, green: 0, blue: 250'
        assert Pixel(*pixel2).__dict__ == {'_Pixel__red': -1, '_Pixel__green': 255, '_Pixel__blue': 251}, \
            'Components isn`t red: -1, green: 255, blue: 251'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel1', [(119, -214, 250)])
@pytest.mark.parametrize('pixel2', [(120, 279, 251)])
def test_N_pixel_components_if_green_is_invalid(pixel1, pixel2):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert Pixel(*pixel1).__dict__ == {'_Pixel__red': 119, '_Pixel__green': -214, '_Pixel__blue': 250}, \
            'Components isn`t red: 119, green: -214, blue: 250'
        assert Pixel(*pixel2).__dict__ == {'_Pixel__red': 120, '_Pixel__green': 279, '_Pixel__blue': 251}, \
            'Components isn`t red: 120, green: 279, blue: 251'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel1', [(119, 214, -250)])
@pytest.mark.parametrize('pixel2', [(120, 23, 800)])
def test_N_pixel_components_if_blue_is_invalid(pixel1, pixel2):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert Pixel(*pixel1).__dict__ == {'_Pixel__red': 119, '_Pixel__green': 214, '_Pixel__blue': -250}, \
            'Components isn`t red: 119, green: 214, blue: -250'
        assert Pixel(*pixel2).__dict__ == {'_Pixel__red': 120, '_Pixel__green': 23, '_Pixel__blue': 800}, \
            'Components isn`t red: 120, green: 23, blue: 800'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel', [(0, -214, 756)])
def test_N_pixel_components_if_green_and_blue_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert Pixel(*pixel).__dict__ == {'_Pixel__red': 0, '_Pixel__green': -214, '_Pixel__blue': 756}, \
            'Components isn`t red: 0, green: -214, blue: 756'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel', [(-1, 256, 1)])
def test_N_pixel_components_if_red_and_green_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert Pixel(*pixel).__dict__ == {'_Pixel__red': -1, '_Pixel__green': 256, '_Pixel__blue': 1}, \
            'Components isn`t red: -1, green: 256, blue: 1'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel', [(-200, 5, 257)])
def test_N_pixel_components_if_red_and_blue_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
    3-> Components of pixel are in the range [0 .. 255].
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert Pixel(*pixel).__dict__ == {'_Pixel__red': -200, '_Pixel__green': 5, '_Pixel__blue': 257}, \
            'Components isn`t red: -200, green: 5, blue: 257'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(127, 10, 118)])
def test_N_adding_valid_pixel_with_object_which_is_not_pixel(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is greater then 255, it should be set to 255.
    -> Negative test cases:
    """
    with pytest.raises(TypeError) as ex:
        assert pixel1 + [1, 1, 1] == Pixel(1, 1, 1), \
            'Sum of pixel1 and 1 is not equal to Pixel(1, 1, 1)'
        assert pixel2 + [1, 1, 1] == Pixel(255, 255, 255), \
            'Sum of pixel2 and 1 is not equal to Pixel(255, 255, 255)'
        assert pixel3 + [1, 1, 1] == Pixel(128, 11, 119), \
            'Sum of pixel3 and 1 is not equal to Pixel(128, 11, 119)'
    assert str(ex.value) == 'Object "other" -> "[1, 1, 1]" is not a Pixel object', \
        'Object [1, 1, 1] is type Pixel'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(128, 0, 1)])
def test_N_radding_valid_pixel_with_object_which_is_not_pixel(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is greater then 255, it should be set to 255.
    -> Negative test cases:
    """
    with pytest.raises(TypeError) as ex:
        assert 'b' + pixel1 == Pixel(0, 0, 0), \
            'Sum of pixel1 and 1 is not equal to Pixel(0, 0, 0)'
        assert 'b' + pixel2 == Pixel('255b', '255b', '255b'), \
            'Sum of pixel2 and 1 is not equal to Pixel(255b, 255b, 255b)'
        assert 'b' + pixel3 == Pixel('128b', '0b', '1b'), \
            'Sum of pixel3 and 1 is not equal to Pixel(128b, 0b, 1b)'
    assert str(ex.value) == 'Object "other" -> "b" is not a Pixel object', \
        'Object "b" is type Pixel'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(100, 50, 200)])
def test_N_adding_valid_pixel_with_object_where_any_one_component_is_not_valid(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is greater then 255, it should be set to 255.
    -> Negative test cases:
    """
    other_pixel = (0, 0, -10)
    with pytest.raises(ValueError) as ex:
        assert other_pixel == Pixel(0, 0, -10), \
            'Sum of pixel1 and other_pixel is not equal to Pixel(0, 0, -10)'
        assert pixel1 + Pixel(*other_pixel) == Pixel(0, 0, -10), \
            'Sum of pixel1 and other_pixel is not equal to Pixel(0, 0, -10)'
        assert pixel2 + Pixel(*other_pixel) == Pixel(255, 255, 245), \
            'Sum of pixel2 and other_pixel is not equal to Pixel(255, 255, 245)'
        assert pixel3 + Pixel(*other_pixel) == Pixel(100, 50, 190), \
            'Sum of pixel3 and other_pixel is not equal to Pixel(100, 50, 190)'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(99, 199, 254)])
def test_N_radding_valid_pixel_with_object_where_any_two_component_is_not_valid(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is greater then 255, it should be set to 255.
    -> Negative test cases:
    """
    other_pixel = (0, 257, -1)
    with pytest.raises(ValueError) as ex:
        assert other_pixel == Pixel(0, 257, -1), \
            'Sum of pixel1 and other_pixel is not equal to Pixel(0, 257, -1)'
        assert Pixel(*other_pixel) + pixel1 == Pixel(0, 255, 0), \
            'Sum of pixel1 and other_pixel is not equal to Pixel(0, 255, 0)'
        assert Pixel(*other_pixel) + pixel2 == Pixel(255, 255, 254), \
            'Sum of pixel2 and other_pixel is not equal to Pixel(255, 255, 254)'
        assert Pixel(*other_pixel) + pixel3 == Pixel(99, 255, 253), \
            'Sum of pixel3 and other_pixel is not equal to Pixel(99, 255, 253)'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(125, 2, 95)])
def test_N_subtracting_valid_pixel_with_object_which_is_not_pixel(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is less then zero, it should be set to 0.
    -> Negative test cases:
    """
    with pytest.raises(TypeError) as ex:
        assert pixel1 - [1, 1, 1] == Pixel(0, 0, 0), \
            'Subtract of pixel1 and 1 is not equal to Pixel(0, 0, 0)'
        assert pixel2 - [1, 1, 1] == Pixel(254, 254, 254), \
            'Subtract of pixel2 and 1 is not equal to Pixel(254, 254, 254)'
        assert pixel3 - [1, 1, 1] == Pixel(124, 1, 94), \
            'Subtract of pixel3 and 1 is not equal to Pixel(124, 1, 94)'
    assert str(ex.value) == 'Object "other" -> "[1, 1, 1]" is not a Pixel object', \
        'Object [1, 1, 1] is type Pixel'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(8, 7, 80)])
def test_N_rsubtracting_valid_pixel_with_object_which_is_not_pixel(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is less then zero, it should be set to 0.
    -> Negative test cases:
    """
    with pytest.raises(TypeError) as ex:
        assert 'g' - pixel1 == Pixel(0, 0, 0), \
            'Subtract of pixel1 and 1 is not equal to Pixel(0, 0, 0)'
        assert 'g' - pixel2 == Pixel('255g', '255g', '255g'), \
            'Subtract of pixel2 and 1 is not equal to Pixel(255g, 255g, 255g)'
        assert 'g' - pixel3 == Pixel('8g', '7g', '80g'), \
            'Subtract of pixel3 and 1 is not equal to Pixel(8g, 7g, 80g)'
    assert str(ex.value) == 'Object "other" -> "g" is not a Pixel object', \
        'Object "g" is type Pixel'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 12, 222)])
def test_N_subtracting_valid_pixel_with_object_where_any_one_component_is_not_valid(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is less then zero, it should be set to 0.
    -> Negative test cases:
    """
    other_pixel = (-4, 0, 0)
    with pytest.raises(ValueError) as ex:
        assert other_pixel == Pixel(-4, 0, 0), \
            'Subtract of pixel1 and other_pixel is not equal to Pixel(-4, 0, 0)'
        assert pixel1 - Pixel(*other_pixel) == Pixel(4, 0, 0), \
            'Subtract of pixel1 and other_pixel is not equal to Pixel(4, 0, 0)'
        assert pixel2 - Pixel(*other_pixel) == Pixel(255, 255, 255), \
            'Subtract of pixel2 and other_pixel is not equal to Pixel(255, 255, 255)'
        assert pixel3 - Pixel(*other_pixel) == Pixel(5, 12, 222), \
            'Subtract of pixel3 and other_pixel is not equal to Pixel(5, 12, 222)'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(9, 101, 249)])
def test_N_rsubtracting_valid_pixel_with_object_where_any_two_component_is_not_valid(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Adding/subtracting two pixels should result new Pixel object with components equal
    to sum/difference of corresponding components.
    3-> If resulting component is less then zero, it should be set to 0.
    -> Negative test cases:
    """
    other_pixel = (278, -1, 0)
    with pytest.raises(ValueError) as ex:
        assert other_pixel == Pixel(278, -1, 0), \
            'Subtract of pixel1 and other_pixel is not equal to Pixel(278, -1, 0)'
        assert Pixel(*other_pixel) - pixel1 == Pixel(278, 0, 0), \
            'Subtract of pixel1 and other_pixel is not equal to Pixel(278, -1, 0)'
        assert Pixel(*other_pixel) - pixel2 == Pixel(23, 0, 0), \
            'Subtract of pixel2 and other_pixel is not equal to Pixel(23, 0, 0)'
        assert Pixel(*other_pixel) - pixel3 == Pixel(255, 0, 0), \
            'Subtract of pixel3 and other_pixel is not equal to Pixel(255, 0, 0)'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(10, 20, 30)])
def test_N_multiply_pixel_by_invalid_type_value_(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    -> Negative test cases:
    """
    with pytest.raises(TypeError) as ex:
        assert pixel1 * '2' == Pixel(0, 0, 0), \
            'Multiply of pixel1 and 2 is not equal to Pixel(0, 0, 0)'
        assert pixel2 * '2' == Pixel(255, 255, 255), \
            'Multiply of pixel2 and 2 is not equal to Pixel(255, 255, 255)'
        assert pixel3 * '2' == Pixel(20, 40, 60), \
            'Multiply of pixel3 and 2 is not equal to Pixel(20, 40, 60)'
    assert str(ex.value) == 'Object "other" -> "2" is not type of int or float', \
        'Object "2" is type int'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(17, 56, 241)])
def test_N_multiply_pixel_by_zero(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert pixel1 * 0 == Pixel(0, 0, 0), \
            'Multiply of pixel1 and 0 is not equal to Pixel(0, 0, 0)'
        assert pixel2 * 0 == Pixel(0, 0, 0), \
            'Multiply of pixel2 and 0 is not equal to Pixel(0, 0, 0)'
        assert pixel3 * 0 == Pixel(0, 0, 0), \
            'Multiply of pixel3 and 0 is not equal to Pixel(0, 0, 0)'
    assert str(ex.value) == 'Value "other" -> "0" must be greater than 0', \
        'Object 0 is not zero'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(11, 22, 33)])
def test_N_multiply_pixel_by_less_than_zero(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert pixel1 * -1 == Pixel(0, 0, 0), \
            'Multiply of pixel1 and -1 is not equal to Pixel(0, 0, 0)'
        assert pixel2 * -1 == Pixel(0, 0, 0), \
            'Multiply of pixel2 and -1 is not equal to Pixel(0, 0, 0)'
        assert pixel3 * -1 == Pixel(0, 0, 0), \
            'Multiply of pixel3 and -1 is not equal to Pixel(0, 0, 0)'
    assert str(ex.value) == 'Value "other" -> "-1" must be greater than 0', \
        'Object -1 is not negative number'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(10, 20, 30)])
def test_N_rmultiply_pixel_by_invalid_type_value_(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    -> Negative test cases:
    """
    with pytest.raises(TypeError) as ex:
        assert 'h' * pixel1 == Pixel(0, 0, 0), \
            'Multiply of pixel1 and h is not equal to Pixel(0, 0, 0)'
        assert 'h' * pixel2 == Pixel('255h', '255h', '255h'), \
            'Multiply of pixel2 and h is not equal to Pixel(255h, 255h, 255h)'
        assert 'h' * pixel3 == Pixel('10h', '20h', '30h'), \
            'Multiply of pixel3 and h is not equal to Pixel(10h, 20h, 30h)'
    assert str(ex.value) == 'Object "other" -> "h" is not type of int or float', \
        'Object "h" is type int'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(200, 190, 155)])
def test_N_rmultiply_pixel_by_zero(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert 0 * pixel1 == Pixel(0, 0, 0), \
            'Multiply of pixel1 and 0 is not equal to Pixel(0, 0, 0)'
        assert 0 * pixel2 == Pixel(0, 0, 0), \
            'Multiply of pixel2 and 0 is not equal to Pixel(0, 0, 0)'
        assert 0 * pixel3 == Pixel(0, 0, 0), \
            'Multiply of pixel3 and 0 is not equal to Pixel(0, 0, 0)'
    assert str(ex.value) == 'Value "other" -> "0" must be greater than 0', \
        'Object 0 is not zero'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(199, 1, 58)])
def test_N_rmultiply_pixel_by_less_than_zero(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert -1 * pixel1 == Pixel(0, 0, 0), \
            'Multiply of pixel1 and -1 is not equal to Pixel(0, 0, 0)'
        assert -1 * pixel2 == Pixel(0, 0, 0), \
            'Multiply of pixel2 and -1 is not equal to Pixel(0, 0, 0)'
        assert -1 * pixel3 == Pixel(0, 0, 0), \
            'Multiply of pixel3 and -1 is not equal to Pixel(0, 0, 0)'
    assert str(ex.value) == 'Value "other" -> "-1" must be greater than 0', \
        'Object -1 is not negative number'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(8, 14, 250)])
def test_N_divide_pixel_by_invalid_type_value_(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    -> Negative test cases:
    """
    with pytest.raises(TypeError) as ex:
        assert pixel1 / '2' == Pixel(0, 0, 0), \
            'Divide of pixel1 and 2 is not equal to Pixel(0, 0, 0)'
        assert pixel2 / '2' == Pixel(255, 255, 255), \
            'Divide of pixel2 and 2 is not equal to Pixel(255, 255, 255)'
        assert pixel3 / '2' == Pixel(4, 7, 125), \
            'Divide of pixel3 and 2 is not equal to Pixel(4, 7, 125)'
    assert str(ex.value) == 'Object "other" -> "2" is not type of int or float', \
        'Object "2" is type int'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(2, 254, 130)])
def test_N_divide_pixel_by_zero(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert pixel1 / 0 == Pixel(0, 0, 0), \
            'Divide of pixel1 and 0 is not equal to Pixel(0, 0, 0)'
        assert pixel2 / 0 == Pixel(0, 0, 0), \
            'Divide of pixel2 and 0 is not equal to Pixel(0, 0, 0)'
        assert pixel3 / 0 == Pixel(0, 0, 0), \
            'Divide of pixel3 and 0 is not equal to Pixel(0, 0, 0)'
    assert str(ex.value) == 'Value "other" -> "0" must be greater than 0', \
        'Object 0 is not zero'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(1, 2, 3)])
def test_N_divide_pixel_by_less_than_zero(pixel1, pixel2, pixel3):
    """
    1-> Class Pixel should implement operator overloading for +, -, * (left and right), /,
    == and overload methods __str and __repr__.
    2-> Operator *(/) should allow multiply/divide Pixel object by integer or float number
    greater than zero.
    3-> If resulting component is greater then 255, it should be set to 255.
    4-> If resulting components are fractional, fractional part should be discarded
    5-> If resulting component is less then zero, it should be set to 0.
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert pixel1 / -1 == Pixel(0, 0, 0), \
            'Divide of pixel1 and -1 is not equal to Pixel(0, 0, 0)'
        assert pixel2 / -1 == Pixel(0, 0, 0), \
            'Divide of pixel2 and -1 is not equal to Pixel(0, 0, 0)'
        assert pixel3 / -1 == Pixel(0, 0, 0), \
            'Divide of pixel3 and -1 is not equal to Pixel(0, 0, 0)'
    assert str(ex.value) == 'Value "other" -> "-1" must be greater than 0', \
        'Object -1 is not negative number'


@pytest.mark.parametrize('pixel1', [Pixel(0, 0, 0)])
@pytest.mark.parametrize('pixel2', [Pixel(255, 255, 255)])
@pytest.mark.parametrize('pixel3', [Pixel(34, 167, 199)])
def test_N_eq_two_valid_pixels_is_not_equal(pixel1, pixel2, pixel3):
    """
    1-> Two objects with equal components considered to be equal.
    """
    assert pixel1 != Pixel(1, 1, 1), \
        'Pixel1 is not equal to Pixel(1, 1, 1)'
    assert pixel2 != Pixel(255, 255, 254), \
        'Pixel2 is not equal to Pixel(255, 255, 254)'
    assert pixel3 != Pixel(34, 160, 0), \
        'Pixel3 is not equal to Pixel(34, 160, 0)'


@pytest.mark.parametrize('pixel', [Pixel(0, 0, 0)])
def test_N_eq_pixel_with_object_wich_is_not_type_pixel(pixel):
    """
    1-> Two objects with equal components considered to be equal.
    """
    with pytest.raises(TypeError) as ex:
        assert pixel == [0, 0, 0], \
            'Pixel1 is not equal to [0, 0, 0]'
    assert str(ex.value) == 'Object "other" -> "[0, 0, 0]" is not a Pixel object', \
        'Object [1, 1, 1] is type Pixel'

