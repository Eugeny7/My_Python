class MainPage:
    DROPDOWN_MY_ACCAUNT = ('xpath', '//a[@class="dropdown-toggle" and @href!="#"]')
    DROPDOWN_CURRENCY = ('xpath', '//a[@class="dropdown-toggle" and @href="#"]')
    INPUT_SEARCH = ('xpath', '//input[@name="search"]')
    BUTTON_SHOP = ('xpath', '//button[@type="button" and @data-bs-toggle="dropdown"]')
    BUTTON_CHECKOUT = ('xpath', '//span[@class="d-none d-md-inline" and text()="Checkout"]')


class AdminPage:
    INPUT_USERNAME = ('xpath', '//input[@id="input-username"]')
    INPUT_PASSWORD = ('xpath', '//input[@id="input-password"]')
    BUTTON_SUBMIT = ('xpath', '//button[@type="submit"]')
    LINK_OPENCART = ('xpath', '//a[text()="OpenCart"]')
    HEADER_FORM = ('xpath', '//a[text()="OpenCart"]')


class RegistrationPage:

    INPUT_FIRST_NAME = ('xpath', '//input[@id="input-firstname"]')
    INPUT_LAST_NAME = ('xpath', '//input[@id="input-lastname"]' )
    INPUT_EMAIL = ('xpath', '//input[@id="input-email"]' )
    INPUT_PASSWORD = ('xpath', '//input[@id="input-password"]' )
    BUTTON_CONTINUE = ('xpath', '//button[@type="submit" and text()="Continue"]' )

# Other

ITEM_CART = ('xpath', '//button[@type="button" and @data-bs-toggle ="dropdown"]')
# wait.until(EC.visibility_of_element_located(ITEM_CART)).text
