from googleSearchProject.PageObjects.SearchResultsBasePage import SearchResultsBasePage
from selenium.webdriver.common.by import By


class SearchResultsBooksMode(SearchResultsBasePage):

    """Locators elements in Search Results Page Books Mode"""

    # Header Section
    search_books_mode_selected_btn = (By.XPATH, "//div[@id='top_nav']//div[@aria-current='page' and text()='Books']")

    # Search Results section

    """Actions in Search Results Page Books Mode"""

    def __init__(self, driver):
        super().__init__(driver)

    def is_results_books_mode_page_displayed(self):
        self.is_element_visible(self.search_books_mode_selected_btn)