from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from stepik_project.stepik.locators import BasePageLocators
import math

class BasePage:
    def __init__(self, browser: WebDriver, url):
        self.browser = browser
        self.url = url

    def is_not_element_present(self, locator, timeout=4):
        try:
            wait = WebDriverWait(self.browser, timeout)
            wait.until(ec.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            wait = WebDriverWait(self.browser, timeout, 1)
            wait.until_not(ec.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def get_element(self, locator: tuple) -> WebElement:
        try:
            element = self.browser.find_element(*locator)
        except NoSuchElementException:
            raise AssertionError(f'The element {locator}is not found')
        return element

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        self.get_element(BasePageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        self.get_element(BasePageLocators.BASKET_LINK).click()

    def go_to_product_list_page(self):
        self.get_element(BasePageLocators.DROPDOWN_LIST).click()
        self.get_element(BasePageLocators.SELECT_ALL_ITEMS).click()

