from googleSearchProject.PageObjects.SearchResultsBasePage import SearchResultsBasePage
from selenium.webdriver.common.by import By


class SearchResultsPageAllMode(SearchResultsBasePage):

    """Locators elements in Search Results Page All Mode"""

    # Search Section
    search_all_mode_selected_btn = (By.XPATH, "//div[@id='top_nav']//div[@aria-current='page' and text()='All']")

    # Search Results section
    link_to_results_by_order = "((//div[@id='search']//div[@class='g'])[{0}]//a)[1]"
    title_of_results_by_order = "((//div[@id='search']//div[@class='g'])[{0}]//a)[1]//h3[contains(text(),\"{1}\")]"

    """Actions in Search Results Page All Mode"""

    def __init__(self, driver):
        super().__init__(driver)

    def check_results_all_mode_page_displayed(self):
        return self.is_element_visible(self.search_all_mode_selected_btn)

    def check_title_result_by_order(self, order, title):
        result_title_xpath = self.title_of_results_by_order.format(order, title)
        return self.is_element_visible((By.XPATH, result_title_xpath))

    def select_result_by_order(self, order):
        result_link_xpath = self.link_to_results_by_order.format(order)
        self.click_btn((By.XPATH, result_link_xpath))
