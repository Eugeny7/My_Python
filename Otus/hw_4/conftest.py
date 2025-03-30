from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', action='store', default='http://192.168.0.104:8081')


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
