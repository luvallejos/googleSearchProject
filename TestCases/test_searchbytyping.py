from googleSearchProject.Config.webdriver import Driver
from googleSearchProject.Config.config import Config
from googleSearchProject.PageObjects.SearchPage import SearchPage
from googleSearchProject.PageObjects.SearchResultsPageAllMode import SearchResultsPageAllMode


class TestSearchByTyping:

    def setup(self):
        self.driver = Driver()
        self.driver.navigate(Config.BASE_URL)

    def test_searching_valid_input(self):
        search_page = SearchPage(self.driver)
        search_page.search("The name of the wind")
        results_page = SearchResultsPageAllMode(self.driver)
        assert results_page.check_title_result_by_order(1, "The Name of the Wind")
        results_page.select_result_by_order(1)
        assert results_page.check_title_page("The Name of the Wind - Wikipedia")

    def test_searching_invalid_input(self):
        search_page = SearchPage(self.driver)
        search_page.search("---------------------------")
        results_page = SearchResultsPageAllMode(self.driver)
        assert results_page.check_no_results_found()

    def teardown(self):
        self.driver.instance.quit()
