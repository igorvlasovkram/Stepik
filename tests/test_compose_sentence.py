import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as match
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize('partial_link',
                         ['236895/step/1',
                          '236896/step/1',
                          '236897/step/1',
                          '236898/step/1',
                          '236899/step/1',
                          '236903/step/1',
                          '236904/step/1',
                          '236905/step/1']
                         )
def test_step(browser, partial_link):
    browser.get(f'https://stepik.org/lesson/{partial_link}')
    answer = math.log(int(time.time()))

    WebDriverWait(browser, 10) \
        .until(match.visibility_of_element_located((By.CLASS_NAME, 'textarea')))
    browser.find_element(By.CLASS_NAME, 'ember-text-area').send_keys(str(answer))
    WebDriverWait(browser, 10) \
        .until(match.element_to_be_clickable
               ((By.CLASS_NAME, 'submit-submission')))
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    WebDriverWait(browser, 10) \
        .until(match.visibility_of_element_located
               ((By.CLASS_NAME, 'smart-hints__hint')))
    optional_feedback = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')

    assert 'Correct!' in optional_feedback.text, 'Your answer is not correct!'
