from googleSearchProject.PageObjects.SearchResultsBasePage import SearchResultsBasePage
from selenium.webdriver.common.by import By


class SearchResultsPageAllMode(SearchResultsBasePage):

    """Locators elements in Search Results Page All Mode"""

    #Header Section
    search_all_mode_selected_btn = (By.XPATH, "//div[@id='top_nav']//div[@aria-current='page' and text()='All']")


    #Search Results section

    search_result_page = (By.ID, "cnt")
    search_results_all_mode = (By.ID, "search")
    results_status = (By.ID, "result-stats")
    noresults_msg = (By.XPATH, "//div[@id='res']//p[contains(text(),\"Suggestions:\")]")
    link_to_results_by_order = "((//div[@id='search']//div[@class='g'])[{0}]//a)[1]"
    title_of_results_by_order = "((//div[@id='search']//div[@class='g'])[{0}]//a)[1]//h3[contains(text(),\"{1}\")]"

    search_mode_xpath = "//div[@id='hdtb-msb']//div[text()=\"{0}\"]"

    """Actions in Search Results Page All Mode"""

    def __init__(self, driver):
        super().__init__(driver)

    def is_results_page_displayed(self):
        self.is_element_visible(self.search_result_page)

    def results_found(self):
        return self.is_element_visible(self.results_status)

    def no_results_found(self):
        return self.is_element_visible(self.noresults_msg)

    def check_title_result_by_order(self, order, title):
        result_title_xpath = self.title_of_results_by_order.format(order, title)
        return self.is_element_visible((By.XPATH, result_title_xpath))

    def select_result_by_order(self, order):
        result_link_xpath = self.link_to_results_by_order.format(order)
        self.click_btn((By.XPATH, result_link_xpath))









