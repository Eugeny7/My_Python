from Otus.hw_4.basepage import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

class AdminPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_browser(self,url):
        self.browser.get(f'{url}/administration')

    def send_input_name(self, selector, credentials_username):
        wait = WebDriverWait(self.browser, 3)
        actions = ActionChains(self.browser)
        input_username = self.find_element(selector)
        actions.move_to_element(input_username).click().send_keys(credentials_username).perform()

    def send_input_password(self, selector, credentials_password):
        wait = WebDriverWait(self.browser, 3)
        actions = ActionChains(self.browser)
        input_password = self.find_element(selector)
        actions.move_to_element(input_password).click().send_keys(credentials_password).perform()

    OPENCART_LOGIN = 'user'
    OPENCART_PASSWORD = 'bitnami'
    DEFAULT_EMAIL_USER = 'user@example.com'

    INPUT_USERNAME = ('xpath', '//input[@id="input-username"]')
    INPUT_PASSWORD = ('xpath', '//input[@id="input-password"]')
    BUTTON_SUBMIT = ('xpath', '//button[@type="submit"]')
    LINK_OPENCART = ('xpath', '//a[text()="OpenCart"]')
    HEADER_FORM = ('xpath', '//a[text()="OpenCart"]')
    DROPDOWN_MENU = ('xpath', '//span[@class="d-none d-md-inline d-lg-inline"]')
    PROFILE_BUTTON = ('xpath', '//a[@class="dropdown-item" and contains(@href, "user_token")]')
    INPUT_EMAIL = ('xpath', '//input[@id="input-email"]')
