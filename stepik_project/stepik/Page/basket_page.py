from stepik_project.stepik.Page.base_page import BasePage
from stepik_project.stepik.locators import BasketPageLocators

class BasketPage(BasePage):
    
    def give_text_basket_is_empty(self):
        text = self.get_element(BasketPageLocators.CONTENT_INNER).text
        return text

    def should_be_basket_is_empty(self):
        TEXT = 'Ваша корзина пуста'
        assert TEXT in self.give_text_basket_is_empty(), 'Basket is not empty'

    def is_not_element_in_basket(self):
        assert self.is_not_element_present(BasketPageLocators.BTN_CHECKOUT), \
            f'Basket is not empty, because element {BasketPageLocators.BTN_CHECKOUT} find'