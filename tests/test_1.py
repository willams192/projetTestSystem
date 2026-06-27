from pages.AddCustomerPage import AddCustomerPage


class TestLoginPage:

    def test_login_page(self, open_browser):
        login_page = open_browser
        login_page.click_login_manager_button()
        add_customer_page = AddCustomerPage(login_page.driver)

        add_customer_page.click_add_customer()
        add_customer_page.input_customer_name()
        add_customer_page.input_customer_last_name()
        add_customer_page.input_customer_address()

        add_customer_page.click_confirm_add_customer()
        assert add_customer_page.is_url_valid_customer(), 'Página não encontrada'