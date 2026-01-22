from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        u = self.driver.find_element(*self.USERNAME)
        p = self.driver.find_element(*self.PASSWORD)
        u.clear(); u.send_keys(username)
        p.clear(); p.send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def error_text(self) -> str:
        els = self.driver.find_elements(*self.ERROR)
        return els[0].text if els else ""
