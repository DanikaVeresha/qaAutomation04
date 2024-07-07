"""
Please make a test for a successful login for this page, just in one file using pytes+selenium
https://www.saucedemo.com/
"""
import pytest

from lecture21_22.conf.valid_users_data import valid_names, valid_passwords
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(15)


@pytest.mark.parametrize('name', [(valid_names[0])])
@pytest.mark.parametrize('password', [valid_passwords])
def test_login_for_standard_user(name, password):
    """
    1-> Open the page https://www.saucedemo.com/
    2-> Find the field for the username
    3-> Click on the field for the username
    4-> Clear the field for the username
    5-> Send the username standard_user to the field for the username
    6-> Find the field for the password
    7-> Click on the field for the password
    8-> Clear the field for the password
    9-> Send the password secret_sauce to the field for the password
    10-> Find the login button
    11-> Click on the login button
    12-> Save the screenshot of the page
    """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_standard_user.png')
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
        'The user has not logged in'


@pytest.mark.parametrize('name', [(valid_names[2])])
@pytest.mark.parametrize('password', [valid_passwords])
def test_login_for_problem_user(name, password):
    """
    1-> Open the page https://www.saucedemo.com/
    2-> Find the field for the username
    3-> Click on the field for the username
    4-> Clear the field for the username
    5-> Send the username problem_user to the field for the username
    6-> Find the field for the password
    7-> Click on the field for the password
    8-> Clear the field for the password
    9-> Send the password secret_sauce to the field for the password
    10-> Find the login button
    11-> Click on the login button
    12-> Save the screenshot of the page
    """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_problem_user.png')
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
        'The user has not logged in'


@pytest.mark.parametrize('name', [(valid_names[3])])
@pytest.mark.parametrize('password', [valid_passwords])
def test_login_for_performance_glitch_user(name, password):
    """
    1-> Open the page https://www.saucedemo.com/
    2-> Find the field for the username
    3-> Click on the field for the username
    4-> Clear the field for the username
    5-> Send the username performance_glitch_user to the field for the username
    6-> Find the field for the password
    7-> Click on the field for the password
    8-> Clear the field for the password
    9-> Send the password secret_sauce to the field for the password
    10-> Find the login button
    11-> Click on the login button
    12-> Save the screenshot of the page
    """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_performance_glitch_user.png')
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
        'The user has not logged in'


@pytest.mark.parametrize('name', [(valid_names[4])])
@pytest.mark.parametrize('password', [valid_passwords])
def test_login_for_error_user(name, password):
    """
   1-> Open the page https://www.saucedemo.com/
   2-> Find the field for the username
   3-> Click on the field for the username
   4-> Clear the field for the username
   5-> Send the username error_user to the field for the username
   6-> Find the field for the password
   7-> Click on the field for the password
   8-> Clear the field for the password
   9-> Send the password secret_sauce to the field for the password
   10-> Find the login button
   11-> Click on the login button
   12-> Save the screenshot of the page
   """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_error_user.png')
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
        'The user has not logged in'


@pytest.mark.parametrize('name', [(valid_names[5])])
@pytest.mark.parametrize('password', [valid_passwords])
def test_login_for_visual_user(name, password):
    """
    1-> Open the page https://www.saucedemo.com/
    2-> Find the field for the username
    3-> Click on the field for the username
    4-> Clear the field for the username
    5-> Send the username visual_user to the field for the username
    6-> Find the field for the password
    7-> Click on the field for the password
    8-> Clear the field for the password
    9-> Send the password secret_sauce to the field for the password
    10-> Find the login button
    11-> Click on the login button
    12-> Save the screenshot of the page
    """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_visual_user.png')
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
        'The user has not logged in'


@pytest.mark.parametrize('name', [(valid_names[1])])
@pytest.mark.parametrize('password', [valid_passwords])
def test_login_for_locked_out_user(name, password):
    """
    1-> Open the page https://www.saucedemo.com/
    2-> Find the field for the username
    3-> Click on the field for the username
    4-> Clear the field for the username
    5-> Send the username locked_out_user to the field for the username
    6-> Find the field for the password
    7-> Click on the field for the password
    8-> Clear the field for the password
    9-> Send the password secret_sauce to the field for the password
    10-> Find the login button
    11-> Click on the login button
    12-> Save the screenshot of the page
    """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_locked_out_user.png')
    with (pytest.raises(AssertionError)):
        # Asserting that the resulting URL matches https://www.saucedemo.com/inventory.html,
        # proving that the user has visited the site and has successfully logged in, raises an
        # exception of type "AssertionError".
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
            'The user has not logged in'


