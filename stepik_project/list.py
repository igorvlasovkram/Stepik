from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/selects1.html')

amount = int(browser.find_element(By.ID, 'num1').text) \
         + int(browser.find_element(By.ID, 'num2').text)

browser.find_element(By.ID, 'dropdown').click()
browser.find_element(By.CSS_SELECTOR, f'option[value="{str(amount)}"]').click()

browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
