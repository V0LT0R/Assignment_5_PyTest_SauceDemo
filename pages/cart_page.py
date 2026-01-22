from selenium.webdriver.common.by import By

class CartPage:
    ITEM = (By.CSS_SELECTOR, ".cart_item")
    CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def has_items(self) -> bool:
        return len(self.driver.find_elements(*self.ITEM)) > 0

    def checkout(self):
        self.driver.find_element(*self.CHECKOUT).click()
