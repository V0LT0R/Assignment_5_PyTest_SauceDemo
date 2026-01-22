import logging
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

LOGGER = logging.getLogger("automation")

@pytest.mark.smoke
def test_tc01_valid_login(driver):
    """TC-01: Valid login should open Inventory page"""
    LOGGER.info("TC-01 START: valid login")
    login = LoginPage(driver)
    login.open()

    LOGGER.info("Step: login with valid credentials")
    login.login("standard_user", "secret_sauce")

    LOGGER.info("Checkpoint: inventory title is 'Products'")
    inv = InventoryPage(driver)
    assert inv.title_text() == "Products"
    LOGGER.info("TC-01 END: pass")


def test_tc02_invalid_login_shows_error(driver):
    """TC-02: Invalid login should show error message"""
    LOGGER.info("TC-02 START: invalid login")
    login = LoginPage(driver)
    login.open()

    LOGGER.info("Step: login with invalid password")
    login.login("standard_user", "wrong_password")

    LOGGER.info("Checkpoint: error message contains expected text")
    assert "do not match" in login.error_text().lower()
    LOGGER.info("TC-02 END: pass")


@pytest.mark.smoke
def test_tc03_logout_returns_to_login(driver):
    """TC-03: Logout should return to login page"""
    LOGGER.info("TC-03 START: logout")
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inv = InventoryPage(driver)

    # Explicit wait for menu button to be clickable (demonstrates explicit wait usage)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))

    LOGGER.info("Step: logout via menu")
    inv.logout()

    LOGGER.info("Checkpoint: URL contains saucedemo.com and login button exists")
    assert "saucedemo.com" in driver.current_url
    assert driver.find_elements(By.ID, "login-button")
    LOGGER.info("TC-03 END: pass")
