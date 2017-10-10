from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class testExample(BaseTest):

    def test_example(self):
        homepage = HomePage(self.driver)

        test = (homepage.search_query())