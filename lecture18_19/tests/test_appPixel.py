import pytest
from lecture18_19.application.appPixel import Pixel
import re


@pytest.fixture(params=[(1, 255, 1)])
def pixel(request):
    return Pixel(*request.param)


def test_create_pixel(pixel):
    assert pixel.red() in range(256), 'Red component must be in the range [0 .. 255]'
    assert pixel.green() in range(256), 'Green component must be in the range [0 .. 255]'
    assert pixel.blue() in range(256), 'Blue component must be in the range [0 .. 255]'


def test_valid_component(pixel):
    assert isinstance(pixel.red(), int), 'Red component must be an integer'
    assert isinstance(pixel.green(), int), 'Green component must be an integer'
    assert isinstance(pixel.blue(), int), 'Blue component must be an integer'
    assert re.match(r'^\d+$', str(pixel.red())), 'Red component must be a digit'
    assert re.match(r'^\d+$', str(pixel.green())), 'Green component must be a digit'
    assert re.match(r'^\d+$', str(pixel.blue())), 'Blue component must be a digit'


def test_add_pixel(pixel):
    pixel2 = Pixel(255, 255, 255)
    pixel = pixel.__add__(pixel2)
    assert pixel.red() == 255, 'Sum red components must be <= 255 and => 0'
    assert pixel.green() == 255, 'Sum green components must be <= 255 and => 0'
    assert pixel.blue() == 255, 'Sum blue components must be <= 255 and => 0'


def test_add_pixel_if_value_other_is_not_type_pixel(pixel):
    other = 1
    assert pixel.__add__(other) == 'Object "other" -> "1" is not a Pixel object'
    assert not isinstance(other, Pixel), 'Object "other" must not be a Pixel object'


def test_sub_pixel(pixel):
    pixel2 = Pixel(1, 1, 1)
    pixel = pixel.__sub__(pixel2)
    assert pixel.red() == 0, 'Sum red components must be <= 255 and => 0'
    assert pixel.green() == 254, 'Sum green components must be <= 255 and => 0'
    assert pixel.blue() == 0, 'Sum blue components must be <= 255 and => 0'


def test_sub_pixel_if_value_other_is_not_type_pixel(pixel):
    other = 1
    assert pixel.__sub__(other) == 'Object "other" -> "1" is not a Pixel object'
    assert not isinstance(other, Pixel), 'Object "other" must not be a Pixel object'


def test_mul_pixel(pixel):
    pixel = pixel.__mul__(2)
    assert pixel.red() == 2, 'Multiplying red components must be <= 255 and => 0'
    assert pixel.green() == 255, 'Multiplying green components must be <= 255 and => 0'
    assert pixel.blue() == 2, 'Multiplying blue components must be <= 255 and => 0'


def test_mul_pixel_if_value_other_is_not_type_int_or_float(pixel):
    other = 'b'
    assert pixel.__mul__(other) == 'Object "other" -> "b" is not type of int or float'
    assert not isinstance(other, (int, float)), 'Object "other" must not be a type of int or float'


def test_mul_pixel_if_value_other_is_less_than_0(pixel):
    other = -1
    assert pixel.__mul__(other) == 'Value "other" -> "-1" must be greater than 0'
    assert other <= 0, 'Value "other" must be less than 0'


def test_rmul_pixel(pixel):
    pixel = pixel.__rmul__(2)
    assert pixel.red() == 2, 'Multiplying red components must be <= 255 and => 0'
    assert pixel.green() == 255, 'Multiplying green components must be <= 255 and => 0'
    assert pixel.blue() == 2, 'Multiplying blue components must be <= 255 and => 0'


def test_rmul_pixel_if_value_other_is_not_type_int_or_float(pixel):
    other = 'b'
    assert pixel.__rmul__(other) == 'Object "other" -> "b" is not type of int or float'
    assert not isinstance(other, (int, float)), 'Object "other" must not be a type of int or float'


def test_rmul_pixel_if_value_other_is_less_than_0(pixel):
    other = -1
    assert pixel.__rmul__(other) == 'Value "other" -> "-1" must be greater than 0'
    assert other <= 0, 'Value "other" must be less than 0'


def test_truediv_pixel(pixel):
    pixel = pixel.__truediv__(2)
    assert pixel.red() == 0, 'Dividing red components must be <= 255 and => 0'
    assert pixel.green() == 127, 'Dividing green components must be <= 255 and => 0'
    assert pixel.blue() == 0, 'Dividing blue components must be <= 255 and => 0'


def test_truediv_pixel_1034(pixel):
    pixel = pixel.__truediv__(1034)
    assert pixel.red() == 0, 'Dividing red components must be <= 255 and => 0'
    assert pixel.green() == 0, 'Dividing green components must be <= 255 and => 0'
    assert pixel.blue() == 0, 'Dividing blue components must be <= 255 and => 0'


def test_truediv_pixel_if_value_other_is_not_type_int_or_float(pixel):
    other = 'b'
    assert pixel.__truediv__(other) == 'Object "other" -> "b" is not type of int or float'
    assert not isinstance(other, (int, float)), 'Object "other" must not be a type of int or float'


def test_truediv_pixel_if_value_other_is_less_than_0(pixel):
    other = 0
    assert pixel.__truediv__(other) == 'Value "other" -> "0" must be greater than 0'
    assert other <= 0, 'Value "other" must be less than 0'


def test_rtruediv_pixel(pixel):
    pixel = pixel.__rtruediv__(2)
    assert pixel.red() == 2, 'Dividing red components must be <= 255 and => 0'
    assert pixel.green() == 0, 'Dividing green components must be <= 255 and => 0'
    assert pixel.blue() == 2, 'Dividing blue components must be <= 255 and => 0'


def test_rtruediv_pixel_1034(pixel):
    pixel = pixel.__rtruediv__(1034)
    assert pixel.red() == 255, 'Dividing red components must be <= 255 and => 0'
    assert pixel.green() == 4, 'Dividing green components must be <= 255 and => 0'
    assert pixel.blue() == 255, 'Dividing blue components must be <= 255 and => 0'


def test_rtruediv_pixel_if_value_other_is_not_type_int_or_float(pixel):
    other = 'b'
    assert pixel.__rtruediv__(other) == 'Object "other" -> "b" is not type of int or float'
    assert not isinstance(other, (int, float)), 'Object "other" must not be a type of int or float'


def test_rtruediv_pixel_if_value_other_is_less_than_0(pixel):
    other = 0
    assert pixel.__rtruediv__(other) == 'Value "other" -> "0" must be greater than 0'
    assert other <= 0, 'Value "other" must be less than 0'


def test_rtruediv_pixel_if_pixel_component_is_zero():
    pixel = Pixel(0, 1, 255)
    assert pixel.__rtruediv__(1034) == 'Some pixel component is zero'


def test_eq_pixel(pixel):
    true_pixel = Pixel(1, 255, 1)
    false_pixel = Pixel(6, 255, 125)
    assert pixel.__eq__(true_pixel) == True, 'The pixels must be equal'
    assert pixel.__eq__(false_pixel) == False, 'The pixels must not be equal'


def test_eq_pixel_if_value_other_is_not_type_pixel(pixel):
    other = 1
    assert pixel.__eq__(other) == 'Object "other" -> "1" is not a Pixel object'
    assert not isinstance(other, Pixel), 'Object "other" must not be a Pixel object'


