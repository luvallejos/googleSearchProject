from googleSearchProject.PageObjects.SearchResultsBasePage import SearchResultsBasePage
from selenium.webdriver.common.by import By


class SearchResultsNewsMode(SearchResultsBasePage):

    """Locators elements in Search Results Page News Mode"""

    # Header Section
    search_news_mode_selected_btn = (By.XPATH, "//div[@id='top_nav']//div[@aria-current='page' and text()='News']")

    # Search Results section

    """Actions in Search Results Page News Mode"""

    def __init__(self, driver):
        super().__init__(driver)

    def is_results_news_mode_page_displayed(self):
        self.is_element_visible(self.search_news_mode_selected_btn)
