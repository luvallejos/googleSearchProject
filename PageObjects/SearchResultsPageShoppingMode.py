from googleSearchProject.PageObjects.SearchResultsBasePage import SearchResultsBasePage
from selenium.webdriver.common.by import By


class SearchResultsShoppingMode(SearchResultsBasePage):

    """Locators elements in Search Results Page Shopping Mode"""

    # Search Section
    search_shopping_mode_selected_btn = (By.XPATH, "//div[@id='top_nav']//div[@aria-current='page' and text()='Shopping']")

    # Search Results section

    """Actions in Search Results Page Shopping Mode"""

    def __init__(self, driver):
        super().__init__(driver)

    def check_results_shopping_mode_page_displayed(self):
        return self.is_element_visible(self.search_shopping_mode_selected_btn)