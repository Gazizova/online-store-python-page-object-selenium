import unittest

from basetestcase import BaseTestCase
from src.pages.login_page import LoginPage
from src.pages.my_account.my_account_page import AccountPage
from src.pages.start_page import StartPage


class MyTestCase(BaseTestCase):
    def setUp(self):
        super(MyTestCase, self).setup()
        # self.setup()
        # self.navigate_to_page(Locators.url)

        # self.driver = webdriver.Chrome()
        # self.driver.get(Locators.url)

    def test_login(self):
        start = StartPage(self.driver)
        start.singInButton_click()

        login = LoginPage(self.driver)
        login.emailInput('address@address.com')
        login.passwordInput('12345+')
        login.clickSihgInButton()

        self.account = AccountPage(self.driver)
        self.account._validate_page(self.driver)
        self.account.order_history().click()


    # def test_order_history(self):
    #     MyTestCase.test_login()
    #     self.account = AccountPage(self.driver)
    #
    #     self.account.order_history().click()




if __name__ == '__main__':
    unittest.main()
