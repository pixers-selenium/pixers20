from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class OrderPlace(BasePage):

    EMAIL_BOX = (By.ID, 'order_deliveryAddress_email')
    NAME_BOX = (By.ID, 'name')
    COMPANY_NAME_BOX = (By.ID, 'companyName')
    ADDRESS1_BOX = (By.ID, 'address1')
    ADDRESS2_BOX = (By.ID, 'address2')
    POSTAL_CODE_BOX = (By.ID, 'zip')
    CITY_BOX = (By.ID, 'city')
    PHONE_BOX = (By.ID, 'phone')
    DOTPAY_CHECKOUT_RADIO_BUTTON = (By.CSS_SELECTOR, 'body > section > form > div > article > div:nth-child(2) > div > div > div > div:nth-child(1) > div > div.col-md-2.col-sm-2.col-xs-12.payment-title > label')
    CARD_RADIO_BUTTON = (By.CSS_SELECTOR, 'body > section > form > div > article > div:nth-child(2) > div > div > div > div:nth-child(2) > div > div.col-md-2.col-sm-2.col-xs-12.payment-title > label')
    PAYPAL_RADIO_BUTTON = (By.CSS_SELECTOR, 'body > section > form > div > article > div:nth-child(2) > div > div > div > div:nth-child(3) > div > div.col-md-2.col-sm-2.col-xs-12.payment-title > label')
    DOTPAY_CHECKOUT_OFFLINE_RADIO_BUTTON = (By.CSS_SELECTOR, 'body > section > form > div > article > div:nth-child(2) > div > div > div > div:nth-child(4) > div > div.col-md-2.col-sm-2.col-xs-12.payment-title > label')
    PAY_BUTTON = (By.CLASS_NAME, 'btn btn-block btn-buying btn-lg text-uppercase')

    def find_and_insert_email(self, text):
        self.insert_text(self.EMAIL_BOX, text)
        return self

    def find_and_insert(self, text):
        self.insert_text(self.NAME_BOX, text)
        self.insert_text(self.COMPANY_NAME_BOX, text)
        self.insert_text(self.ADDRESS1_BOX, text)
        self.insert_text(self.ADDRESS2_BOX, text)
        self.insert_text(self.CITY_BOX, text)
        self.insert_text(self.PHONE_BOX, text)
        return self

    def find_and_insert_postal(self, text):
        self.insert_text(self.POSTAL_CODE_BOX, text)
        return self

    def choose_payment(self):
        if self.click_on(self.DOTPAY_CHECKOUT_RADIO_BUTTON):
            print('dotpay')
        elif self.click_on(self.CARD_RADIO_BUTTON):
            print('card')
        elif self.click_on(self.DOTPAY_CHECKOUT_OFFLINE_RADIO_BUTTON):
            print('dotpay_offline')
        return self

    def click_pay(self):
        self.click_on(self.PAY_BUTTON)
        return self

