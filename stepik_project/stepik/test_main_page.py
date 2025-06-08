import pytest

from .Page.base_page import BasePage
from .Page.basket_page import BasketPage
from .Page.login_page import LoginPage


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = BasePage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = BasePage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_login_and_registration_form(browser):
    page = LoginPage(browser, 'https://selenium1py.pythonanywhere.com/ru/accounts/login/')
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasePage(browser, 'https://selenium1py.pythonanywhere.com/ru/')
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_basket_is_empty()
    page.is_not_element_in_basket()