@pytest.mark.parametrize('name', ['invalid_username'])
@pytest.mark.parametrize('password', [valid_passwords])
def test_login_for_invalid_username(name, password):
    """
    1-> Open the page https://www.saucedemo.com/
    2-> Find the field for the username
    3-> Click on the field for the username
    4-> Clear the field for the username
    5-> Send the username invalid_username to the field for the username
    6-> Find the field for the password
    7-> Click on the field for the password
    8-> Clear the field for the password
    9-> Send the password secret_sauce to the field for the password
    10-> Find the login button
    11-> Click on the login button
    12-> Save the screenshot of the page
    """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_invalid_username.png')
    with (pytest.raises(AssertionError)):
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
            'The user has not logged in'


@pytest.mark.parametrize('name', [(valid_names[0])])
@pytest.mark.parametrize('password', ['invalid_password'])
def test_login_for_standard_user_where_invalid_password(name, password):
    """
    1-> Open the page https://www.saucedemo.com/
    2-> Find the field for the username
    3-> Click on the field for the username
    4-> Clear the field for the username
    5-> Send the username standard_user to the field for the username
    6-> Find the field for the password
    7-> Click on the field for the password
    8-> Clear the field for the password
    9-> Send the password invalid_password to the field for the password
    10-> Find the login button
    11-> Click on the login button
    12-> Save the screenshot of the page
    """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_standard_user_with_invalid_password.png')
    with (pytest.raises(AssertionError)):
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
            'The user has not logged in'


@pytest.mark.parametrize('name', ['invalid_username'])
@pytest.mark.parametrize('password', ['invalid_password'])
def test_login_for_user_where_all_the_data_is_invalid(name, password):
    """
    1-> Open the page https://www.saucedemo.com/
    2-> Find the field for the username
    3-> Click on the field for the username
    4-> Clear the field for the username
    5-> Send the username invalid_username to the field for the username
    6-> Find the field for the password
    7-> Click on the field for the password
    8-> Clear the field for the password
    9-> Send the password invalid_password to the field for the password
    10-> Find the login button
    11-> Click on the login button
    12-> Save the screenshot of the page
    """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_invalid_username_with_invalid_password.png')
    with (pytest.raises(AssertionError)):
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
            'The user has not logged in'


@pytest.mark.parametrize('name', [' standard_user '])
@pytest.mark.parametrize('password', [valid_passwords])
def test_login_for_valid_username_and_valid_password_where_space_in_username(name, password):
    """
    1-> Open the page https://www.saucedemo.com/
    2-> Find the field for the username
    3-> Click on the field for the username
    4-> Clear the field for the username
    5-> Send the username standard_user to the field for the username
    6-> Find the field for the password
    7-> Click on the field for the password
    8-> Clear the field for the password
    9-> Send the password secret_sauce to the field for the password
    10-> Find the login button
    11-> Click on the login button
    12-> Save the screenshot of the page
    """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_standard_user_with_space_in_name.png')
    with (pytest.raises(AssertionError)):
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
            'The user has not logged in'


@pytest.mark.parametrize('name', [(valid_names[0])])
@pytest.mark.parametrize('password', ['secret_sauce '])
def test_login_for_valid_username_and_valid_password_where_space_in_password(name, password):
    """
    1-> Open the page https://www.saucedemo.com/
    2-> Find the field for the username
    3-> Click on the field for the username
    4-> Clear the field for the username
    5-> Send the username standard_user to the field for the username
    6-> Find the field for the password
    7-> Click on the field for the password
    8-> Clear the field for the password
    9-> Send the password secret_sauce to the field for the password
    10-> Find the login button
    11-> Click on the login button
    12-> Save the screenshot of the page
    """
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.click()
    username_field.clear()
    username_field.send_keys(name)
    password_field = driver.find_element(By.ID, 'password')
    password_field.click()
    password_field.clear()
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    driver.save_screenshot('login_for_standard_user_with_space_in_password.png')
    with (pytest.raises(AssertionError)):
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
            'The user has not logged in'
