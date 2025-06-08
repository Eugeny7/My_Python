
from stepik_project.Page.base_page import BasePage
from stepik_project.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_the_basket(self):
        self.open()
        self.get_element(ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def should_be_message_add_basket(self):
        self.is_element_present(*ProductPageLocators.ALERT_MESSAGE_ADD_BASKET)
        title_book = self.get_element(ProductPageLocators.TITLE_BOOK).text
        title_book_message = self.get_element(ProductPageLocators.TITLE_BOOK_IN_MESSAGE).text
        assert title_book == title_book_message

    def should_be_message_price_book(self):
        self.is_element_present(*ProductPageLocators.ALERT_COAST_BASKET)
        price_book = self.get_element(ProductPageLocators.PRICE_BOOK).text
        price_book_message = self.get_element(ProductPageLocators.PRICE_BOOK_IN_MESSAGE).text
        assert price_book == price_book_message

    def should_not_be_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.ALERT_MESSAGE_ADD_BASKET), \
            "Success message is presented, but should not be"

    def should_not_be_element(self):
        assert self.is_disappeared(ProductPageLocators.ALERT_MESSAGE_ADD_BASKET), \
            f'The element {ProductPageLocators.ALERT_MESSAGE_ADD_BASKET} did not disappear from the page'

    def go_to_product_page(self):
        self.get_element(ProductPageLocators.TITLE_ITEM_LINK).click()
