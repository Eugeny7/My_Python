import allure
import pytest
from Otus.hw_4.src.mainpage import MainPage
from Otus.hw_4.src.adminpage import AdminPage
from Otus.hw_4.src.registrpage import RegPage


@allure.title('Проверка наличия элементов на главной странице Opencart')
def test_main_page(browser, url):
    element = MainPage(browser)
    element.open_browser(url)
    element.find_element(element.DROPDOWN_MY_ACCAUNT)
    element.find_element(element.DROPDOWN_CURRENCY)
    element.find_element(element.INPUT_SEARCH)
    element.find_element(element.BUTTON_SHOP)
    element.find_element(element.BUTTON_CHECKOUT)

@allure.title('Проверка наличия элементов на странице личного кабинета администратора')
def test_admin_page(browser, url):
    element = AdminPage(browser)
    element.open_browser(url)
    element.find_element(element.HEADER_FORM)
    element.find_element(element.INPUT_USERNAME)
    element.find_element(element.INPUT_PASSWORD)
    element.find_element(element.BUTTON_SUBMIT)
    element.find_element(element.LINK_OPENCART)

@allure.title('Проверка наличия элементов на странице регистрации Opencart')
def test_registration_page(browser, url):
    element = RegPage(browser)
    element.open_browser(url)
    element.find_element(element.INPUT_FIRST_NAME)
    element.find_element(element.INPUT_LAST_NAME)
    element.find_element(element.INPUT_EMAIL)
    element.find_element(element.INPUT_PASSWORD)
    element.find_element(element.BUTTON_CONTINUE)
    element.find_element(element.INPUT_FIRST_NAME)

@allure.title('Проверка авторизации в личный кабинет администратора')
def test_admin_login(browser, url):
    element = AdminPage(browser)
    element.open_browser(url)
    element.send_input_name(element.INPUT_USERNAME, element.OPENCART_LOGIN)
    element.send_input_password(element.INPUT_PASSWORD, element.OPENCART_PASSWORD)
    element.find_element(element.BUTTON_SUBMIT).click()
    element.find_element(element.DROPDOWN_MENU).click()
    element.find_element(element.PROFILE_BUTTON).click()
    user_name = element.get_attribute(element.INPUT_USERNAME)
    user_email = element.get_attribute(element.INPUT_EMAIL)
    assert user_name == element.OPENCART_LOGIN and user_email == element.DEFAULT_EMAIL_USER

@allure.title('Проверка добавления товара в корзину на главной странице Opencart ')
def test_shopping_cart(browser, url):
    element = MainPage(browser)
    element.open_browser(url)
    name_item_main = element.get_text(MainPage.ITEM_NAME)
    item = element.find_element(MainPage.ADD_CART_BUTTON)
    element.click_element(item)
    shopping_cart = element.find_element(MainPage.SHOPPING_CART_BUTTON)
    element.click_element(shopping_cart)
    name_item_shopping = element.get_text(MainPage.ITEM_NAME)
    assert name_item_main == name_item_shopping, f'The goods are not consistent'

@allure.title('Проверка изменения валюты на главной странице Opencart')
@pytest.mark.parametrize('currency',
                         [MainPage.CURRENCY_EURO_BUTTON,
                          MainPage.CURRENCY_Dollar_BUTTON,
                          MainPage.CURRENCY_Sterling_BUTTON])
def test_currency(browser, url, currency):
    element = MainPage(browser)
    element.open_browser(url)
    dropdown_currency = element.find_element(element.CURRENCY_DROPDOWN_MAIN)
    element.click_element(dropdown_currency)
    item_currency = element.find_element(currency)
    symbol_currency = item_currency.text[0]
    element.click_element(item_currency)
    browser.refresh()
    currency_strong = element.get_text(element.CURRENCY_STRONG)
    assert symbol_currency == currency_strong
