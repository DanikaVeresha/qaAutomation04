import pytest
from lecture_20.application.app_Pixel import Pixel
import re


@pytest.mark.parametrize('pixel1', [(Pixel(0, 0, 0))])
@pytest.mark.parametrize('pixel2', [(Pixel(255, 255, 255))])
@pytest.mark.parametrize('pixel3', [(Pixel(128, 127, 140))])
def test_P_pixel_len_all_the_components_is_valid(pixel1, pixel2, pixel3):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
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
    -> Positive test cases:
    """
    assert all(isinstance(i, int) for i in pixel1.__dict__.values()), 'Components is not int type'
    assert all(isinstance(i, int) for i in pixel2.__dict__.values()), 'Components is not int type'
    assert all(isinstance(i, int) for i in pixel3.__dict__.values()), 'Components is not int type'


@pytest.mark.parametrize('pixel', [(0.125, 254.7, 127.5)])
def test_P_components_is_int_type_if_start_values_is_float(pixel):
    """
    1-> 1-> Components of pixel are integer numbers.
    -> Positive test cases:
    """
    assert Pixel(*pixel).__dict__ == {'_Pixel__red': 0, '_Pixel__green': 254, '_Pixel__blue': 127}, \
        'Components isn`t red: 0, green: 255, blue: 127'

##############################################################################################


@pytest.mark.parametrize('pixel', [(-1, 310, 257)])
def test_N_pixel_len_all_the_components_is_invalid(pixel):
    """
    1-> Constructor should take 3 arguments - red, green and blue components of pixel.
    2-> When trying to create object with components out of this range, raise Value Error.
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
    -> Negative test cases:
    """
    with pytest.raises(ValueError) as ex:
        assert Pixel(*pixel).__dict__ == {'_Pixel__red': -200, '_Pixel__green': 5, '_Pixel__blue': 257}, \
            'Components isn`t red: -200, green: 5, blue: 257'
    assert str(ex.value) == 'Components must be in the range [0 .. 255]', \
        'Pixel components is correct'