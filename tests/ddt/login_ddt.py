import unittest
import csv
from ddt import ddt, data, unpack
from selenium import webdriver
from basetestcase import BaseTestCase
from src.pages.login_page import LoginPage
from src.pages.start_page import StartPage


def getdata(file_name):
    rows = []
    data_file = open(file_name, "rb")
    reader = csv.reader(data_file)
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class Login(BaseTestCase):
    def setUp(self):
        super(Login, self).setup()

    # specify test data using @data decorator
    # @data(("addresss@address.com", '12345+'), ("addresss@address.com", '123456+'))
    @data(*getdata("test_data.csv"))
    @unpack
    def test_something(self, userlogin, password):
        start = StartPage(self.driver)
        start.singInButton_click()

        login = LoginPage(self.driver)
        login.emailInput(userlogin)
        login.passwordInput(password)
        login.clickSihgInButton()

        # self.account = AccountPage(self.driver)


if __name__ == '__main__':
    unittest.main()
