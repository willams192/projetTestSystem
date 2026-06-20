from selenium.webdriver.common.by import By
from Page.BasePage import BasePage


class LoginPage(BasePage):
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    login_customer_button = (By.CSS_SELECTOR, "button[ng-click='customer()']")
    login_bank_manager_button = (By.CSS_SELECTOR, "button[ng-click='manager()']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.URL)

    def click_login_customer_button(self):
        self.driver.find_element(*self.login_customer_button).click()

    def click_login_manager_button(self):
        self.driver.find_element(*self.login_bank_manager_button).click()
