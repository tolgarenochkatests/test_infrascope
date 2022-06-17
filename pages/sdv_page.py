import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import SdvLocators


class SdvPage(BasePage):
    def add_sdv(self, sdv_name):
        self.browser.find_element(*SdvLocators.SDV_NAME_INPUT).send_keys(sdv_name)
        self.browser.find_element(*SdvLocators.SDV_TYPE_INPUT).click()
        time.sleep(1)
        self.browser.find_element(*SdvLocators.SDV_TYPE_SELECT).click()
        self.browser.find_element(*SdvLocators.SDV_IP_INPUT).send_keys("10.0.5.188")
        self.browser.find_element(*SdvLocators.SVD_CIPHER_INPUT).click()
        self.browser.find_element(By.XPATH, "//*[contains(text(),'Нет')]").click()
        self.browser.find_element(*SdvLocators.SDV_USER_NAME_INPUT).send_keys("User")
        self.browser.find_element(*SdvLocators.SDV_USER_PAS_INPUT).send_keys("1q2w3e4r5t!")
        self.browser.find_element(*SdvLocators.SDV_ADD_BUT).click()

    def should_be_new_sdv(self):
        assert self.is_element_present(*SdvLocators.NEW_SDV_SUCCESS_ADD_MESSAGE), "SDV не добавлен"


