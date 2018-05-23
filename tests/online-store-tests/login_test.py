import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from src.uimap import Locators
from selenium.webdriver.support import expected_conditions
from src.pages.login_page import LoginPage
from src.pages.start_page import StartPage
from src.pages.my_account_page import AccountPage
from selenium.webdriver.support.ui import WebDriverWait
from basetestcase import BaseTestCase


class MyTestCase(BaseTestCase):
    def setUp(self):
        super(MyTestCase, self).setup()
        # self.setup()
        # self.navigate_to_page(Locators.url)

    #     self.driver = webdriver.Chrome()
    #     self.driver.get(Locators.url)

    def test_login(self):
        start = StartPage(self.driver)
        start._validate_page(self.driver)
        start.singInButton_click()

        login = LoginPage(self.driver)
        login.emailInput('address@address.com')
        login.passwordInput('12345+')
        login.clickSihgInButton()

        # my_account = AccountPage(self.driver)
        # WebDriverWait(self.driver, 10).until(my_account.order_history().is_displayed())
        # if my_account.order_history().is_displayed():
        #     print "MyAccount loaded successfully"



if __name__ == '__main__':
    unittest.main()
