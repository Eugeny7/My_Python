from .Page.main_page import MainPage
from .Page.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.should_be_login_link()

def test_login_and_registration_form(browser):
    page = LoginPage(browser, 'https://selenium1py.pythonanywhere.com/ru/accounts/login/')
    page.should_be_login_page()