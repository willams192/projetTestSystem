from pages.AccountPage import AccountPage


class TestWithdrawal:

    def test_withdrawal(self, logged_in_customer):
        account_page = logged_in_customer

        account_page.click_deposit_tab()
        account_page.enter_amount(100)
        account_page.click_submit()

        account_page.click_withdrawal_tab()
        balance_before = account_page.get_balance()

        account_page.enter_amount(1)
        account_page.click_submit()

        balance_after = account_page.get_balance()
        assert balance_after == balance_before - 1
