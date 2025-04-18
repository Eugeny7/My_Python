import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Otus.hw_4.locators import *


@pytest.mark.smoke
def test_main_page(browser, url):
    wait = WebDriverWait(browser, 5)
    browser.get(url)
    wait.until(EC.visibility_of_element_located(MainPage.DROPDOWN_MY_ACCAUNT)).click()
    wait.until(EC.visibility_of_element_located(MainPage.DROPDOWN_CURRENCY)).click()
    wait.until(EC.visibility_of_element_located(MainPage.INPUT_SEARCH)).click()
    wait.until(EC.visibility_of_element_located(MainPage.BUTTON_SHOP)).click()
    wait.until(EC.visibility_of_element_located(MainPage.BUTTON_CHECKOUT)).click()


def test_admin_page(browser, url):
    wait = WebDriverWait(browser, 3)
    browser.get(f'{url}/administration')
    wait.until(EC.visibility_of_element_located(AdminPage.HEADER_FORM))
    wait.until(EC.visibility_of_element_located(AdminPage.INPUT_USERNAME)).click()
    wait.until(EC.visibility_of_element_located(AdminPage.INPUT_PASSWORD)).click()
    wait.until(EC.visibility_of_element_located(AdminPage.BUTTON_SUBMIT)).click()
    wait.until(EC.visibility_of_element_located(AdminPage.LINK_OPENCART)).click()


def test_registration_page(browser, url):
    wait = WebDriverWait(browser, 4)
    browser.get(f'{url}/en-gb?route=account/register')
    wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_FIRST_NAME)).click()
    wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_LAST_NAME)).click()
    wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_EMAIL)).click()
    wait.until(EC.visibility_of_element_located(RegistrationPage.INPUT_PASSWORD)).click()
    wait.until(EC.visibility_of_element_located(RegistrationPage.BUTTON_CONTINUE)).click()


def test_admin_login(browser, url):
    wait = WebDriverWait(browser, 5)
    actions = ActionChains(browser)
    browser.get(f'{url}/administration/')
    input_name = wait.until(EC.visibility_of_element_located(AdminPage.INPUT_USERNAME))
    input_password = wait.until(EC.visibility_of_element_located(AdminPage.INPUT_PASSWORD))
    actions.move_to_element(input_name).click().send_keys(AdminPage.OPENCART_LOGIN).perform()
    actions.move_to_element(input_password).click().send_keys(AdminPage.OPENCART_PASSWORD).perform()
    wait.until(EC.visibility_of_element_located(AdminPage.BUTTON_SUBMIT)).click()
    wait.until(EC.visibility_of_element_located(AdminPage.DROPDOWN_MENU)).click()
    wait.until(EC.visibility_of_element_located(AdminPage.PROFILE_BUTTON)).click()
    user_name = wait.until(EC.visibility_of_element_located(AdminPage.INPUT_USERNAME)).get_attribute('value')
    user_email = wait.until(EC.visibility_of_element_located(AdminPage.INPUT_EMAIL)).get_attribute('value')
    assert user_name == AdminPage.OPENCART_LOGIN and user_email == AdminPage.DEFAULT_EMAIL_USER


def test_shopping_cart(browser, url):
    wait = WebDriverWait(browser, 7)
    actions = ActionChains(browser)
    browser.get(url)
    name_item_main = wait.until(EC.visibility_of_element_located(MainPage.ITEM_NAME)).text
    item = wait.until(EC.visibility_of_element_located(MainPage.ADD_CART_BUTTON))
    actions.pause(0.5).move_to_element(item).click().perform()
    shopping_cart = wait.until(EC.visibility_of_element_located(MainPage.SHOPPING_CART_BUTTON))
    actions.move_to_element(shopping_cart).pause(0.2).click().perform()
    name_item_shopping = wait.until(EC.visibility_of_element_located(MainPage.ITEM_NAME)).text
    assert name_item_main == name_item_shopping, f'The goods are not consistent'


@pytest.mark.parametrize('currency',
                         [MainPage.CURRENCY_EURO_BUTTON,
                          MainPage.CURRENCY_Dollar_BUTTON,
                          MainPage.CURRENCY_Sterling_BUTTON])
def test_currency(browser, url, currency):
    wait = WebDriverWait(browser, 5)
    actions = ActionChains(browser)
    browser.get(url)
    element = wait.until(EC.visibility_of_element_located(MainPage.CURRENCY_DROPDOWN_MAIN))
    actions.move_to_element(element).click().perform()
    item_currency = wait.until(EC.visibility_of_element_located(currency))
    symbol_currency = item_currency.text[0]
    actions.move_to_element(item_currency).click().perform()
    currency_strong = wait.until(EC.visibility_of_element_located(MainPage.CURRENCY_STRONG)).text
    assert symbol_currency == currency_strong
