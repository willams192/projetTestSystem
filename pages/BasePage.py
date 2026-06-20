from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def close(self):
        self.driver.quit()

    def is_url_valid(self, url):
        return self.driver.current_url == url