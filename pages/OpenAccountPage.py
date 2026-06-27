from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.BasePage import BasePage


class OpenAccountPage(BasePage):
    url_open_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
    open_account_tab_btn = (By.CSS_SELECTOR, 'button[ng-class="btnClass2"]')
    customer_dropdown = (By.ID, 'userSelect')
    currency_dropdown = (By.ID, 'currency')
    process_btn = (By.CSS_SELECTOR, 'button[type="submit"]')

    def __init__(self, driver):
        super(OpenAccountPage, self).__init__(driver)

    def click_open_account_tab(self):
        open_account_btn = self.driver.find_element(*self.open_account_tab_btn)
        open_account_btn.click()

    def select_customer(self, customer_name):
        dropdown = Select(self.driver.find_element(*self.customer_dropdown))
        dropdown.select_by_visible_text(customer_name)

    def select_currency(self, currency_value):
        dropdown = Select(self.driver.find_element(*self.currency_dropdown))
        dropdown.select_by_value(currency_value)

    def click_process(self):
        confirm_btn = self.driver.find_element(*self.process_btn)
        confirm_btn.click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        assert "Account created successfully" in alert.text
        alert.accept()