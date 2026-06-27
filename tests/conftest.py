import pytest
from selenium import webdriver

from pages.AddCustomerPage import AddCustomerPage
from pages.LoginPage import LoginPage


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
    return add_customer_page