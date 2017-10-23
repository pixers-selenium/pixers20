from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class testGoToFirstProduktFromProductListing(BaseTest):

    def test_example_2(self):
        homepage = HomePage(self.driver)
        query = "kot"

        test = (homepage.search_query(query)
                        .go_to_first_product())

    def test_dotpay_offline_checkout(self):
        homePage = HomePage(self.driver)
        query = "kot"
        text = 'test'
        email = "qa@pixers.pl"
        postal = "11-111"
        payment_type = "offline"
        expected_url = "dotpay"

        test = (homePage.search_query(query)
                        .click_newsletter_close()
                        .go_to_product()
                        .buy_product()
                        .go_to_order_place()
                        .fill_address_form(text)
                        .fill_email(email)
                        .fill_postal(postal)
                        .choose_payment(payment_type)
                        .click_pay_button()
                        .is_url_contains(expected_url))

        self.assertTrue(test)

    def test_change_product_color_to_sepia(self):
        homePage = HomePage(self.driver)
        query = "kot"
        expec = "=sepia"
        effect = "sepia"

        test = (homePage.search_query(query)
                        .click_newsletter_close()
                        .go_to_product()
                        .open_more_options()
                        .change_effect(effect)
                        .is_url_contains(expec))

        self.assertTrue(test)

    def add_product_to_wishlist(self):
        homePage = HomePage(self.driver)
        query = "kot"

        test = (homePage.search_query(query)
                        .click_newsletter_close()
                        .go_to_product()
                        .add_to_wishlist())

        self.assertTrue(test)


