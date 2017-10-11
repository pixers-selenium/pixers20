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
    DOTPAY_CHECKOUT_RADIO_BUTTON = (By.XPATH, '/html/body/section/form/div/article/div[2]/div/div/div/div[1]/div/div[1]/label')
    CARD_RADIO_BUTTON = (By.XPATH, '/html/body/section/form/div/article/div[2]/div/div/div/div[2]/div/div[1]/label')
    PAYPAL_RADIO_BUTTON = (By.XPATH, '/html/body/section/form/div/article/div[2]/div/div/div/div[3]/div/div[1]/label')
    DOTPAY_CHECKOUT_OFFLINE_RADIO_BUTTON = (By.XPATH, '/html/body/section/form/div/article/div[2]/div/div/div/div[4]/div/div[1]/label')
    PAY_BUTTON = (By.XPATH, '/html/body/section/form/div/article/div[4]/div[2]/button')


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
        self.insert_text(self.POSTAL_CODE_BOX,text)
        return self
