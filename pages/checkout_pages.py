from selenium.webdriver.common.by import By

class CheckoutInfoPage:
    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def fill_and_continue(self, first: str, last: str, zip_code: str):
        self.driver.find_element(*self.FIRST).send_keys(first)
        self.driver.find_element(*self.LAST).send_keys(last)
        self.driver.find_element(*self.ZIP).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE).click()

class CheckoutOverviewPage:
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")
    FINISH = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def total_text(self) -> str:
        return self.driver.find_element(*self.TOTAL).text

    def finish(self):
        self.driver.find_element(*self.FINISH).click()

class CheckoutCompletePage:
    HEADER = (By.CSS_SELECTOR, ".complete-header")

    def __init__(self, driver):
        self.driver = driver

    def header_text(self) -> str:
        return self.driver.find_element(*self.HEADER).text
