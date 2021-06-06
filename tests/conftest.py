import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    options = webdriver.FirefoxOptions()
    options.headless = True
    browser = webdriver.Firefox(options=options)

    yield browser

    browser.quit()
