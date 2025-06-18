import time
import math
from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or safari")
    parser.addoption('--language', action ='store', default='es')

@pytest.fixture
def browser_name(request):
    return request.config.getoption('browser_name')
@pytest.fixture
def browser_language(request):
    return request.config.getoption('language')

@pytest.fixture(scope="function")
def browser(browser_name, browser_language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    if browser_name == 'chrome':
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif browser_name == 'safari':
        browser = webdriver.Safari(options=options)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or safari")
    yield browser
    browser.quit()



@pytest.fixture(scope='function')
def math_result():
    answer = math.log(int(time.time()))
    return answer