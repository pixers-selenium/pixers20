from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.OrderCart import OrderCart


class ProductPage(BasePage):
    BUY_NOW_BUTTON = (By.ID, 'buyProductButton')
    ADD_TO_CART_POPUP = (By.ID, 'modalAddedToCart')
    GO_TO_CART_BUTTON = (By.ID, 'go-to-cart-button')
    WISHLIST_BUTTON = (By.CSS_SELECTOR, '#wishlist-item > a')
    MORE_OPTIONS_ICON = (By.XPATH, '//*[@id="addToCartForm"]/ul/li[2]/a/i')
    EFFECT_DROPDOWN = (By.CSS_SELECTOR, '#configure-more > ul > li:nth-child(1) > div > div > button')
    SEPIA_EFFECT = (By.CSS_SELECTOR, '#configure-more > ul > li:nth-child(1) > div > div > ul > li:nth-child(3) > a')
    GRAYSCALLE_EFFECT = (By.CSS_SELECTOR, "#configure-more > ul > li:nth-child(1) > div > div > ul > li:nth-child(2) > a")
    NONE_EFFECT = (By.CSS_SELECTOR, "#configure-more > ul > li:nth-child(1) > div > div > ul > li:nth-child(1) > a")

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

    def open_more_options(self):
        self.click_on(self.MORE_OPTIONS_ICON)
        return self

    def change_effect(self, effect):
        self.click_on(self.EFFECT_DROPDOWN)

        if effect == "sepia":
            self.click_on(self.SEPIA_EFFECT)
        elif effect == "grayscale":
            self.click_on(self.GRAYSCALLE_EFFECT)
        elif effect == "none":
            self.click_on(self.NONE_EFFECT)
        else:
            print("Choose effect")

        return self


