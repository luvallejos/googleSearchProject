import time
from googleSearchProject.Config.webdriver import Driver
from googleSearchProject.Config.config import Config
from googleSearchProject.PageObjects.SearchPage import SearchPage
from googleSearchProject.PageObjects.SearchResultsPageAllMode import SearchResultsPageAllMode


class TestSearchByTyping:

    def setup(self):
        self.driver = Driver()
        self.driver.navigate(Config.BASE_URL)

    def test_searching_valid_input(self):
        searchpage = SearchPage(self.driver)
        searchpage.search("The name of the wind")
        #resultspage = SearchResultsPageAllMode(self.driver)
        #resultspage.check_title_result_by_order(1, "The Name of the Wind")
        #resultspage.select_result_by_order(1)
        #assert resultspage.check_title_selected_result_page("The Name of the Wind - Wikipedia")

    def teardown(self):
        self.driver.instance.quit()
