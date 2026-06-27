from pages.OpenAccountPage import OpenAccountPage


class Test2:

    def test_open_bank_account_in_dollar(self, created_customer):
        add_customer_page = created_customer
        open_account_page = OpenAccountPage(add_customer_page.driver)
        open_account_page.click_open_account_tab()
        open_account_page.select_customer("Teste Testador")
        open_account_page.select_currency("Dollar")

        open_account_page.click_process()
        assert open_account_page.is_url_valid(open_account_page.url_open_account), "Falha ao permanecer na página"