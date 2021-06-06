from selenium import webdriver
import time
import unittest

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

class Registration(unittest.TestCase):
    def test_fall(self):
        browser.get('http://suninjuly.github.io/registration2.html')

        browser.find_element(
            By.CSS_SELECTOR,
            '.first_block .first_class input'
        ).send_keys('name1')
        browser.find_element(
            By.CSS_SELECTOR,
            '.first_block .second_class input'
        ).send_keys('name2')
        browser.find_element(
            By.CSS_SELECTOR,
            '.first_block .third_class input'
        ).send_keys('email')
        browser.find_element(
            By.CSS_SELECTOR,
            'button.btn'
        ).click()
        time.sleep(1)
        message = browser.find_element(By.TAG_NAME, 'h1')
        message_text = message.text
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            message_text
        )

        browser.quit()

    def test_pass(self):
        browser.get('http://suninjuly.github.io/registration1.html')

        browser.find_element(
            By.CSS_SELECTOR,
            '.first_block .first_class input'
        ).send_keys('name1')
        browser.find_element(
            By.CSS_SELECTOR,
            '.first_block .second_class input'
        ).send_keys('name2')
        browser.find_element(
            By.CSS_SELECTOR,
            '.first_block .third_class input'
        ).send_keys('email')
        browser.find_element(
            By.CSS_SELECTOR,
            'button.btn'
        ).click()
        time.sleep(1)
        message = browser.find_element(By.TAG_NAME, 'h1')
        message_text = message.text
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            message_text
        )

        browser.quit()
