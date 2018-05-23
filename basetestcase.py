from selenium import webdriver
import unittest
from tests.resources import *

class BaseTestCase(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # return self.driver

    # def navigate_to_page(self, url):
        self.driver.get("http://automationpractice.com/index.php")

    def tearDown(self):
        self.driver.quit()