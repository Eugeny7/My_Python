from Otus.hw_4.src.basepage import BasePage
import allure


class RegPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    INPUT_FIRST_NAME = ('xpath', '//input[@id="input-firstname"]')
    INPUT_LAST_NAME = ('xpath', '//input[@id="input-lastname"]')
    INPUT_EMAIL = ('xpath', '//input[@id="input-email"]')
    INPUT_PASSWORD = ('xpath', '//input[@id="input-password"]')
    BUTTON_CONTINUE = ('xpath', '//button[@type="submit" and text()="Continue"]')

    def open_browser(self, url):
        with allure.step('Переход на страницу регистрации'):
            self.browser.get(f'{url}/en-gb?route=account/register')
