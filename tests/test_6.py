import time
from datetime import datetime
from pages.AccountPage import AccountPage


class TestTransactions:

    def test_transactions(self, logged_in_customer):
        account_page = logged_in_customer

        account_page.click_deposit_tab()
        account_page.enter_amount(100)
        account_page.click_submit()
        account_page.wait_for_message("Deposit Successful")

        account_page.click_withdrawal_tab()
        account_page.enter_amount(1)
        account_page.click_submit()

        time.sleep(5)
        account_page.click_transactions_tab()
        transactions = account_page.get_transactions()

        today = datetime.now()
        expected_month = today.strftime("%b")
        expected_day = str(today.day)

        credit = next(t for t in transactions if t['type'] == 'Credit')
        debit = next(t for t in transactions if t['type'] == 'Debit')

        assert credit['amount'] == '100'
        assert expected_month in credit['date']
        assert expected_day in credit['date']

        assert debit['amount'] == '1'
        assert expected_month in debit['date']
        assert expected_day in debit['date']
