from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.locators import SecurLocators
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        self.browser.find_element(*SecurLocators.DOP_BUT).click()
        self.browser.find_element(*SecurLocators.GO_BUT).click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_page(self, how, what):
        link = self.browser.find_element(how, what)
        link.click()

    def scroll_down(self):
        self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
