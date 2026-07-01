from pages.AccountPage import AccountPage


class TestDeposit:

    def test_deposit(self, logged_in_customer):
        account_page = logged_in_customer

        account_page.click_deposit_tab()
        balance_before = account_page.get_balance()

        account_page.enter_amount(100)
        account_page.click_submit()

        assert "Deposit Successful" in account_page.get_message()
        balance_after = account_page.get_balance()
        assert balance_after == balance_before + 100
