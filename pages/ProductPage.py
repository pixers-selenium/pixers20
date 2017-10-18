from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.OrderCart import OrderCart


class ProductPage(BasePage):
    BUY_NOW_BUTTON = (By.ID, 'buyProductButton')
    ADD_TO_CART_POPUP = (By.ID, 'modalAddedToCart')
    GO_TO_CART_BUTTON = (By.ID, 'go-to-cart-button')
    WISHLIST_BUTTON = (By.CSS_SELECTOR, '#wishlist-item > a')
    BUTTON_DIMENSION_UNIT = (By.CSS_SELECTOR, '#addToCartForm > ul > li:nth-child(1) > div > div.col-xs-3.text-right > section > div > div > div > button')
    UNIT_CM = (By.CSS_SELECTOR, '#addToCartForm > ul > li:nth-child(1) > div > div.col-xs-3.text-right > section > div > div > div > ul > li:nth-child(1) > a')
    UNIT_FT = (By.CSS_SELECTOR, '#addToCartForm > ul > li:nth-child(1) > div > div.col-xs-3.text-right > section > div > div > div > ul > li:nth-child(3) > a')
    UNIT_IN = (By.CSS_SELECTOR, '#addToCartForm > ul > li:nth-child(1) > div > div.col-xs-3.text-right > section > div > div > div > ul > li:nth-child(2) > a')

    def open_unit_dropdown(self):
        self.click_on(self.BUTTON_DIMENSION_UNIT)
        return self

    def choose_unit(self, unit):
        if unit == "CM":
            self.click_on(self.UNIT_CM)
        elif unit == "FT":
            self.click_on(self.UNIT_FT)
        elif unit == "IN":
            self.click_on(self.UNIT_IN)
        else:
            print("Choose unit.")
        return self

    def is_unit_dropdown_open(self):
        url = 'FT'
        self.wait_for_url_contains(url)
        if url in str(url):
            return True
        else:
            return False

    def buy_product(self):
        self.click_on(self.BUY_NOW_BUTTON)
        self.wait_for_element(self.ADD_TO_CART_POPUP)
        self.click_on(self.GO_TO_CART_BUTTON)
        return OrderCart(self.driver)

    def click_buy_now_button(self):
        self.find_element(self.BUY_NOW_BUTTON).click()
        return self

    def add_to_wishlist(self):
        self.click_on(self.WISHLIST_BUTTON)
        return self
