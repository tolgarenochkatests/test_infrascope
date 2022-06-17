from selenium.webdriver.common.by import By


class SecurLocators:
    DOP_BUT = By.ID, "details-button"
    GO_BUT = By.ID, "proceed-link"


class AuthLocators:
    LOGIN_INPUT = By.ID, "username"
    PAS_INPUT = By.XPATH, ".//div[5]/div/input"
    ENTER_BUT = By.XPATH, "//*[contains(text(),'Войти')]"


class MainLocators:
    SUCCESS_ENTER = By.XPATH, "//*[contains(text(),'Навигация')]"
    DEVICES_LINK = By.XPATH, "//*[contains(text(),'Устройства')]"
    DEVICES_GROUPS_LINK = By.XPATH, "//*[contains(text(),'Группы устройств')]"
    DEVICE_REGISTRY_LINK = By.XPATH, "//*[contains(text(),'Реестр устройств')]"
    POLICY_LINK = By.XPATH, "//*[contains(text(),'Политики ИБ')]"
    SESSION_POLICY_LINK = By.XPATH, "//*[contains(text(),'Политики сессий')]"
    DATA_LINK = By.XPATH, "//*[contains(text(),'Данные')]"
    SDV_LINK = By.XPATH, "//*[contains(text(),'Защищенное хранилище')]"
    USERS_LINK = By.XPATH, "//*[contains(text(),'Пользователи')]"
    CREDENTIAL_LINK = By.XPATH, "//*[contains(text(),'Права')]"


class DevicesGroupsLocators:
    ADD_GROUP_BUT = By.XPATH, "//span[3]/div[2]/span/button"
    ADD_GROUP_NAME_INPUT = By.XPATH, "//section[1]/span[1]/div/div/input"
    ADD_GROUP_SAVE_BUT = By.XPATH, "//*[contains(text(),'Сохранить')]"
    DEVICE_GROUP_REALMS_LINK = By.XPATH, "//*[contains(text(),'Области групп устройств')]"
    DEVICE_GROUP_REALMS_NAME_INPUT = By.XPATH, "//section[1]/div[1]/span/div/div/input"
    DEVICE_GROUP_REALMS_USERS_GROUP_SEARCH_INPUT = By.XPATH, "//div[2]/div/div[1]/div/input"
    DEVICE_GROUP_REALMS_USERS_GROUP_SYSTEM_ADMIN = By.XPATH, "//*[contains(text(),'System.admins')]"
    DEVICE_GROUP_REALMS_DESCRIPTION = By.XPATH, "//section[1]/div[2]/span/div/div/input"
    ADD_DEVICE_GROUP_REALMS_GROUP_SAVE_BUT = By.XPATH, "//*[contains(text(),'Добавить')]"
    PROPERTIES_BUT = By.XPATH, "//*[contains(text(),'Свойства')]"
    KEY_NAME_INPUT = By.XPATH, "//div/div[1]/span/div/div/div/div[1]/input"
    KEY_VALUE_INPUT = By.XPATH, "//span/div/div[2]/span/div/div/input"
    ADD_KEY_BUT = By.XPATH, "//span[2]/span/button"
    KEY_VALUE_CHECK = By.CLASS_NAME, "check"
    CLOSE_PROPERTIES_BUT = By.CLASS_NAME, "delete"


class DeviceRegistryLocators:
    ADD_DEVICE_PLUS = By.XPATH, "//span/span[4]/div[2]/button"
    IP_INPUT = By.XPATH, "//section[1]/span[1]/div/div/input"
    NAME_INPUT = By.XPATH, "//section[1]/span[2]/div/div/input"
    PROTOKOL_INPUT = By.XPATH, "//span[3]/div/div/div/div[1]/input"
    PORT_INPUT = By.XPATH, "//section[1]/span[4]/div/div/input"
    ELEMENT_TYPE_INPUT = By.XPATH, "//span[5]/div/div/div/div[1]/input"
    GROUP_SEARCH_INPUT = By.XPATH, "//section[1]/div[1]/div[1]/div/input"
    ADD_DEVICE_BUT = By.XPATH, "//span[3]/span/button"
    PSEVDO_CHECK = By.CLASS_NAME, "check"
    NEW_DEVICE_SUCCESS_ADD_MESSAGE = By.XPATH, "//*[contains(text(),'Добавлен')]"


