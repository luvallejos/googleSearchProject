from googleSearchProject.Config.webdriver import Driver
from googleSearchProject.Config.config import Config
from googleSearchProject.PageObjects.SearchPage import SearchPage
from googleSearchProject.PageObjects.SearchResultsPageAllMode import SearchResultsPageAllMode


class TestSearchBySuggestion:

    def setup(self):
        self.driver = Driver()
        self.driver.navigate(Config.BASE_URL)

    def test_searching_by_selecting_suggestion(self):
        search_page = SearchPage(self.driver)
        search_page.select_suggestion_in_list("The Name of the Wind", 1)
        results_page = SearchResultsPageAllMode(self.driver)
        assert results_page.check_title_result_by_order(1, "The Name of the Wind")
        results_page.select_result_by_order(1)
        assert results_page.check_title_page("The Name of the Wind - Wikipedia")

    def teardown(self):
        self.driver.instance.quit()
