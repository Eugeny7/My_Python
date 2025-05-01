import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, selector):
        with allure.step('Поиск веб элемента'):
            try:
                wait = WebDriverWait(self.browser, 5)
                return wait.until(ec.visibility_of_element_located(selector))
            except TimeoutException:
                allure.attach(
                    name=f'Страница поиска веб элемента {selector}',
                    body=self.browser.get_screenshot_as_png(),
                    attachment_type=allure.attachment_type.PNG
                )

                raise AssertionError(f'Элемент{selector}не найден')

    def get_attribute(self, selector):
        with allure.step('Поиск веб элемента и получение атрибута'):
            return self.find_element(selector).get_attribute('value')

    def click_element(self, item):
        with allure.step('Клик по веб элементу'):
            actions = ActionChains(self.browser)
            actions.pause(0.3).move_to_element(item).click().perform()
