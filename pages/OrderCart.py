from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class OrderCart(BasePage):
    GO_TO_BOX = (By.ID, 'go-to-cart-button')
    PAYPALL_CHECKOUT = (By.CSS_SELECTOR, '#pay-pal-express-btn > a') #class name czy css selector, skąd mam to wiedzieć ?

    def go_to_bascet(self): # czy w tym locatorze trzeba coś wpisać ?
        self.click_on(self.GO_TO_BOX)

    def Paypall_button(self)
        self.click_on(self.PAYPALL_CHECKOUT)







