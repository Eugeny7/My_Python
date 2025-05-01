from Otus.hw_4.src.basepage import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    DROPDOWN_MY_ACCAUNT = ('xpath', '//a[@class="dropdown-toggle" and @href!="#"]')
    DROPDOWN_CURRENCY = ('xpath', '//a[@class="dropdown-toggle" and @href="#"]')
    INPUT_SEARCH = ('xpath', '//input[@name="search"]')
    BUTTON_SHOP = ('xpath', '//button[@type="button" and @data-bs-toggle="dropdown"]')
    BUTTON_CHECKOUT = ('xpath', '//span[@class="d-none d-md-inline" and text()="Checkout"]')
    ITEM_NAME = ('xpath', '//h4/a[text()="MacBook"]')
    ADD_CART_BUTTON = ('css selector', 'button[formaction*="cart.add"]')
    SHOPPING_CART_BUTTON = ('xpath', '//span[@class="d-none d-md-inline" and text()="Shopping Cart"]')
    CURRENCY_DROPDOWN_MAIN = ('xpath', '//span[text()="Currency"]')
    CURRENCY_EURO_BUTTON = ('xpath', '//a[@class="dropdown-item" and contains(text(), "Euro")]')
    CURRENCY_Sterling_BUTTON = ('xpath', '//a[@class="dropdown-item" and contains(text(), "Sterling")]')
    CURRENCY_Dollar_BUTTON = ('xpath', '//a[@class="dropdown-item" and contains(text(), "Dollar")]')
    CURRENCY_STRONG = ('xpath', '//strong')

    def open_browser(self, url):
        with allure.step('Переход на главную страницу Opencart'):
            self.browser.get(url)

    def get_text(self, selector):
        with allure.step('Поиск веб элемента и получение текстовой ноды'):
            return self.find_element(selector).text
