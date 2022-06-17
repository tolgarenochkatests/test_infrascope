import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import DevicesGroupsLocators


class DevicesGroupPage(BasePage):
    def add_devices_group(self, name):
        self.browser.find_element(*DevicesGroupsLocators.ADD_GROUP_BUT).click()
        self.browser.find_element(*DevicesGroupsLocators.ADD_GROUP_NAME_INPUT).send_keys(name)
        self.browser.find_element(*DevicesGroupsLocators.ADD_GROUP_SAVE_BUT).click()

    def should_be_new_group(self, name):
        assert self.is_element_present(By.XPATH, f"//*[contains(text(),'{name}')]"), "Новая группа не появилась в " \
                                                                                     "списке групп "

    def add_device_group_realms(self, name_gr, name_r):
        self.browser.find_element(*DevicesGroupsLocators.DEVICE_GROUP_REALMS_NAME_INPUT).send_keys(name_r)
        self.browser.find_element(By.XPATH, f"//*[contains(text(),'{name_gr}')]").click()
        self.browser.find_element(*DevicesGroupsLocators.DEVICE_GROUP_REALMS_USERS_GROUP_SEARCH_INPUT).send_keys("system")
        self.browser.find_element(*DevicesGroupsLocators.DEVICE_GROUP_REALMS_USERS_GROUP_SYSTEM_ADMIN).click()
        self.browser.find_element(*DevicesGroupsLocators.DEVICE_GROUP_REALMS_DESCRIPTION).send_keys("description")
        self.browser.find_element(*DevicesGroupsLocators.ADD_DEVICE_GROUP_REALMS_GROUP_SAVE_BUT).click()

    def should_be_new_group_realm(self, name_r):
        assert self.is_element_present(By.XPATH, f"//*[contains(text(),'{name_r}')]"), "Новая область групп не " \
                                                                                       "появилась в списке"

    def add_group_properties(self, name_gr):
        group = self.browser.find_element(By.XPATH, f"//*[contains(text(),'{name_gr}')]")
        action = ActionChains(self.browser)
        action.context_click(group).perform()
        self.browser.find_element(*DevicesGroupsLocators.PROPERTIES_BUT).click()
        key = self.browser.find_element(*DevicesGroupsLocators.KEY_NAME_INPUT)
        key.send_keys("addSessionUserToUserSelection" + Keys.ENTER)
        value = self.browser.find_element(*DevicesGroupsLocators.KEY_VALUE_INPUT)
        value.send_keys("true")
        add = self.browser.find_element(*DevicesGroupsLocators.ADD_KEY_BUT)
        add.click()
        time.sleep(1)
        key2 = self.browser.find_element(*DevicesGroupsLocators.KEY_NAME_INPUT)
        key2.send_keys("addManualLoginToUserSelection" + Keys.ENTER)
        check = self.browser.find_element(*DevicesGroupsLocators.KEY_VALUE_CHECK)
        check.click()
        add.click()
        time.sleep(1)
        key3 = self.browser.find_element(*DevicesGroupsLocators.KEY_NAME_INPUT)
        key3.send_keys("addAssignedCredentialToUserSelection" + Keys.ENTER)
        check = self.browser.find_element(*DevicesGroupsLocators.KEY_VALUE_CHECK)
        check.click()
        add.click()
        time.sleep(1)

    def should_be_properties(self):
        assert self.is_element_present(By.XPATH, "//*[contains(text(),'addSessionUserToUserSelection')]"), \
            "Не добавлено свойство addSessionUserToUserSelection"
        assert self.is_element_present(By.XPATH, "//*[contains(text(),'addManualLoginToUserSelection')]"), \
            "Не добавлено свойство addManualLoginToUserSelection"
        assert self.is_element_present(By.XPATH, "//*[contains(text(),'addAssignedCredentialToUserSelection')]"), \
            "Не добавлено свойство addAssignedCredentialToUserSelection"

    def close_properties(self):
        self.browser.find_element(*DevicesGroupsLocators.CLOSE_PROPERTIES_BUT).click()
        time.sleep(2)


