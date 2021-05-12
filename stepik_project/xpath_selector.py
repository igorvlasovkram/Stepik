from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/find_xpath_form')

    browser.find_element_by_name('first_name').send_keys("Ivan")
    browser.find_element_by_name('last_name').send_keys("Petrov")
    browser.find_element_by_class_name('city').send_keys("Smolensk")
    browser.find_element_by_id('country').send_keys("Russia")
    browser.find_element_by_xpath('//button[text()="Submit"]').click()

finally:
    time.sleep(30)

    browser.quit()
