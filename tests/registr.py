from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
options_browser = webdriver.ChromeOptions()
options_browser.add_argument('--window_size=1920,1080')

url = 'https://stage.srf.rest/auth/sign-in'
browser.get(url)

def registration ():

# Поиск селектора и клик по кнопке "Зарегистрироваться"
      reg_button = browser.find_element(By.XPATH, '//p-button[@type="button" and @class = "p-element"]')
      reg_button.click()
      time.sleep(2)
# Выбор селектора из списка
#     brows.find_elements(By.CLASS_NAME, 'p-button-label')[2].click()
# Ввод имени
      name_field = browser.find_element(By.XPATH, '//input[@id="firstName"]')
      name_field.click()
      name_field.send_keys('Eugeny')
#  Ввод Фамилии
      surname_field = browser.find_element(By.XPATH, '//input[@id="surname"]')
      surname_field.click()
      surname_field.send_keys('Puchkov')
# Выбор должности из селектора
      job_title = browser.find_element(By.XPATH, '//span[@id="pn_id_3_label"]')
      job_title.click()
      role = browser.find_element(By.XPATH, '//li[@id="p-highlighted-option"]')
# Получить атрибут локатора и кликнуть по нему
      print(role.get_attribute('id'))
      role.click()
      time.sleep(2)
registration ()