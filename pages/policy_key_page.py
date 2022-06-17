from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import PolicyKeyLocators


class PolicyKeyPage(BasePage):
    def add_key(self):
        self.browser.find_element(*PolicyKeyLocators.KEY_NAME_INPUT).send_keys(".*")
        self.browser.find_element(*PolicyKeyLocators.KEY_TYPE_INPUT).send_keys("White Key" + Keys.ENTER)
        self.browser.find_element(*PolicyKeyLocators.ELEM_TYPE_SEARCH).send_keys("Windows")
        self.browser.find_element(By.TAG_NAME, "option").click()
        self.browser.find_element(*PolicyKeyLocators.ADD_KEY_BUT).click()

    def should_be_new_key(self):
        assert self.is_element_present(*PolicyKeyLocators.NEW_KEY_SUCCESS_ADD_MESSAGE), \
            "Ключ не добавлен"
