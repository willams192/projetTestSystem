from pages.LoginPage import LoginPage


class TestLoginPage:

    def test_login_page(self, open_browser):
        login_page = open_browser
        login_page.click_login_customer_button()
