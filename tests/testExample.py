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

    def test_dotpay_checkout(self): #tu ma byc tak jak nazwa tego testu ?
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
                        .is_url_contains(payment_type))#czy tu coś zmieniać ?

        self.assertTrue(test)

    def test_product_dimensions_unit_change(self):
        homePage = HomePage(self.driver)
        query = "kot"
        expected = "_unit=FT"

        test = (homePage.search_query(query)
                .click_newsletter_close()
                .go_to_product(4)
                .open_unit_dropdown()
                .choose_unit("FT")
                .is_url_contains(expected)
                )
        self.assertTrue(test)

    def test_show_more_items(self):
         homePage = HomePage(self.driver)
         query = "kot"

         test = (homePage.search_query(query)
                 .click_newsletter_close()
                 .click_show_more_items()
                 .get_product_quantity())

         self.assertEqual(74, test)

    def test_send_message(self):
        homePage = HomePage(self.driver)
        query = "kot"
        name = "test"
        email = "qa@pixers.pl"
        message = 'test, test'
        test = (homePage.search_query(query)
                            .click_newsletter_close()
                            .click_ask_question()
                            .fill_name(name)
                            .fill_data_email(email)
                            .fill_your_message(message)
                            .click_on_send_message()
                            .is_ask_form_send())

        self.assertTrue(test)

