from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):

    SEARCH_BOX = (By.ID, 'photoProduct_query')
    SEARCH_CATEGORY_SELECTOR = (By.XPATH, '//*[@id="header"]/section[2]/div/div/div[2]/div/div[1]/div/button')
    SEARCH_BUTTON = (By.CLASS_NAME, 'icon-search')

    def search_query(self, text):
        self.insert_text(self.SEARCH_BOX, text)
        self.click_on(self.SEARCH_BUTTON)
        return self  # powinno zwracac nowy obiekt klasy ProductListing(self.driver), ale na razie jej nie ma