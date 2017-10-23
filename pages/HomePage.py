from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.ProductListing import ProductListing


class HomePage(BasePage):

    SEARCH_BOX = (By.ID, 'photoProduct_query')
    SEARCH_CATEGORY_SELECTOR = (By.XPATH, '//*[@id="header"]/section[2]/div/div/div[2]/div/div[1]/div/button')
    SEARCH_BUTTON = (By.CLASS_NAME, 'icon-search')
    CHANGE_COUNTRY_DROPDOWN = (By.CSS_SELECTOR, '#header > section.hidden-xs > div > div > div > div:nth-child(2) > div > button > span > span.flag.flag-pl.flag-framed')
    COUNTRY_USA = (By.CSS_SELECTOR, '#header > section.hidden-xs > div > div > div > div:nth-child(2) > div > ul > li:nth-child(1) > a > span:nth-child(2)')

    def search_query(self, text):
        self.insert_text(self.SEARCH_BOX, text)
        self.click_on(self.SEARCH_BUTTON)
        return ProductListing(self.driver)

    def change_country_to_usa(self):
        self.click_on(self.CHANGE_COUNTRY_DROPDOWN)
        self.click_on(self.CHANGE_COUNTRY_DROPDOWN)
        #self.wait_for_element(self.COUNTRY_USA)
        self.click_on(self.COUNTRY_USA)
        return self

