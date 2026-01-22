from selenium.webdriver.common.by import By

class InventoryPage:
    TITLE = (By.CSS_SELECTOR, ".title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CSS_SELECTOR, "a.shopping_cart_link")
    MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def title_text(self) -> str:
        return self.driver.find_element(*self.TITLE).text

    def add_backpack(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART).click()

    def logout(self):
        self.driver.find_element(*self.MENU).click()
        self.driver.find_element(*self.LOGOUT).click()
