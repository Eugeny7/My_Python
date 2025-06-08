from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options_browser = webdriver.ChromeOptions()
options_browser.add_argument('--window_size=1920,1080')
browser = webdriver.Chrome()
url = 'https://stage.srf.rest/auth/sign-in'

def registration ():
    browser.get(url)
    reg_button = browser.find_element(By.XPATH, '//p-button[@type="button" and @class = "p-element"]')
    reg_button.click()
    time.sleep(2)

