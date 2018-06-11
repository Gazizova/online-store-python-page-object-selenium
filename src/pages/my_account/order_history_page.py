from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.uimap import Locators
from selenium import webdriver
from src.pages.base_page import InvalidPageException
from src.pages.base_page import BasePage

class OrderHistory(BasePage):

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        super(OrderHietory, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            self.element = WebDriverWait(driver, 10).until(
                expected_conditions.title_contains("Order history - My Store"))
        except:
            raise InvalidPageException("Order history is not loaded")

    def order_history(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .element_to_be_clickable((By.XPATH, Locators.OrderHistoryAndDetailsXpath)))
        order_history = self.driver.find_element(By.XPATH, Locators.OrderHistoryAndDetailsXpath)
        return order_history
