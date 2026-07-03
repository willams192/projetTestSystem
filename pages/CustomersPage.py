from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CustomersPage(BasePage):
    url_customers = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    customers_tab_btn = (By.CSS_SELECTOR, 'button[ng-class="btnClass3"]')
    search_input = (By.CSS_SELECTOR, 'input[ng-model="searchCustomer"]')
    delete_btn_format = "//td[contains(text(), '{name}')]/..//button[text()='Delete']"
    customer_row_format = "//td[contains(text(), '{name}')]"
    customer_table_body = (By.CSS_SELECTOR, "table tbody tr")
    account_number_row_elements= (By.CSS_SELECTOR,  "table tbody tr td span[ng-repeat*='accountNo']")

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
        
    def is_only_one_result_in_list(self):
        rows = self.driver.find_elements(*self.customer_table_body)

        return len(rows) == 1
    
    def is_account_number_in_list(self, current_account_number):
        account_number_list = self.driver.find_elements(*self.account_number_row_elements)
        for account_number in account_number_list:
            if account_number.text == current_account_number:
                return True
            
        return False