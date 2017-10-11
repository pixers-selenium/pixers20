from pages.HomePage import HomePage
from pages.HomePage import ProductListing
from tests.BaseTest import BaseTest


def test_example_2(BaseTest):
    product_listing = ProductListing(self.driver)

    test2 = (product_listing.go_to_first_product)