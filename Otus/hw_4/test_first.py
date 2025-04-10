import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Otus.hw_4.locators import *

@pytest.mark.smoke
def test_main_page(browser, url):
    wait = WebDriverWait(browser, 5)
    browser.get(url)
    wait.until(EC.visibility_of_element_located(DROPDOWN_MY_ACCAUNT)).click()
    wait.until(EC.visibility_of_element_located(DROPDOWN_CURRENCY)).click()
    wait.until(EC.visibility_of_element_located(INPUT_SEARCH)).click()
    wait.until(EC.visibility_of_element_located(BUTTON_SHOP)).click()
    wait.until(EC.visibility_of_element_located(BUTTON_CHECKOUT)).click()

def test_admin_page(browser, url):
    wait = WebDriverWait(browser, 3)
    browser.get(f'{url}/administration')
    wait.until(EC.visibility_of_element_located(HEADER_FORM))
    wait.until(EC.visibility_of_element_located(INPUT_USERNAME)).click()
    wait.until(EC.visibility_of_element_located(INPUT_PASSWORD)).click()
    wait.until(EC.visibility_of_element_located(BUTTON_SUBMIT)).click()
    wait.until(EC.visibility_of_element_located(LINK_OPENCART)).click()
    browser.back()