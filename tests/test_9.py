
from pages.CustomersPage import CustomersPage

class TestSearchUserByAccountNumber:

    def test_search_user_by_account_number(self,created_customer_account):
        login_page = created_customer_account

        customer_page = CustomersPage(login_page.driver)

        customer_page.click_customers_tab()
        customer_page.search_customer('1016')

        #checa se a listagem tem apenas uma linha
        assert customer_page.is_only_one_result_in_list()

        #chechar se numero da conta está presente na linha
        assert customer_page.is_account_number_in_list('1016')







