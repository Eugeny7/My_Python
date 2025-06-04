from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    TEXT = 'login'

class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary')
    ALERT_MESSAGE_ADD_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')
    TITLE_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main > :nth-child(1)')
    TITLE_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    ALERT_COAST_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(3)')
    PRICE_BOOK = (By.CSS_SELECTOR, 'p.price_color')
    PRICE_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, '.alertinner p strong')