class PolicyKeyLocators:
    KEY_NAME_INPUT = By.XPATH, "//div[1]/div[1]/span/div/div/input"
    KEY_TYPE_INPUT = By.XPATH, "//span/div/div/div/div[1]/input"
    ELEM_TYPE_SEARCH = By.XPATH, "//div[3]/div[1]/div/input"
    ADD_KEY_BUT = By.XPATH, "//section[2]/span[2]/span/button"
    NEW_KEY_SUCCESS_ADD_MESSAGE = By.XPATH, "//*[contains(text(),'Добавлено')]"


class PolicyGroupLocators:
    POLICY_GROUP_LINK = By.XPATH, "//*[contains(text(),'Группа правил')]"
    POLICY_GROUP_NAME_INPUT = By.XPATH, "//div[1]/span[1]/div/div/input"
    POLICY_GROUP_ACTION_INPUT = By.XPATH, "//span[1]/div/div/div/div[1]/input"
    POLICY_GROUP_MODE_INPUT = By.XPATH, "//span[3]/div/div/div/div[1]/input"
    POLICY_GROUP_KEY = By.XPATH, "//*[contains(text(),'.*')]"
    POLICY_GROUP_ADD_BUT = By.XPATH, "//section[2]/span[2]/span/button"
    NEW_POLICY_GROUP_SUCCESS_ADD_MESSAGE = By.XPATH, "//*[contains(text(),'Добавлено')]"


class PolicyRealmLocators:
    POLICY_GROUP_LINK = By.XPATH, "//*[contains(text(),'Область политики')]"
    POLICY_REALM_NAME_INPUT = By.XPATH, "//div[1]/span/div/div/input"
    POLICY_GROUP_SEARCH_INPUT = By.XPATH, "//section[1]/div[1]/div/div[1]/div/input"
    POLICY_DEVICES_REALM_SEARCH_INPUT = By.XPATH, "//section[1]/div[2]/div/div[1]/div/input"
    POLICY_REALM_ADD_BUT = By.XPATH, "//section[2]/span[2]/span/button"
    NEW_POLICY_REALM_SUCCESS_ADD_MESSAGE = By.XPATH, "//*[contains(text(),'Добавлено')]"


class SdvLocators:
    SDV_NAME_INPUT = By.XPATH, "//div[1]/span[1]/div/div/input"
    SDV_TYPE_INPUT = By.XPATH, "//span[3]/div/div/div/div[1]/input"
    SDV_TYPE_SELECT = By.XPATH, "/html/body/ul/li[3]"
    SDV_IP_INPUT = By.XPATH, "//span[4]/div/div/input"
    SVD_CIPHER_INPUT = By.XPATH, "//span[5]/div/div/div/div[1]/input"
    SDV_USER_NAME_INPUT = By.XPATH, "//form/div[2]/span[1]/div/div/input"
    SDV_USER_PAS_INPUT = By.XPATH, "//form/div[2]/span[2]/div/div/input"
    SDV_ADD_BUT = By.XPATH, "//span[3]/span/button"
    NEW_SDV_SUCCESS_ADD_MESSAGE = By.XPATH, "//*[contains(text(),'Добавлено')]"


class CredentialLocators:
    USER_NAME_INPUT = By.XPATH, "//div[1]/span[1]/div/div/div/div[1]/input"
    SOURCE_INPUT = By.XPATH, "//div[1]/span[2]/div/div/div/div[1]/input"
    SDV_NAME_INPUT = By.XPATH, "//div[2]/span[1]/div/div/div/div[1]/input"
    ADD_CREDENTIAL_BUT = By.XPATH, "//div[2]/span/section/span[2]/span/button"
    NEW_CREDENTIAL_SUCCESS_ADD_MESSAGE = By.XPATH, "//*[contains(text(),'Добавлено')]"






