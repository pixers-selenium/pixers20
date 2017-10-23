from pages.HomePage import HomePage
from pages.HomePage import ProductListing
from tests.BaseTest import BaseTest


class testExample(BaseTest):

    def test_example(self):
        homepage = HomePage(self.driver)
        query = "kot"

        test = (homepage.search_query(query)
                        .get_page_title())

        self.assertIn(query, test)

    def test_dotpay_checkout(self):
        homePage = HomePage(self.driver)
        query = "kot"
        text = 'test'
        email = "qa@pixers.pl"
        postal = "11-111"
        payment_type = "dotpay"

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
                        .is_url_contains(payment_type))

        self.assertTrue(test)

    def test_paypal_checkout(self):
        homePage = HomePage(self.driver)
        query = "kot"
        text = 'test'
        email = "qa@pixers.pl"
        postal = "11-111"
        payment_type = "paypal"

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
                        .is_url_contains(payment_type))

        self.assertTrue(test)



