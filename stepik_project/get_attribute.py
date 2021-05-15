import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/get_attribute.html')

x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
y = calc(x)
browser.find_element(By.ID, 'answer').send_keys(y)

browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()

browser.find_element(By.CLASS_NAME, 'btn-default').click()

time.sleep(10)

browser.quit()
