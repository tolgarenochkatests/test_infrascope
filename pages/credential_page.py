import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import CredentialLocators


class CredentialPage(BasePage):
    def add_credential(self, sdv_name):
        self.browser.find_element(*CredentialLocators.USER_NAME_INPUT).click()
        self.browser.find_element(By.XPATH, "//*[contains(text(),'admin')]").click()
        self.browser.find_element(*CredentialLocators.SOURCE_INPUT).click()
        self.browser.find_element(By.XPATH, "//*[contains(text(),'Secret Data Vault')]").click()
        self.browser.find_element(*CredentialLocators.SDV_NAME_INPUT).send_keys(sdv_name + Keys.ENTER)
        self.browser.find_element(*CredentialLocators.ADD_CREDENTIAL_BUT).click()

    def should_be_new_credential(self):
        assert self.is_element_present(*CredentialLocators.NEW_CREDENTIAL_SUCCESS_ADD_MESSAGE), "Права не добавлены"
