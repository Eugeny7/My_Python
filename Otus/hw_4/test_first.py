import time

import pytest


@pytest.mark.smoke
def test_first(browser, url):
    browser.get(url)
    time.sleep(5)
