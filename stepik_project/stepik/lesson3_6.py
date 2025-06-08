from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

email = ''
password = ''


@pytest.mark.parametrize('url',
                         ['https://stepik.org/lesson/236895/step/1',
                          'https://stepik.org/lesson/236896/step/1',
                          'https://stepik.org/lesson/236897/step/1',
                          'https://stepik.org/lesson/236898/step/1',
                          'https://stepik.org/lesson/236899/step/1',
                          'https://stepik.org/lesson/236903/step/1',
                          'https://stepik.org/lesson/236904/step/1',
                          'https://stepik.org/lesson/236905/step/1'
                          ])
def test_stepik_input(url, browser, math_result):
    wait = WebDriverWait(browser, 10)
    browser.get(url)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.woof-message [type=button]'))).click()
    browser.find_element(By.CSS_SELECTOR, '.ember-view.navbar__auth.navbar__auth_login').click()
    browser.find_element(By.ID, 'id_login_email').send_keys(email)
    browser.find_element(By.ID, 'id_login_password').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn').click()
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.light-tabs.ember-view')))
    input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ember-text-area.ember-view')))
    input_field.clear()
    input_field.send_keys(math_result)
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    actual_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text
    expected_text = 'Correct!'
    assert actual_text == expected_text, f'Фактический результат: {actual_text} НЕ равен ожидаемому:{expected_text}'
