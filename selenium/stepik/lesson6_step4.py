from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# LINK = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(LINK)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, 'country')
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     button.click()
#     browser.find_element(By.)
#
# finally:
#     time.sleep(5)
#     browser.quit()

# URL = 'https://suninjuly.github.io/find_link_text'
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     element = str(math.ceil(math.pow(math.pi, math.e)*10000))
#     browser.find_element(By.LINK_TEXT, f'{element}').click()
#     browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
#     browser.find_element(By.NAME, "last_name").send_keys("Petrov")
#     browser.find_element(By.CLASS_NAME, 'form-control.city').send_keys("Smolensk")
#     browser.find_element(By.ID, 'country').send_keys("Russia")
#     browser.find_element(By.CSS_SELECTOR, "button.btn").click()
# finally:
#     time.sleep(20)
#     browser.quit()

# URL = "http://suninjuly.github.io/huge_form.html"
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     elements = browser.find_elements(By.TAG_NAME, 'input')
#     for element in elements:
#         element.send_keys('Test')
#
#     browser.find_element(By.CSS_SELECTOR, '.btn').click()
# finally:
#     time.sleep(5)
#     browser.quit()

# URL = 'https://suninjuly.github.io/registration2.html'
# TEXT = 'Congratulations! You have successfully registered!'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     elements = browser.find_elements(By.CSS_SELECTOR, '[required]')
#     for element in elements:
#         element.send_keys('Test')
#     browser.find_element(By.CSS_SELECTOR, '.btn').click()
#     time.sleep(2)
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1").text
#     assert welcome_text_elt == TEXT
# finally:
#     browser.quit()

URL = 'http://suninjuly.github.io/registration1.html'
TEXT = 'Congratulations! You have successfully registered!'

try:
    browser = webdriver.Chrome()
    browser.get(URL)
    elements = browser.find_elements(By.CSS_SELECTOR, '[required]')
    for element in elements:
        element.send_keys('Test')
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    time.sleep(2)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text_elt == TEXT
finally:
    browser.quit()

# URL = 'https://suninjuly.github.io/math.html'
#
# try:
#     browser= webdriver.Chrome()
#     browser.get(URL)
#     def calc(x_element):
#         return str(math.log(abs(12 * math.sin(int(x_element)))))
#     x_element = browser.find_element(By.ID, 'input_value').text
#     y = calc(x_element)
#     browser.find_element(By.ID, 'answer').send_keys(y)
#     browser.find_element(By.CSS_SELECTOR, '[for=robotCheckbox]').click()
#     browser.find_element(By.CSS_SELECTOR, '[for=robotsRule]').click()
#     browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
# finally:
#     time.sleep(5)
#     browser.quit()


# URL = 'https://suninjuly.github.io/get_attribute.html'
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     element_x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
#     y = calc(element_x)
#     browser.find_element(By.ID, 'answer').send_keys(y)
#     browser.find_element(By.ID, 'robotCheckbox').click()
#     browser.find_element(By.ID, 'robotsRule').click()
#     browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
# finally:
#     time.sleep(5)
#     browser.quit()


# URl = 'https://suninjuly.github.io/selects1.html'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URl)
#     num_1 = int(browser.find_element(By.ID, 'num1').text)
#     num_2 = int(browser.find_element(By.ID, 'num2').text)
#     sum_num = str(num_1 + num_2)
#     select = Select(browser.find_element(By.ID, 'dropdown'))
#     select.select_by_value(sum_num)
#     browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
# finally:
#     time.sleep(5)
#     browser.quit()

# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get(URl)
# browser.execute_script("alert('Robots at work');")
# time.sleep(5)

# URL = 'http://suninjuly.github.io/execute_script.html'
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     el_x = int(browser.find_element(By.ID, 'input_value').text)
#     y = calc(el_x)
#     browser.execute_script("window.scrollBy(0, 100);")
#     field = browser.find_element(By.ID, 'answer')
#     field.click()
#     field.send_keys(y)
#     browser.find_element(By.CSS_SELECTOR, '[for=robotCheckbox]').click()
#     browser.find_element(By.CSS_SELECTOR, '[for=robotsRule]').click()
#     browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
# finally:
#     time.sleep(10)
#     browser.quit()


# URL = 'http://suninjuly.github.io/file_input.html'
#
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
#
# browser = webdriver.Chrome()
# browser.get(URL)
# browser.find_element(By.NAME, 'firstname').send_keys('Eugeny')
# browser.find_element(By.NAME, 'lastname').send_keys('Puchkov')
# browser.find_element(By.NAME, 'email').send_keys('test@yandex.ru')
# browser.find_element(By.CSS_SELECTOR, '[type=file]').send_keys(file_path)
# browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
# time.sleep(7)

# URL = 'http://suninjuly.github.io/alert_accept.html'
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
#     browser.switch_to.alert.accept()
#     element_x = browser.find_element(By.ID, 'input_value').text
#     element_y = calc(element_x)
#     browser.find_element(By.ID, 'answer').send_keys(element_y)
#     browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
# finally:
#     time.sleep(8)
#     browser.quit()

# URL = 'https://suninjuly.github.io/redirect_accept.html'
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     browser.find_element(By.CSS_SELECTOR, '[type = submit]').click()
#     browser.switch_to.window(browser.window_handles[1])
#     element_x = browser.find_element(By.ID, 'input_value').text
#     element_y = calc(element_x)
#     browser.find_element(By.ID, 'answer').send_keys(element_y)
#     browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
# finally:
#     time.sleep(8)
#     browser.quit()

# URL = 'http://suninjuly.github.io/explicit_wait2.html'
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(URL)
#     wait = WebDriverWait(browser, 14)
#     wait.until(EC.text_to_be_present_in_element((By.ID,'price'), '$100'))
#     browser.find_element(By.ID, 'book').click()
#     element_x = browser.find_element(By.ID, 'input_value').text
#     element_y = calc(element_x)
#     browser.find_element(By.ID, 'answer').send_keys(element_y)
#     browser.find_element(By.ID, 'solve').click()
# finally:
#     time.sleep(8)
#     browser.quit()