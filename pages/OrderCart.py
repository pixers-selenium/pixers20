from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.OrderPlace import OrderPlace


class OrderCart(BasePage):

    CHECKOUT_BUTTON = (By.XPATH, '//a[@aria-label="submit-button"]')
    PAYPALL_CHECKOUT = (By.CSS_SELECTOR, '#pay-pal-express-btn > a')

    def go_to_order_place(self):
        self.click_on(self.CHECKOUT_BUTTON)
        return OrderPlace(self.driver)

    def click_on_paypall_button(self):
        self.click_on(self.PAYPALL_CHECKOUT)
        return self







