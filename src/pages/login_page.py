from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.uimap import Locators
from base_page import BasePage
from base_page import InvalidPageException
from my_account_page import AccountPage

class LoginPage(BasePage):

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        super(LoginPage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            self.element = WebDriverWait(self.driver, 10).until(
                expected_conditions.text_to_be_present_in_element((
                    By.CLASS_NAME, "navigation_page"), "Authentication"))
        except:
            raise InvalidPageException("Login page is not loaded")

    def emailInput(self, login):
        emailInputField = self.driver.find_element(By.ID, Locators.EmailID)
        emailInputField.clear()
        emailInputField.send_keys(login)

    def passwordInput(self, password):
        passwordInputField = self.driver.find_element(By.ID, Locators.PasswordID)
        passwordInputField.clear()
        passwordInputField.send_keys(password)

    def clickSihgInButton(self):
        SignInButton = self.driver.find_element(By.ID, Locators.SubmitLoginButtonID)
        SignInButton.click()
        # return AccountPage(self.driver)
