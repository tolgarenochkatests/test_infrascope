import time
import pytest
from pages.auth_page import AuthPage
from pages.credential_page import CredentialPage
from pages.device_registry_page import DeviceRegistryPage
from pages.devices_group_page import DevicesGroupPage
from pages.locators import MainLocators, DevicesGroupsLocators, PolicyGroupLocators, PolicyRealmLocators
from pages.main_page import MainPage
from random import choice
from string import ascii_uppercase
from pages.policy_group_page import PolicyGroupPage
from pages.policy_key_page import PolicyKeyPage
from pages.policy_realm_page import PolicyRealmPage
from pages.sdv_page import SdvPage

group_name = ''.join(choice(ascii_uppercase) for i in range(12))
realms_name = ''.join(choice(ascii_uppercase) for i in range(8))
device_name = "RDP"
policy_group_name = ''.join(choice(ascii_uppercase) for i in range(4))
policy_realm_name = ''.join(choice(ascii_uppercase) for i in range(4))
sdv_name = ''.join(choice(ascii_uppercase) for i in range(3))


class TestEToE:
    def test_auth_with_valid_login_and_pas(self, browser):
        link = "https://10.0.5.47/"
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_admin()
        page.should_enter_be_successful()
        time.sleep(1)

    # @pytest.mark.skip
    def test_create_devices_group(self, browser):
        page = MainPage(browser, browser.current_url)
        page.go_to_page(*MainLocators.DEVICES_LINK)
        page.go_to_page(*MainLocators.DEVICES_GROUPS_LINK)
        page = DevicesGroupPage(browser, browser.current_url)
        page.add_devices_group(group_name)
        time.sleep(1)
        page.should_be_new_group(group_name)
        page.add_group_properties(group_name)
        page.should_be_properties()
        page.close_properties()
        time.sleep(3)

    # @pytest.mark.skip
    def test_create_device_group_realms(self, browser):
        page = DevicesGroupPage(browser, browser.current_url)
        page.go_to_page(*DevicesGroupsLocators.DEVICE_GROUP_REALMS_LINK)
        time.sleep(1)
        page.add_device_group_realms(group_name, realms_name)
        page.should_be_new_group_realm(realms_name)

    # @pytest.mark.skip
    def test_create_device(self, browser):
        page = MainPage(browser, browser.current_url)
        page.go_to_page(*MainLocators.DEVICE_REGISTRY_LINK)
        page = DeviceRegistryPage(browser, browser.current_url)
        time.sleep(1)
        page.add_device(device_name, group_name)
        page.should_be_new_device()

    # @pytest.mark.skip
    def test_create_policy_key(self, browser):
        page = MainPage(browser, browser.current_url)
        page.go_to_page(*MainLocators.DEVICES_LINK)
        page.go_to_page(*MainLocators.POLICY_LINK)
        page.go_to_page(*MainLocators.SESSION_POLICY_LINK)
        page = PolicyKeyPage(browser, browser.current_url)
        time.sleep(1)
        page.add_key()
        page.should_be_new_key()

    # @pytest.mark.skip
    def test_create_group_policy(self, browser):
        page = PolicyKeyPage(browser, browser.current_url)
        page.go_to_page(*PolicyGroupLocators.POLICY_GROUP_LINK)
        time.sleep(2)
        page = PolicyGroupPage(browser, browser.current_url)
        page.add_key_group(policy_group_name)
        page.should_be_new_policy_group()

    # @pytest.mark.skip
    def test_create_realm_policy(self, browser):
        page = PolicyGroupPage(browser, browser.current_url)
        page.go_to_page(*PolicyRealmLocators.POLICY_GROUP_LINK)
        time.sleep(1)
        page = PolicyRealmPage(browser, browser.current_url)
        page.add_policy_realm(policy_realm_name, policy_group_name, realms_name)
        page.should_be_new_policy_realm()

    # @pytest.mark.skip
    def test_crate_sdv(self, browser):
        page = MainPage(browser, browser.current_url)
        page.go_to_page(*MainLocators.POLICY_LINK)
        time.sleep(1)
        page.go_to_page(*MainLocators.DATA_LINK)
        page.go_to_page(*MainLocators.SDV_LINK)
        time.sleep(5)
        page = SdvPage(browser, browser.current_url)
        page.add_sdv(sdv_name)
        page.should_be_new_sdv()

    # @pytest.mark.skip
    def test_add_credential(self, browser):
        page = MainPage(browser, browser.current_url)
        page.go_to_page(*MainLocators.DATA_LINK)
        time.sleep(1)
        page.go_to_page(*MainLocators.USERS_LINK)
        page.go_to_page(*MainLocators.CREDENTIAL_LINK)
        page = CredentialPage(browser, browser.current_url)
        time.sleep(4)
        page.add_credential(sdv_name)
        page.should_be_new_credential()

    # @pytest.mark.skip
    def test_open_device(self, browser):
        page = MainPage(browser, browser.current_url)
        page.go_to_page(*MainLocators.DEVICES_LINK)
        page.go_to_page(*MainLocators.DEVICE_REGISTRY_LINK)
        page = DeviceRegistryPage(browser, browser.current_url)
        time.sleep(1)
        page.open_device(group_name, sdv_name)
        time.sleep(10)



