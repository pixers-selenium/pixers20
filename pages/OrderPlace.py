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
    PAYMENT_DOTPAY = (By.CSS_SELECTOR, 'label[for="optionsRadiosDotpay_checkout"]')
    PAYMENT_OFFLINE = (By.CSS_SELECTOR, 'label[for="optionsRadiosDotpay_checkout_offline"]')
    PAYMENT_PAYPAL = (By.CSS_SELECTOR, 'label[for="optionsRadiosPaypal_express"]')
    PAYMENT_PAYPAL_CARD = (By.CSS_SELECTOR, 'label[for="optionsRadiosPaypal_card"]')
    PAY_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="pay-securely"]')

    def fill_email(self, text):
        self.insert_text(self.EMAIL_BOX, text)
        return self

    def fill_address_form(self, text):
        self.insert_text(self.NAME_BOX, text)
        self.insert_text(self.COMPANY_NAME_BOX, text)
        self.insert_text(self.ADDRESS1_BOX, text)
        self.insert_text(self.ADDRESS2_BOX, text)
        self.insert_text(self.CITY_BOX, text)
        self.insert_text(self.PHONE_BOX, text)
        return self

    def fill_postal(self, text):
        self.insert_text(self.POSTAL_CODE_BOX, text)
        return self

    def choose_payment(self, payment_type):
        if payment_type == "dotpay":
            self.click_on(self.PAYMENT_DOTPAY)
        elif payment_type == "card":
            self.click_on(self.PAYMENT_PAYPAL_CARD)
        elif payment_type == "offline":
            self.click_on(self.PAYMENT_OFFLINE)
        elif payment_type == "paypal":
            self.click_on(self.PAYMENT_PAYPAL)
        else:
            print("Choose payment type.")
        return self

    def click_pay_button(self):
        self.click_on(self.PAY_BUTTON)
        return self
