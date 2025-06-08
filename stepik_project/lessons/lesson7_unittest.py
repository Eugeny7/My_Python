from selenium.webdriver.common.by import By
from selenium import webdriver

import unittest


class TestAbs(unittest.TestCase):
    def test_registration1(self):
        URL = 'http://suninjuly.github.io/registration1.html'
        TEXT = 'Congratulations! You have successfully registered!'
        self.browser = webdriver.Chrome()
        self.browser.get(URL)
        self.browser.find_element(By.CSS_SELECTOR, '.form-control.first[required]').send_keys('Test')
        self.browser.find_element(By.CSS_SELECTOR, '.form-control.second[required]').send_keys('Test')
        self.browser.find_element(By.CSS_SELECTOR, '.form-control.third[required]').send_keys('Test')
        self.browser.find_element(By.CSS_SELECTOR, '.btn').click()
        self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(self.welcome_text_elt, TEXT, f'{self.welcome_text_elt} НЕ соответствует {TEXT}')
        self.browser.quit()

    def test_registration2(self):
        URL = 'http://suninjuly.github.io/registration2.html'
        TEXT = 'Congratulations! You have successfully registered!'
        self.browser = webdriver.Chrome()
        self.browser.get(URL)
        self.browser.find_element(By.CSS_SELECTOR, '.form-control.first[required]').send_keys('Test')
        self.browser.find_element(By.CSS_SELECTOR, '.form-control.second[required]').send_keys('Test')
        self.browser.find_element(By.CSS_SELECTOR, '.form-control.third[required]').send_keys('Test')
        self.browser.find_element(By.CSS_SELECTOR, '.btn').click()
        self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(self.welcome_text_elt, TEXT, f'{self.welcome_text_elt} НЕ соответствует {TEXT}')
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
