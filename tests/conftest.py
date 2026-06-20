import pytest
from selenium import webdriver

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
