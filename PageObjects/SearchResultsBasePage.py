from googleSearchProject.PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchResultsBasePage(BasePage):

    """This class cointains commons elements and methods for all Search Results Pages for different modes"""

    """Locators elements in Search Results Base Page"""

    # Search Section
    google_results_logo = (By.ID, "logo")
    search_box_input = (By.XPATH, "//input[@aria-label='Search']")
    search_by_voice_btn = (By.XPATH, "//div[@aria-label='Search by voice']")
    search_btn = (By.XPATH, "//button[@aria-label='Google Search']")
    search_mode_btn = "//div[@id='top_nav']//a[text()=\"{0}\"]"
    more_btn = (By.XPATH, "//div[@id='top_nav']//div[text()='More']")
    more_options_btn = "//g-menu-item//a[text()=\"{0}\"]"
    settings_btn = (By.ID, "abar_button_opt")
    settings_options_btn = "//g-menu-item//span[text()=\"{0}\"]"
    tools_btn = (By.ID, "hdtb-tls")

    # Search Results section
    results_status = (By.ID, "result-stats")
    noresults_msg = (By.XPATH, "//div[@id='res']//p[contains(text(),\"Suggestions:\")]")

    """Actions in Search Results Base Page"""

    def __init__(self, driver):
        super().__init__(driver)

    def switch_search_mode(self, mode):
        mode_btn = self.search_mode_btn.format(mode)
        self.click_btn((By.XPATH, mode_btn))

    def select_more_option(self, option):
        self.click_btn(self.more_btn)
        option_btn = self.more_options_btn.format(option)
        self.click_btn((By.XPATH, option_btn))

    def select_settings_option(self, option):
        self.click_btn(self.settings_btn)
        option_btn = self.settings_options_btn.format(option)
        self.click_btn((By.XPATH, option_btn))

    def check_title_page(self, text):
        get_title = self.driver.instance.title
        return get_title == text

    def check_results_found(self):
        return self.is_element_visible(self.results_status)

    def check_no_results_found(self):
        return self.is_element_visible(self.noresults_msg)


