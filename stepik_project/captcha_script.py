import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/math.html')

x = browser.find_element(By.ID, 'input_value').text
y = calc(x)
browser.find_element(By.ID, 'answer').send_keys(y)

browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()

browser.find_element(By.CLASS_NAME, 'btn-default').click()

time.sleep(10)

browser.quit()
