from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("foo bar")

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)

    browser.quit()
