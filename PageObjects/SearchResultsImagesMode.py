from googleSearchProject.PageObjects.SearchResultsBasePage import SearchResultsBasePage
from selenium.webdriver.common.by import By


class SearchResultsImagesMode(SearchResultsBasePage):

    """Locators elements in Search Results Page Images Mode"""

    # Search Section
    search_mode_btn = "//a[@data-navigation='server' and text()=\"{0}\"]"

    # Search Results section
    image_content = (By.XPATH, "//div[@id='islmp']")
    results_images_found = (By.TAG_NAME, "scrolling-carousel")
    no_results_images_found = (By.XPATH, "//div[@id='islmp']//p[contains(text(),\"Suggestions:\")]")

    """Actions in Search Results Page Images Mode"""

    def __init__(self, driver):
        super().__init__(driver)

    def check_results_images_mode_page_displayed(self):
        return self.is_element_visible(self.image_content)

    def switch_search_mode(self, mode):
        mode_btn = self.search_mode_btn.format(mode)
        self.click_btn((By.XPATH, mode_btn))

    def check_results_found(self):
        return self.is_element_visible(self.results_images_found)

    def check_no_results_found(self):
        return self.is_element_visible(self.no_results_images_found)
