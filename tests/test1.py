from selenium import webdriver
from pages.LoginPage import LoginPage


class TestLoginPage:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.click_login_customer_button()
