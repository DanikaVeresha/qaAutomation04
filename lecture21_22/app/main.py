"""
Task-> automate the following scenario:
"""
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from lecture21_22.timer_settings.timer import timer
from lecture21_22.conf.valid_users_data import get_valid_name, valid_passwords


logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w")
logger = logging.getLogger(__name__)

driver = webdriver.Chrome()


timer(lambda: driver.get('https://www.saucedemo.com/'), 10) # I give 15 seconds to load the page
logger.info(f'Connection with {driver.name} along the path "https://www.saucedemo.com/" was successfully')
username_field = driver.find_element(By.ID, 'user-name')
timer(lambda: username_field.click(), 1)
timer(lambda: username_field.clear(), 2)
logger.info(f'The field "username" is empty')
timer(lambda: username_field.send_keys(get_valid_name()), 2)
logger.info(f'The USERNAME successfully recorded')

password_field = driver.find_element(By.ID, 'password')
timer(lambda: password_field.click(), 1)
timer(lambda: password_field.clear(), 2)
logger.info(f'The field "password" is empty')
timer(lambda: password_field.send_keys(valid_passwords), 2)
logger.info(f'The PASSWORD successfully written')

login_button = driver.find_element(By.ID, 'login-button')
timer(lambda: login_button.click(), 2)
logger.info(f'The user has successfully logged in')
timer(lambda: driver.save_screenshot('page.png'), 4)
logger.info(f'The screenshot of the successful login was saved')

item = driver.find_elements(By.XPATH, '//*[@id="item_4_title_link"]/div')
timer(lambda: item[0].click(), 2)
logger.info(f'The user has successfully selected the item')

user_order = driver.find_element(By.XPATH,
                                 '//*[@id="inventory_item_container"]/div/div/div[1]/img')
timer(lambda: user_order.click(), 3)
timer(lambda: user_order.screenshot('item.png'), 4)
logger.info(f'The screenshot of the selected item was saved')

timer(lambda: driver.refresh(), 4)
logger.info(f'The user has successfully refreshed the page')

timer(lambda: driver.back(), 2)
logger.info(f'The user has successfully moved back')

timer(lambda: driver.back(), 2)
logger.info(f'The user has successfully moved back in main page')

timer(lambda: driver.quit(), 5) # -> close all the tubs
logger.info(f'The user has successfully closed all the tabs')










