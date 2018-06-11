from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.uimap import Locators
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.base_page import BasePage
from src.pages.base_page import InvalidPageException
from src.pages.login_page import LoginPage

class StartPage(BasePage):

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        super(StartPage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            WebDriverWait(self.driver, 20).until(
                lambda x: x.find_element_by_xpath(Locators.SignInButtonXpath).is_displayed())
            # WebDriverWait(self.driver, 20).until(
            #     lambda x: x.find_element_by_xpath(Locators.SignInButtonXpath).is_displayed())
        except:
            raise InvalidPageException("Start page is not loaded")

    def singInButton_click(self):
        self.driver.find_element(By.XPATH, Locators.SignInButtonXpath).click()
        return LoginPage(self.driver)

    def contactUsButton(self):
        contactUsButton = self.driver.find_element(By.XPATH, Locators.ContactUsButtonXpath)
        return contactUsButton

    def womenLink(self):
        womenLink = self.driver.find_element(By.XPATH, Locators.WomenButtonXpath)
        return womenLink

    def dressLink(self):
        dressLink = self.driver.find_element(By.XPATH, Locators.DressesButtonXpath)
        return dressLink

    def tShirtsLink(self):
        tShirtsLink = self.driver.find_element(By.XPATH, Locators.T_shirtsButtonXpath)
        return tShirtsLink
