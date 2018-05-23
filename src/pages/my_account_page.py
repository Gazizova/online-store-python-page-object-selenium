from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.uimap import Locators
from selenium import webdriver

class AccountPage(object):

    def __init__(self, driver):
        # self.driver = driver
        self.driver = webdriver.Chrome()

    def order_history(self):
        order_history = self.driver.find_element(By.XPATH, Locators.OrderHistoryAndDetailsXpath)
        return order_history