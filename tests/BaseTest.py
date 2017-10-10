import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):

    # confguration
    ENV = 'prod'
    DRIVER = 'chrome'
    DRIVER_PATH = 'C:/chromedriver.exe'

    def setUp(self):
        self.driver = self.createDriver()
        self.driver.maximize_window()
        self.driver.get("http://pixers.pl")

        if self.ENV == 'spluczka':
            self.driver.add_cookie({'name': 'broken', 'value': 'spluczka'})

    def tearDown(self):
        self.driver.quit()

    def createDriver(self):
        if self.DRIVER == 'chrome':
            return webdriver.Chrome(self.DRIVER_PATH)

        if self.DRIVER == 'firefox':
            return webdriver.Firefox(executable_path=self.DRIVER_PATH)