

class TestErrorMessageWhenWithdrawWithoutHavingEnoughMoney:

    expected_erro_message = "Transaction Failed. You can not withdraw amount more than the balance."


    def test_error_message(self, logged_in_customer):
        account_page = logged_in_customer

        account_page.click_deposit_tab()
        account_page.enter_amount(100)
        account_page.click_submit()
        account_page.wait_for_message("Deposit Successful")

        balance_before = account_page.get_balance()

        account_page.click_withdrawal_tab()
        account_page.enter_amount(101)
        account_page.click_submit()

        #verificar se saldo não foi alterado
        balance_after = account_page.get_balance()
        assert balance_after == balance_before

        #verificar mensagem de erro
        erro_message = account_page.get_message()
        assert erro_message == self.expected_erro_message




