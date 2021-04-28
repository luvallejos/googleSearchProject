from googleSearchProject.PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):

    """Locators for elements page"""

    search_result_page = (By.ID, "cnt")
    results_status = (By.ID, "result-stats")
    noresults_msg = (By.XPATH, "//div[@id='res']//p[contains(text(),\"Suggestions:\")]")
    search_results_all_mode = (By.ID, "search")
    link_to_results_by_order = "((//div[@id='search']//div[@class='g'])[{0}]//a)[1]"
    search_mode_xpath = "//div[@id='hdtb-msb']//div[text()=\"{0}\"]"

    def __init__(self, driver):
        super().__init__(driver)

    def is_results_page_displayed(self):
        self.is_element_visible(self.search_result_page)

    def results_found(self):
        return self.is_element_visible(self.results_status)

    def no_results_found(self):
        return self.is_element_visible(self.noresults_msg)

    def select_result_by_order(self, order):
        result_link_xpath = self.link_to_results_by_order.format(order)
        self.click_btn((By.XPATH, result_link_xpath))








