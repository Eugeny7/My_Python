from appium.webdriver.common.appiumby import AppiumBy

def test_gmail(driver):
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.google.android.gm:id/welcome_tour_got_it"]')
    element.click()