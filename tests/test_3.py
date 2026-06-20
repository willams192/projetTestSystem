from pages.CustomersPage import CustomersPage


class TestDeleteCustomer:

    def test_delete_customer(self, created_customer):
        add_customer_page = created_customer

        customers_page = CustomersPage(add_customer_page.driver)

        nome_cliente = "Teste"

        customers_page.click_customers_tab()
        customers_page.search_customer(nome_cliente)
        customers_page.delete_customer_by_name(nome_cliente)

        assert not customers_page.is_customer_in_list(nome_cliente), f"O cliente {nome_cliente} ainda aparece na lista!"