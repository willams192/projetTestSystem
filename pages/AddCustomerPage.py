from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class AddCustomerPage(BasePage):
    url_add_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    add_customer_btn = (By.CSS_SELECTOR, 'button[ng-class="btnClass1"]')
    confirm_add_customer_btn = (By.CSS_SELECTOR, 'button.btn.btn-default')
    input_name_customer = (By.CSS_SELECTOR, 'input[ng-model="fName"]')
    input_last_name = (By.CSS_SELECTOR, 'input[ng-model="lName"]')
    input_post_code = (By.CSS_SELECTOR, 'input[ng-model="postCd"]')
    name_customer = 'Teste'
    last_name_customer = 'Testador'
    post_code_customer = '123'
    msg_success_customer= "Customer added successfully"

    def __init__(self, driver):
        super(AddCustomerPage, self).__init__(driver)

    def is_url_valid_customer(self):
        return self.is_url_valid(self.url_add_customer)

    def click_add_customer(self):
        btn_customer = self.driver.find_element(*self.add_customer_btn)
        btn_customer.click()

    def input_customer_name(self):
        input_name_customer = self.driver.find_element(*self.input_name_customer)
        input_name_customer.send_keys(self.name_customer)

    def input_customer_last_name(self):
        last_name = (self.driver.find_element(*self.input_last_name))
        last_name.send_keys(self.last_name_customer)

    def input_customer_address(self):
        input_post_code = self.driver.find_element(*self.input_post_code)
        input_post_code.send_keys(self.post_code_customer)

    def click_confirm_add_customer(self):
        btn_confirm_add_customer = self.driver.find_element(*self.confirm_add_customer_btn)
        btn_confirm_add_customer.click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        assert self.msg_success_customer in alert.text, f"Mensagem inesperada: {alert.text}"
        alert.accept()