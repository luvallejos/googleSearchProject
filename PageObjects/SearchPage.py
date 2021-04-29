from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from googleSearchProject.PageObjects.BasePage import BasePage


class SearchPage(BasePage):

    """Locators elements in Search Page"""

    # Search box Section
    google_logo = (By.XPATH, "//img[@alt='Google']")
    search_voice_btn = (By.XPATH, "//div[@aria-label='Search by voice']")
    search_input = (By.XPATH, "//input[@title='Search']")
    google_search_btn = (By.XPATH, "(//input[@name='btnK'])[2]")
    lucky_search_btn = (By.NAME, "(//input[@name='btnI'])[2]")
    suggestions_by_input_xpath = "(//ul[@role=\"listbox\"]//li//span[text()=\"{0}\"])[{1}]"
    suggestions_by_order_xpath = "(//ul[@role=\"listbox\"]//li//span)[{0}]"

    """Actions in Search Page"""

    def __init__(self, driver):
        super().__init__(driver)

    def search(self, text):
        self.send_keys(self.search_input, text)
        self.send_keys(self.search_input, Keys.ENTER)

    def check_suggestion_in_list(self, suggestion, position):
        self.send_keys(self.search_input, suggestion)
        suggestion_xpath = self.suggestions_by_input_xpath.format(suggestion, position)
        return self.is_element_visible((By.XPATH, suggestion_xpath))

    def select_suggestion_in_list_by_position(self, suggestion, position):
        self.send_keys(self.search_input, suggestion)
        suggestion_xpath = self.suggestions_by_order_xpath.format(position)
        self.click_btn((By.XPATH, suggestion_xpath))
