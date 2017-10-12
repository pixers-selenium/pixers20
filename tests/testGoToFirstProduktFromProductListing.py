from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class testGoToFirstProduktFromProductListing(BaseTest):

    def test_example_2(self):
        homepage = HomePage(self.driver)
        query = "kot"

        test = (homepage.search_query(query)
                        .go_to_first_product())