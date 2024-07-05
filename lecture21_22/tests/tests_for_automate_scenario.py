"""
Tests for automate_scenario.py on valid user login
"""
import pytest
import re

from lecture21_22.conf.valid_users_data import valid_names, valid_passwords
from selenium import webdriver
from selenium.webdriver.common.by import By
from lecture21_22.timer_settings.timer import timer


driver = webdriver.Chrome()


@pytest.mark.parametrize('username', [valid_names[0]])
def test_P_valid_standard_user(username):
    """
    Test for valid username
    """
    username.strip()
    assert isinstance(username, str), 'Username must be a string'
    assert re.match(r'^[a-z_]+$', username), 'Username must be standard_user'


@pytest.mark.parametrize('username', [valid_names[2]])
def test_P_valid_problem_user(username):
    """
    Test for valid username
    """
    username.strip()
    assert isinstance(username, str), 'Username must be a string'
    assert re.match(r'^[a-z_]+$', username), 'Username must be problem_user'


@pytest.mark.parametrize('username', [valid_names[3]])
def test_P_valid_performance_glitch_user(username):
    """
    Test for valid username
    """
    assert isinstance(username, str), 'Username must be a string'
    assert re.match(r'^[a-z_]+$', username), 'Username must be performance_glitch_user'


@pytest.mark.parametrize('username', [valid_names[4]])
def test_P_valid_error_user(username):
    """
    Test for valid username
    """
    assert isinstance(username, str), 'Username must be a string'
    assert re.match(r'^[a-z_]+$', username), 'Username must be error_user'


@pytest.mark.parametrize('username', [valid_names[5]])
def test_P_valid_visual_user(username):
    """
    Test for valid username
    """
    assert isinstance(username, str), 'Username must be a string'
    assert re.match(r'^[a-z_]+$', username), 'Username must be visual_user'


@pytest.mark.parametrize('username', [valid_names[1]])
def test_P_invalid_locked_out_user(username):
    """
    Test for valid username
    """
    assert isinstance(username, str), 'Username must be a string'
    assert re.match(r'^[a-z_]+$', username), 'Username must be locked_out_user'


@pytest.mark.parametrize('password', [valid_passwords[0]])
def test_P_valid_password_for_all_the_users(password):
    """
    Test for valid password
    """
    assert isinstance(password, str), 'Password must be a string'
    assert re.match(r'^[a-z_]+$', password), 'Password must be secret_sauce'


@pytest.mark.parametrize('username', [valid_names[0]])
@pytest.mark.parametrize('password', [valid_passwords[0]])
def test_P_standard_user_login(username, password):
    """
    Test for valid user login
    """
    username.strip() # if user enter username with spaces
    password.strip() # if user enter password with spaces
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_standard_user.png'), 2)


@pytest.mark.parametrize('username', [valid_names[2]])
@pytest.mark.parametrize('password', [valid_passwords[0]])
def test_P_problem_user_login(username, password):
    """
    Test for valid user login
    """
    username.strip()  # if user enter username with spaces
    password.strip()  # if user enter password with spaces
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_problem_user.png'), 2)


@pytest.mark.parametrize('username', [valid_names[3]])
@pytest.mark.parametrize('password', [valid_passwords[0]])
def test_P_performance_glitch_user_login(username, password):
    """
    Test for valid user login
    """
    username.strip()  # if user enter username with spaces
    password.strip()  # if user enter password with spaces
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_performance_glitch_user.png'), 2)


@pytest.mark.parametrize('username', [valid_names[4]])
@pytest.mark.parametrize('password', [valid_passwords[0]])
def test_P_error_user_login(username, password):
    """
    Test for valid user login
    """
    username.strip()  # if user enter username with spaces
    password.strip()  # if user enter password with spaces
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_error_user.png'), 2)


@pytest.mark.parametrize('username', [valid_names[5]])
@pytest.mark.parametrize('password', [valid_passwords[0]])
def test_P_visual_user_login(username, password):
    """
    Test for valid user login
    """
    username.strip()  # if user enter username with spaces
    password.strip()  # if user enter password with spaces
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_visual_user.png'), 2)

##################################################################################################


@pytest.mark.parametrize('username', [valid_names[1]])
@pytest.mark.parametrize('password', [valid_passwords[0]])
def test_N_locked_out_user_login(username, password):
    """
    Test for invalid user login
    """
    username.strip()
    password.strip()
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_locked_out_user.png'), 2)


@pytest.mark.parametrize('username', [' standard_user '])
@pytest.mark.parametrize('password', ['secret_sauce'])
def test_N_if_enter_any_username_with_spaces_and_valid_password(username, password):
    """
    Test for valid username
    """
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_invalid_standard_user.png'), 2)


@pytest.mark.parametrize('username', ['danika'])
@pytest.mark.parametrize('password', ['secret_sauce'])
def test_N_if_enter_any_username_and_valid_password(username, password):
    """
    Test for valid username
    """
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_invalid_danika.png'), 2)


@pytest.mark.parametrize('username', ['error_user'])
@pytest.mark.parametrize('password', ['12345678'])
def test_N_if_enter_valid_username_and_invalid_password(username, password):
    """
    Test for valid username
    """
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_invalid_error_user.png'), 2)


@pytest.mark.parametrize('username', ['standard_user'])
@pytest.mark.parametrize('password', [' secret_sauce'])
def test_N_if_enter_valid_username_and_valid_password_with_space(username, password):
    """
    Test for valid username
    """
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_invalid_standard_user.png'), 2)


@pytest.mark.parametrize('username', ['danika'])
@pytest.mark.parametrize('password', [' 12345678'])
def test_N_if_enter_invalid_username_password(username, password):
    """
    Test for valid username
    """
    timer(lambda: driver.get('https://www.saucedemo.com/'), 10)
    username_field = driver.find_element(By.ID, 'user-name')
    timer(lambda: username_field.click(), 1)
    timer(lambda: username_field.clear(), 2)
    timer(lambda: username_field.send_keys(username), 2)
    password_field = driver.find_element(By.ID, 'password')
    timer(lambda: password_field.click(), 1)
    timer(lambda: password_field.clear(), 2)
    timer(lambda: password_field.send_keys(password), 2)
    login_button = driver.find_element(By.ID, 'login-button')
    timer(lambda: login_button.click(), 4)
    timer(lambda: driver.save_screenshot('result_of_confirmed_login_for_invalid_danika.png'), 2)

