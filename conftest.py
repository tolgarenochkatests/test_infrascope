import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
