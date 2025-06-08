
from stepik_project.stepik.Page.product_page import ProductPage
from stepik_project.stepik.Page.base_page import BasePage
from stepik_project.stepik.Page.basket_page import BasketPage
import pytest

@pytest.mark.skip
@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_add_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_add_basket()
    page.should_be_message_price_book()

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_basket()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_basket()
    page.should_not_be_element()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/#'
    page = BasePage(browser, link)
    page.open()
    page.go_to_product_list_page()
    page = ProductPage(browser, browser.current_url)
    page.go_to_product_page()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.should_be_basket_is_empty()
    page.is_not_element_in_basket()
