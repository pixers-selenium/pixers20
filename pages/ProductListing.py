from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class ProductListing(BasePage):

    FIRST_PRODUCT = (By.CLASS_NAME, 'img-responsive image-square ')
    SORT_DROPDOWN = (By.CLASS_NAME, 'btn dropdown-toggle btn-default btn-sm-tight')
    SORT_BY_RANGED = (By.XPATH, '//*[@id="configure-more-popup"]/div/div/div[2]/div/div/ul/li[1]/a')
    SORT_BY_POPULAR = (By.XPATH, '//*[@id="configure-more-popup"]/div/div/div[2]/div/div/ul/li[2]/a')
    SORT_BY_LATEST = (By.XPATH, '//*[@id="configure-more-popup"]/div/div/div[2]/div/div/ul/li[3]/a')
    SORT_BY_CHEAPEST = (By.XPATH, '//*[@id="configure-more-popup"]/div/div/div[2]/div/div/ul/li[4]/a')

    def go_to_first_product(self):
        self.click_on(self.FIRST_PRODUCT)
        return self

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

"""
    def chose_sort_option(self):
        self.click_on(self.SORT_DROPDOWN)
        
        if chose == "Polecane":
            self.click_on(self.SORT_BY_RANGED)
        
        elif chose == "Najpopularniejsze":
            self.click_on(self.SORT_BY_POPULAR)
        
        elif chose == "Najnowsze":
            self.click_on(self.SORT_BY_LATEST)
        
        elif choose == "Od najtańszych":
            self.click_on(self.SORT_BY_CHEAPEST)
        
        else
            print("Dokonaj wyboru")
        
        return self

"""

