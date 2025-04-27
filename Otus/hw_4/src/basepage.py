from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self,selector):
        wait = WebDriverWait(self.browser, 5)
        return wait.until(EC.visibility_of_element_located(selector))

    def get_attribute(self, selector):
        return self.find_element(selector).get_attribute('value')

    def click_element(self, item):
        actions = ActionChains(self.browser)
        actions.pause(0.3).move_to_element(item).click().perform()
