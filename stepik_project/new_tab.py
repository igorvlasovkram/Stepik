import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/redirect_accept.html')

try:
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    workspace_window = browser.window_handles[1]
    browser.switch_to.window(workspace_window)

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    time.sleep(10)

    browser.quit()
