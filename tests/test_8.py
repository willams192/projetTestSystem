from pages.OpenAccountPage import OpenAccountPage
from pages.LoginPage import LoginPage
from pages.AccountPage import AccountPage


class TestChangeAccountNumber:

    def test_change_account_number(self, created_customer_account):
        login_page = created_customer_account

        #Adicionar conta 2
        open_account_page = OpenAccountPage(login_page.driver)
        open_account_page.click_open_account_tab()
        open_account_page.select_customer("Teste Testador")
        open_account_page.select_currency("Pound")
        open_account_page.click_process()

        #Fazer login
        login_page = LoginPage(open_account_page.driver)
        login_page.open_login_page()
        login_page.click_login_customer_button()
        login_page.select_customer("Teste Testador")
        login_page.click_login()

        #Mudar de conta
        account_page = AccountPage(login_page.driver)
        #Salvar moeda e numero da conta
        account_number_before = account_page.get_account_number()
        account_currency_before = account_page.get_currency_type()
        account_page.select_specific_account_selector("1017")

        #verificar numero da conta mudou
        account_number_after = account_page.get_account_number()
        assert account_number_after != account_number_before

        #verificar que a moeda mudou
        account_currency_after = account_page.get_currency_type()
        assert account_currency_after != account_currency_before


