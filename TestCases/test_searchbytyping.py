import time
from googleSearchProject.Config.webdriver import Driver
from googleSearchProject.Config.config import Config
from googleSearchProject.PageObjects.SearchPage import SearchPage
from googleSearchProject.PageObjects.SearchResultsPage import SearchResultsPage


class TestSearchByTyping:

    def setup(self):
        self.driver = Driver()
        self.driver.navigate(Config.BASE_URL)

    def test_searching_valid_input(self):
        searchpage = SearchPage(self.driver)
        searchpage.search("The name of the wind")
        resultspage = SearchResultsPage(self.driver)
        assert [resultspage.results_found(), "No results found"]

    def test_searching_invalid_input(self):
        searchpage = SearchPage(self.driver)
        searchpage.search("---------------------------")
        resultspage = SearchResultsPage(self.driver)
        assert [resultspage.no_results_found(), "Results found for the searching"]
        time.sleep(6)

    def test_select_first_result(self):
        searchpage = SearchPage(self.driver)
        searchpage.search("The name of the wind")
        resultspage = SearchResultsPage(self.driver)
        resultspage.select_result_by_order(1)

    def test_first_suggestion(self):
        searchpage = SearchPage(self.driver)
        searchpage.check_suggestion_in_list("the name of the wind", 1)

    def teardown(self):
        self.driver.instance.quit()
