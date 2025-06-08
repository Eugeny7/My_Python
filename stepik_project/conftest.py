import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def math_result():
    answer = math.log(int(time.time()))
    return answer