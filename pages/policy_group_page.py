import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import PolicyGroupLocators


class PolicyGroupPage(BasePage):
    def add_key_group(self, policy_group_name):
        self.browser.find_element(*PolicyGroupLocators.POLICY_GROUP_NAME_INPUT).send_keys(policy_group_name)
        time.sleep(2)
        self.browser.find_element(*PolicyGroupLocators.POLICY_GROUP_ACTION_INPUT).click()
        time.sleep(1)
        self.browser.find_element(By.XPATH, "//*[contains(text(),'Создать ошибку')]").click()
        self.browser.find_element(*PolicyGroupLocators.POLICY_GROUP_MODE_INPUT).send_keys("OP" + Keys.ENTER)
        self.browser.find_element(*PolicyGroupLocators.POLICY_GROUP_KEY).click()
        self.browser.find_element(*PolicyGroupLocators.POLICY_GROUP_ADD_BUT).click()

    def should_be_new_policy_group(self):
        assert self.is_element_present(*PolicyGroupLocators.NEW_POLICY_GROUP_SUCCESS_ADD_MESSAGE), \
            "Группа политик не добавлена"

