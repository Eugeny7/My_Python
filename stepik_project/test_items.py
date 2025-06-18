from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_should_be_basket_btn(browser):
    browser.get(link)
    try:
        element = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    except NoSuchElementException:
        element = None
    assert element is not None, 'Not found element'