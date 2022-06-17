from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import PolicyRealmLocators


class PolicyRealmPage(BasePage):
    def add_policy_realm(self, policy_realm_name, policy_group_name, device_realm_name):
        self.browser.find_element(*PolicyRealmLocators.POLICY_REALM_NAME_INPUT).send_keys(policy_realm_name)
        policy_group_name_part = policy_group_name[0:3]
        self.browser.find_element(*PolicyRealmLocators.POLICY_GROUP_SEARCH_INPUT).send_keys(policy_group_name_part)
        self.browser.find_element(By.XPATH, f"//*[contains(text(),'{policy_group_name}')]").click()
        device_realm_name_part = device_realm_name[0:4]
        self.browser.find_element(*PolicyRealmLocators.POLICY_DEVICES_REALM_SEARCH_INPUT).send_keys(device_realm_name_part)
        self.browser.find_element(By.XPATH, f"//*[contains(text(),'{device_realm_name}')]").click()
        self.browser.find_element(*PolicyRealmLocators.POLICY_REALM_ADD_BUT).click()

    def should_be_new_policy_realm(self):
        assert self.is_element_present(*PolicyRealmLocators.NEW_POLICY_REALM_SUCCESS_ADD_MESSAGE), \
            "Область политик не добавлена"