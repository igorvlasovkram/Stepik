from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/registration2.html')

    browser.find_element(By.CSS_SELECTOR, '.first_block .first_class input')\
        .send_keys('name1')
    browser.find_element(By.CSS_SELECTOR, '.first_block .second_class input')\
        .send_keys('name2')
    browser.find_element(By.CSS_SELECTOR, '.first_block .third_class input')\
        .send_keys('email')
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(1)
    message = browser.find_element(By.TAG_NAME, 'h1')
    message_text = message.text

    assert "Congratulations! You have successfully registered!" == message_text
finally:
    time.sleep(10)

    browser.quit()
