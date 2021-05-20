import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    WebDriverWait(browser, 12).until(expected_conditions.
        text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(10)

    browser.quit()
