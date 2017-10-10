from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class testExample(BaseTest):

    def test_example(self):
        homepage = HomePage(self.driver)
        query = "kot"

        test = (homepage.search_query(query)
                        .get_page_title())

        self.assertIn(query, test)