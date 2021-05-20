import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/alert_accept.html')

try:
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(10)

    browser.quit()
