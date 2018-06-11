from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.uimap import Locators
from selenium import webdriver
from src.pages.base_page import InvalidPageException
from src.pages.base_page import BasePage

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
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .element_to_be_clickable((By.XPATH, Locators.OrderHistoryAndDetailsXpath)))
        order_history = self.driver.find_element(By.XPATH, Locators.OrderHistoryAndDetailsXpath)
        return order_history

    def my_credit_slips(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .element_to_be_clickable((By.XPATH, Locators.MyCreditSlips)))
        my_credit_slips = self.driver.find_element(By.XPATH, Locators.MyCreditSlips)
        return my_credit_slips

    def my_address(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .element_to_be_clickable((By.XPATH, Locators.MyAddress)))
        my_address = self.driver.find_element(By.XPATH, Locators.MyAddress)
        return my_address

    def my_personal_information(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .element_to_be_clickable((By.XPATH, Locators.MyPersonalInformation)))
        my_personal_information = self.driver.find_element(By.XPATH, Locators.MyPersonalInformation)
        return my_personal_information

    def my_wishlist(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .element_to_be_clickable((By.XPATH, Locators.MyWishlist)))
        my_wishlist = self.driver.find_element(By.XPATH, Locators.MyWishlist)
        return my_wishlist
