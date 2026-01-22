import logging
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_pages import CheckoutInfoPage, CheckoutOverviewPage, CheckoutCompletePage

LOGGER = logging.getLogger("automation")

def test_tc04_checkout_flow(driver):
    """TC-04: Add item to cart and complete checkout"""
    LOGGER.info("TC-04 START: checkout flow")
    login = LoginPage(driver)
    login.open()

    LOGGER.info("Step: login")
    login.login("standard_user", "secret_sauce")

    inv = InventoryPage(driver)
    LOGGER.info("Step: add backpack to cart")
    inv.add_backpack()

    LOGGER.info("Step: open cart")
    inv.go_to_cart()

    cart = CartPage(driver)
    assert cart.has_items(), "Cart is empty after adding an item"

    LOGGER.info("Step: checkout")
    cart.checkout()

    LOGGER.info("Step: fill checkout information")
    info = CheckoutInfoPage(driver)
    info.fill_and_continue("Yevhenii", "Biloshchytskyi", "010000")

    overview = CheckoutOverviewPage(driver)
    LOGGER.info("Checkpoint: total label exists")
    assert "total" in overview.total_text().lower()

    LOGGER.info("Step: finish checkout")
    overview.finish()

    done = CheckoutCompletePage(driver)
    LOGGER.info("Checkpoint: order completion message is shown")
    assert "thank you" in done.header_text().lower()
    LOGGER.info("TC-04 END: pass")
