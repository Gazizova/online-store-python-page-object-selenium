from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.uimap import Locators
from selenium import webdriver
from base_page import InvalidPageException
from base_page import BasePage

class AccountPage(BasePage):

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        super(AccountPage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            self.element = WebDriverWait(driver, 10).until(
                expected_conditions.title_contains("My account - My Store"))
        except:
            raise InvalidPageException("Account page is not loaded")

    def order_history(self):
        order_history = self.driver.find_element(By.XPATH, Locators.OrderHistoryAndDetailsXpath)
        return order_history
