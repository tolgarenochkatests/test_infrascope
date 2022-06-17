from pages.base_page import BasePage
from pages.locators import AuthLocators, MainLocators


class AuthPage(BasePage):
    def enter_as_admin(self):
        self.browser.find_element(*AuthLocators.LOGIN_INPUT).send_keys("admin")
        self.browser.find_element(*AuthLocators.PAS_INPUT).send_keys("1q2w3e4r5t")
        self.browser.find_element(*AuthLocators.ENTER_BUT).click()

    def should_enter_be_successful(self):
        assert self.is_element_present(*MainLocators.SUCCESS_ENTER), "Unsuccessful enter"

