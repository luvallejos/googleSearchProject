from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    """This class contains all the methods commons for all the pages"""

    def __init__(self, driver):
        self.driver = driver

    def click_btn(self, by_locator):
        WebDriverWait(self.driver.instance, 3).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, input_text):
        WebDriverWait(self.driver.instance, 3).until(EC.visibility_of_element_located(by_locator)).send_keys(input_text)

    def is_element_visible(self, by_locator):
        element = WebDriverWait(self.driver.instance, 3).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
