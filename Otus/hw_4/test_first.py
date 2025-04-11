import pytest
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
