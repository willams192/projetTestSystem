import pytest
from selenium import webdriver

from pages.AccountPage import AccountPage
from pages.AddCustomerPage import AddCustomerPage
from pages.CustomersPage import CustomersPage
from pages.LoginPage import LoginPage
from pages.OpenAccountPage import OpenAccountPage


@pytest.fixture
def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    login_page = LoginPage(driver)
    login_page.open_login_page()
    yield login_page
    login_page.close()


@pytest.fixture
def created_customer(open_browser):

    login_page = open_browser
    login_page.click_login_manager_button()

    add_customer_page = AddCustomerPage(login_page.driver)
    add_customer_page.click_add_customer()
    add_customer_page.input_customer_name()
    add_customer_page.input_customer_last_name()
    add_customer_page.input_customer_address()
    add_customer_page.click_confirm_add_customer()

    yield add_customer_page

    login_page.open_login_page()
    login_page.click_login_manager_button()

    customers_page = CustomersPage(add_customer_page.driver)
    customers_page.click_customers_tab()
    customers_page.search_customer(add_customer_page.name_customer)

    if customers_page.is_customer_in_list(add_customer_page.name_customer):
        customers_page.delete_customer_by_name(add_customer_page.name_customer)

@pytest.fixture
def created_customer_account(created_customer):
    add_customer_page = created_customer

    open_account_page = OpenAccountPage(add_customer_page.driver)
    open_account_page.click_open_account_tab()
    open_account_page.select_customer("Teste Testador")
    open_account_page.select_currency("Dollar")
    open_account_page.click_process()

    return add_customer_page


@pytest.fixture
def logged_in_customer(created_customer):
    add_customer_page = created_customer

    open_account_page = OpenAccountPage(add_customer_page.driver)
    open_account_page.click_open_account_tab()
    open_account_page.select_customer("Teste Testador")
    open_account_page.select_currency("Dollar")
    open_account_page.click_process()

    login_page = LoginPage(add_customer_page.driver)
    login_page.open_login_page()
    login_page.click_login_customer_button()
    login_page.select_customer("Teste Testador")
    login_page.click_login()

    return AccountPage(add_customer_page.driver)