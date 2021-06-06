import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/file_input.html')

    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')\
        .send_keys('first name')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')\
        .send_keys('last name')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]') \
        .send_keys('email')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'some_text.txt')
    browser.find_element(By.ID, 'file').send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(10)

    browser.quit()
