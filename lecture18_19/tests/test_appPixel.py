import pytest
from lecture18_19.application.appPixel import Pixel
import re


@pytest.mark.parametrize('x', ['0'])
@pytest.mark.parametrize('y', ['0'])
@pytest.mark.parametrize('z', ['255'])
def test_check_pixel_x(x, y, z):
    pixel = Pixel(x, y, z)
    assert re.match(r'[0-9]', pixel.x), f'X {pixel.x} is not valid'
    assert 0 <= int(pixel.x) <= 255, f'X {pixel.x} is not valid'


@pytest.mark.parametrize('x', ['0'])
@pytest.mark.parametrize('y', ['0'])
@pytest.mark.parametrize('z', ['255'])
def test_check_pixel_y(x, y, z):
    pixel = Pixel(x, y, z)
    assert re.match(r'[0-9]', pixel.y), f'Y {pixel.y} is not valid'
    assert 0 <= int(pixel.y) <= 255, f'Y {pixel.y} is not valid'


@pytest.mark.parametrize('x', ['0'])
@pytest.mark.parametrize('y', ['0'])
@pytest.mark.parametrize('z', ['255'])
def test_check_pixel_z(x, y, z):
    pixel = Pixel(x, y, z)
    assert re.match(r'[0-9]', pixel.z), f'Z {pixel.z} is not valid'
    assert 0 <= int(pixel.z) <= 255, f'Z {pixel.z} is not valid'


@pytest.mark.parametrize('x', ['0'])
@pytest.mark.parametrize('y', ['0'])
@pytest.mark.parametrize('z', ['255'])
def test_get_color(x, y, z):
    pixel = Pixel(x, y, z)
    assert pixel.get_color() == 'blue', 'Color is not valid'
    assert pixel.pixels == ['blue -> 0, 0, 255'], 'Pixel is not valid'


@pytest.fixture(params=[('0', '0', '255'), ('255', '255', '0'), ('0', '255', '0'),
                        ('0', '0', '0'), ('255', '255', '255')])
def pixel(request):
    return Pixel(*request.param)


def test_create_pixel_x_fixture(pixel):
    assert re.match(r'[0-9]', pixel.x), f'X {pixel.x} is not valid'
    assert 0 <= int(pixel.x) <= 255, f'X {pixel.x} is not valid'


def test_create_pixel_y_fixture(pixel):
    assert re.match(r'[0-9]', pixel.y), f'Y {pixel.y} is not valid'
    assert 0 <= int(pixel.y) <= 255, f'Y {pixel.y} is not valid'


def test_create_pixel_z_fixture(pixel):
    assert re.match(r'[0-9]', pixel.z), f'Z {pixel.z} is not valid'
    assert 0 <= int(pixel.z) <= 255, f'Z {pixel.z} is not valid'


def test_get_color_fixture(pixel):
    for item in pixel.list_pixels():
        if item == f'{pixel.x}, {pixel.y}, {pixel.z}':
            assert pixel.get_color() == pixel.list_pixels()[item], 'Color is not valid'
            assert pixel.pixels == [f'{pixel.list_pixels()[item]} -> {item}'], 'Pixel is not valid'


@pytest.fixture(params=[('255', '255', '256')])
def invalid_pixel(request):
    return Pixel(*request.param)


def test_create_invalid_pixel_fixture(invalid_pixel):
    assert re.match(r'[0-9]', invalid_pixel.x), f'X {invalid_pixel.x} is not valid'
    assert 0 <= int(invalid_pixel.x) <= 255, f'X {invalid_pixel.x} is valid'


def test_create_invalid_pixel_y_fixture(invalid_pixel):
    assert re.match(r'[0-9]', invalid_pixel.y), f'Y {invalid_pixel.y} is not valid'
    assert 0 <= int(invalid_pixel.y) <= 255, f'Y {invalid_pixel.y} is valid'


def test_create_invalid_pixel_z_fixture(invalid_pixel):
    assert re.match(r'[0-9]', invalid_pixel.z), f'Z {invalid_pixel.z} is not valid'
    assert 255 >= int(invalid_pixel.x) >= 255, f'X {invalid_pixel.x} is valid'


def test_get_color_invalid_pixel(invalid_pixel):
    for item in invalid_pixel.list_pixels():
        if item == f'{invalid_pixel.x}, {invalid_pixel.y}, {invalid_pixel.z}':
            assert invalid_pixel.get_color() == 'Unknown color', 'Color is not valid'
            assert invalid_pixel.pixels == [], 'Pixel is not valid'




