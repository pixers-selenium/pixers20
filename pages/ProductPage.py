from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class ProductPage(BasePage):
    BUY_NOW_BUTTON = (By.ID, 'buyProductButton')
    ADD_TO_CART_POPUP = (By.ID, 'modalAddedToCart')
    GO_TO_CART_BUTTON = (By.ID, 'go-to-cart-button')
    WISHLIST_BUTTON = (By.CSS_SELECTOR, '#wishlist-item > a')

    def buy_product(self):
        self.click_on(self.BUY_NOW_BUTTON)
        self.wait_for_element(self.ADD_TO_CART_POPUP, self.TIMEOUT)
        self.click_on(self.GO_TO_CART_BUTTON)

        return self

    def add_to_wishlist(self):
        self.click_on(self.WISHLIST_BUTTON)

        return self
