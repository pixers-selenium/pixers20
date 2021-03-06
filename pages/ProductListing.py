from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.ProductPage import ProductPage


class ProductListing(BasePage):

    FIRST_PRODUCT = (By.CSS_SELECTOR, 'body > main > section > section > div:nth-child(1) > article')
    SORT_DROPDOWN = (By.XPATH, '//div[@aria-label="sort-products"]')
    SORT_BY_RANGED = (By.XPATH, '//*[@id="configure-more-popup"]/div/div/div[2]/div/div/ul/li[1]/a')
    SORT_BY_POPULAR = (By.XPATH, '//*[@id="configure-more-popup"]/div/div/div[2]/div/div/ul/li[2]/a')
    SORT_BY_LATEST = (By.XPATH, '//*[@id="configure-more-popup"]/div/div/div[2]/div/div/ul/li[3]/a')
    SORT_BY_CHEAPEST = (By.XPATH, '//*[@id="configure-more-popup"]/div/div/div[2]/div/div/ul/li[4]/a')
    NEWSLETTER_CLOSE = (By.XPATH, '//*[@id="welcomeNewsletterPopup"]/*[@aria-label="close"]')

    def go_to_first_product(self):
        self.click_on(self.FIRST_PRODUCT)
        return ProductPage(self.driver)

    def go_to_product(self, product_index = 1):
        PRODUCT = (By.CSS_SELECTOR, 'body > main > section > section > div:nth-child(' + str(product_index) + ') > article > figure > div > div > a')
        self.find_element(PRODUCT).click()
        self.wait_for_element((By.CSS_SELECTOR, '#addToCartForm:not(.disableForm)'))
        return ProductPage(self.driver)

    def choose_sort_option_ranged(self):
        self.click_on(self.SORT_DROPDOWN)
        self.click_on(self.SORT_BY_RANGED)
        return self

    def choose_sort_option_popular(self):
        self.click_on(self.SORT_DROPDOWN)
        self.click_on(self.SORT_BY_POPULAR)
        return self

    def choose_sort_option_latest(self):
        self.click_on(self.SORT_DROPDOWN)
        self.click_on(self.SORT_BY_LATEST)
        return self

    def choose_sort_option_cheapest(self):
        self.click_on(self.SORT_DROPDOWN)
        self.click_on(self.SORT_BY_CHEAPEST)
        return self


    def chose_sort_option(self, sort_type):
        self.click_on(self.SORT_DROPDOWN)
        
        if sort_type == "ranged":
            self.click_on(self.SORT_BY_RANGED)
        
        elif sort_type == "popular":
            self.click_on(self.SORT_BY_POPULAR)
        
        elif sort_type == "latest":
            self.click_on(self.SORT_BY_LATEST)
        
        elif sort_type == "cheapest":
            self.click_on(self.SORT_BY_CHEAPEST)
        else:
            print("Dokonaj wyboru")
        return self

    def click_newsletter_close(self):
        try:
            self.find_element(self.NEWSLETTER_CLOSE).click()
            self.wait_for_element_is_invisible(self.NEWSLETTER_CLOSE)
        except TimeoutException:
            pass
        return self
