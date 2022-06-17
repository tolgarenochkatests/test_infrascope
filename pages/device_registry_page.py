import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import DeviceRegistryLocators


class DeviceRegistryPage(BasePage):
    def add_device(self, name_d, name_gr):
        time.sleep(5)
        self.browser.find_element(*DeviceRegistryLocators.ADD_DEVICE_PLUS).click()
        self.browser.find_element(*DeviceRegistryLocators.IP_INPUT).send_keys("10.0.5.188")
        self.browser.find_element(*DeviceRegistryLocators.NAME_INPUT).send_keys(name_d)
        self.browser.find_element(*DeviceRegistryLocators.PROTOKOL_INPUT).send_keys("RDP" + Keys.ENTER)
        self.browser.find_element(*DeviceRegistryLocators.PORT_INPUT).send_keys("3389")
        self.browser.find_element(*DeviceRegistryLocators.ELEMENT_TYPE_INPUT).send_keys("Windows" + Keys.ENTER)
        name_gr_part = name_gr[0:4]
        self.browser.find_element(*DeviceRegistryLocators.GROUP_SEARCH_INPUT).send_keys(name_gr_part)
        self.scroll_down()
        self.browser.find_element(By.TAG_NAME, "option").click()
        self.browser.find_element(*DeviceRegistryLocators.PSEVDO_CHECK).click()
        self.browser.find_element(*DeviceRegistryLocators.ADD_DEVICE_BUT).click()

    def should_be_new_device(self):
        assert self.is_element_present(*DeviceRegistryLocators.NEW_DEVICE_SUCCESS_ADD_MESSAGE), "Устройство не добавлено"

    def open_device(self, device_group_name, sdv_name):
        group = self.browser.find_element(By.XPATH, f"//*[contains(text(), '{device_group_name}')]")
        ActionChains(self.browser).context_click(group).perform()
        self.browser.find_element(By.XPATH, "//div[2]/ul/li/a").click()
        self.browser.find_element(By.XPATH, "//td[1]/span/span/button").click()
        self.browser.find_element(By.XPATH, "//*[contains(text(), 'Открыть удаленный рабочий стол')]").click()
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[1])
        self.browser.find_element(By.XPATH, f"//*[contains(text(),'User(Secret Data Vault: {sdv_name} )')]").click()
        time.sleep(1)
        self.browser.find_element(By.XPATH, "//*[contains(text(), 'Desktop')]").click()
