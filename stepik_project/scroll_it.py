import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/execute_script.html')

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()

    radiobuttton = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           radiobuttton)
    radiobuttton.click()

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(5)

    browser.quit()
