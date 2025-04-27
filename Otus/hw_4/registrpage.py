from Otus.hw_4.basepage import BasePage

class RegPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_browser(self, url):
        self.browser.get(f'{url}/en-gb?route=account/register')














    INPUT_FIRST_NAME = ('xpath', '//input[@id="input-firstname"]')
    INPUT_LAST_NAME = ('xpath', '//input[@id="input-lastname"]')
    INPUT_EMAIL = ('xpath', '//input[@id="input-email"]')
    INPUT_PASSWORD = ('xpath', '//input[@id="input-password"]')
    BUTTON_CONTINUE = ('xpath', '//button[@type="submit" and text()="Continue"]')