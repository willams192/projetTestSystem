from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class AccountPage(BasePage):

    deposit_tab = (By.CSS_SELECTOR, 'button[ng-click="deposit()"]')
    withdrawal_tab = (By.CSS_SELECTOR, 'button[ng-click="withdrawl()"]')
    transactions_tab = (By.CSS_SELECTOR, 'button[ng-click="transactions()"]')
    amount_input = (By.CSS_SELECTOR, 'input[ng-model="amount"]')
    submit_btn = (By.CSS_SELECTOR, 'button[type="submit"]')
    balance_element = (By.CSS_SELECTOR, 'strong.ng-binding')
    message_element = (By.CSS_SELECTOR, 'span.error.ng-binding')
    transaction_rows = (By.CSS_SELECTOR, 'table tbody tr')

    def __init__(self, driver):
        super().__init__(driver)

    def get_balance(self):
        elements = self.driver.find_elements(*self.balance_element)
        return int(elements[1].text)

    def click_deposit_tab(self):
        self.driver.find_element(*self.deposit_tab).click()

    def click_withdrawal_tab(self):
        self.driver.find_element(*self.withdrawal_tab).click()
        WebDriverWait(self.driver, 10).until(
            lambda d: any(
                btn.text == 'Withdraw' and btn.is_displayed()
                for btn in d.find_elements(*self.submit_btn)
            )
        )

    def enter_amount(self, amount):
        input_field = self.driver.find_element(*self.amount_input)
        input_field.clear()
        input_field.send_keys(str(amount))

    def click_submit(self):
        buttons = self.driver.find_elements(*self.submit_btn)
        for btn in buttons:
            if btn.is_displayed():
                btn.click()
                return

    def get_message(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.message_element))
        return element.text

    def wait_for_message(self, expected_text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda d: any(
            expected_text.lower() in el.text.lower()
            for el in d.find_elements(*self.message_element)
        ))
        return next(
            el.text for el in self.driver.find_elements(*self.message_element)
            if expected_text.lower() in el.text.lower()
        )

    def click_transactions_tab(self):
        self.driver.find_element(*self.transactions_tab).click()

    def get_transactions(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.transaction_rows))
        rows = self.driver.find_elements(*self.transaction_rows)
        transactions = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) == 3:
                transactions.append({
                    'date': cells[0].text,
                    'amount': cells[1].text,
                    'type': cells[2].text
                })
        return transactions
