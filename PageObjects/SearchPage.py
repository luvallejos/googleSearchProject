from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from googleSearchProject.PageObjects.BasePage import BasePage


class SearchPage(BasePage):

    """Locators elements in Search Page"""

    google_logo = (By.XPATH, "//img[@alt='Google']")
    search_voice_btn = (By.XPATH, "//div[@aria-label='Search by voice']")
    search_input = (By.XPATH, "//input[@title='Search']")
    google_search_btn = (By.XPATH, "(//input[@name='btnK'])[2]")
    lucky_search_btn = (By.NAME, "(//input[@name='btnI'])[2]")
    suggestionsbyinput_xpath = "(//ul[@role=\"listbox\"]//li//span[text()=\"{0}\"])[{1}]"

    """Actions in Search Page"""

    def __init__(self, driver):
        super().__init__(driver)

    def search(self, text):
        self.send_keys(self.search_input, text)
        self.send_keys(self.search_input, Keys.ENTER)

    def check_suggestion_in_list(self, suggestion, position):
        self.send_keys(self.search_input, suggestion)
        suggestion_xpath = self.suggestionsbyinput_xpath.format(suggestion, position)
        return self.is_element_visible((By.XPATH, suggestion_xpath))

    def select_suggestion_in_list(self, suggestion, position):
        self.send_keys(self.search_input, suggestion)
        suggestion_xpath = self.suggestionsbyinput_xpath.format(suggestion, position)
        self.click_btn((By.XPATH, suggestion_xpath))
