import math
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/find_link_text')
driver.find_element_by_link_text\
    (str(math.ceil(math.pow(math.pi, math.e)*10000))).click()

try:
    driver.find_element_by_name('first_name')\
        .send_keys("Ivan")
    driver.find_element_by_name('last_name')\
        .send_keys("Petrov")
    driver.find_element_by_class_name('city')\
        .send_keys("Smolensk")
    driver.find_element_by_id('country')\
        .send_keys("Russia")
    driver.find_element_by_css_selector("button.btn")\
        .click()

finally:
    time.sleep(30)

    driver.quit()
