from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.BasePage import BasePage


class LoginPage(BasePage):
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    login_customer_button = (By.CSS_SELECTOR, "button[ng-click='customer()']")
    login_bank_manager_button = (By.CSS_SELECTOR, "button[ng-click='manager()']")
    customer_dropdown = (By.ID, 'userSelect')
    login_btn = (By.CSS_SELECTOR, 'button[type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.URL)

    def click_login_customer_button(self):
        self.driver.find_element(*self.login_customer_button).click()

    def click_login_manager_button(self):
        self.driver.find_element(*self.login_bank_manager_button).click()

    def select_customer(self, name):
        dropdown = Select(self.driver.find_element(*self.customer_dropdown))
        dropdown.select_by_visible_text(name)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()
