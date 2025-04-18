from selenium import webdriver
import pytest

BASE_URL = 'http://192.168.0.105:8081'


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', action='store', default=BASE_URL)


@pytest.fixture(scope='session')
def browser_name(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def browser(browser_name):
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser_name == 'safari':
        driver = webdriver.Safari()
        driver.maximize_window()
    else:
        raise ValueError(f'{browser_name} not allowed')
    yield driver
    driver.quit()
