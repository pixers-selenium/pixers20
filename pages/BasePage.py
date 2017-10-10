from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TIMEOUT = 10

    LOGO = (By.CLASS_NAME, 'logo')
    NEWSLETTER_CLOSE = (By.XPATH, '//*[@id="welcomeNewsletterPopup"]/*[@aria-label="close"]')
    ORDER_CART_BUTTON = (By.CLASS_NAME, 'productsPopup__icon cart__icon')
    LOADER_OVERLAY = (By.CLASS_NAME, 'loader-overlay')
    WISHLIST_ICON = (By.CLASS_NAME, 'icon-heart-empty')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, time = TIMEOUT):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def find_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)

    def click_on(self, locator):
        element = self.find_element(locator)
        element.click()

    def insert_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
        return self

    def get_page_title(self):
        return self.driver.title