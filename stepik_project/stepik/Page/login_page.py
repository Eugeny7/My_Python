from .base_page import BasePage
from stepik_project.stepik.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.open()
        assert LoginPageLocators.TEXT in self.browser.current_url

    def should_be_login_form(self):
        self.open()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM) , 'Login form not found'

    def should_be_register_form(self):
        self.open()
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration form not found'