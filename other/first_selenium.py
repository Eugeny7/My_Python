from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://stage.srf.rest/auth/sign-in")

def test_url():
# Тест URL
    url = browser.current_url
    assert url == "https://stage.srf.rest/auth/sign-in", "Ошибка, URL не соответствует указанному"
    print(f"URL страницы {url}")

def test_title():
# Тест заголовка
    title = browser.title
    print(f'Текущий заголовок: {title}')
    test_title = 'GourmetricaUi'
    assert title == test_title, f'Заголовок не соответствует указанному, а именно: {test_title}'
    time.sleep(2)