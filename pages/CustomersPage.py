from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CustomersPage(BasePage):
    url_customers = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    customers_tab_btn = (By.CSS_SELECTOR, 'button[ng-class="btnClass3"]')
    search_input = (By.CSS_SELECTOR, 'input[ng-model="searchCustomer"]')
    delete_btn_format = "//td[contains(text(), '{name}')]/..//button[text()='Delete']"
    customer_row_format = "//td[contains(text(), '{name}')]"

    def __init__(self, driver):
        super(CustomersPage, self).__init__(driver)

    def click_customers_tab(self):
        self.driver.find_element(*self.customers_tab_btn).click()

    def search_customer(self, name):
        search = self.driver.find_element(*self.search_input)
        search.clear()
        search.send_keys(name)

    def delete_customer_by_name(self, name):
        xpath_dinamico = (By.XPATH, self.delete_btn_format.format(name=name))
        self.driver.find_element(*xpath_dinamico).click()

    def is_customer_in_list(self, name):
        xpath_dinamico = (By.XPATH, self.customer_row_format.format(name=name))
        try:
            return self.driver.find_element(*xpath_dinamico).is_displayed()
        except:
            return False