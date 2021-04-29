from googleSearchProject.PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchResultsBasePage(BasePage):

    """This class cointains commons elements and methods for all Search Results Pages for different modes"""

    """Locators elements in Search Results Base Page"""

    #Header Section
    google_results_logo = (By.ID, "logo")
    search_box_input = (By.XPATH, "//input[@aria-label='Search']")
    search_by_voice_btn = (By.XPATH, "//div[@aria-label='Search by voice']")
    search_btn = (By.XPATH, "//button[@aria-label='Google Search']")
    search_mode_btn = "//div[@id='top_nav']//a[text()=\"{0}\"]"
    more_btn = (By.XPATH, "//div[@id='top_nav']//div[text()='More']")
    settings_btn = (By.ID, "abar_button_opt")
    tools_btn = (By.ID, "hdtb-tls")


    """Actions in Search Results Base Page"""

    def __init__(self, driver):
        super().__init__(driver)

    def check_title_page(self, text):
        get_title = self.driver.instance.title
        return get_title == text


