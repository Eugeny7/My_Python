class MainPage:
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


class AdminPage:
    OPENCART_LOGIN = 'user'
    OPENCART_PASSWORD = 'bitnami'
    DEFAULT_EMAIL_USER = 'user@example.com'

    INPUT_USERNAME = ('xpath', '//input[@id="input-username"]')
    INPUT_PASSWORD = ('xpath', '//input[@id="input-password"]')
    BUTTON_SUBMIT = ('xpath', '//button[@type="submit"]')
    LINK_OPENCART = ('xpath', '//a[text()="OpenCart"]')
    HEADER_FORM = ('xpath', '//a[text()="OpenCart"]')
    DROPDOWN_MENU = ('xpath', '//span[@class="d-none d-md-inline d-lg-inline"]')
    PROFILE_BUTTON = ('xpath', '//a[@class="dropdown-item" and contains(@href, "user_token")]')
    INPUT_EMAIL = ('xpath', '//input[@id="input-email"]')


class RegistrationPage:
    INPUT_FIRST_NAME = ('xpath', '//input[@id="input-firstname"]')
    INPUT_LAST_NAME = ('xpath', '//input[@id="input-lastname"]')
    INPUT_EMAIL = ('xpath', '//input[@id="input-email"]')
    INPUT_PASSWORD = ('xpath', '//input[@id="input-password"]')
    BUTTON_CONTINUE = ('xpath', '//button[@type="submit" and text()="Continue"]')
