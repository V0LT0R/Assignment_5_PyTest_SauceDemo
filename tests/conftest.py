import os
import logging
import pytest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ---------- Logging (file) ----------
def _configure_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("automation")
    logger.setLevel(logging.INFO)

    # prevent duplicate handlers in reruns
    if logger.handlers:
        return logger

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")

    fh = logging.FileHandler("logs/automation.log", encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(fmt)

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger

LOGGER = _configure_logger()


# ---------- PyTest lifecycle management ----------
@pytest.fixture
def driver(request):
    LOGGER.info("SETUP: start browser")
    os.makedirs("reports/screenshots", exist_ok=True)

    headless = os.environ.get("HEADLESS", "false").lower() == "true"
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1400,900")

    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    d.implicitly_wait(5)
    d.maximize_window()

    yield d

    LOGGER.info("TEARDOWN: quit browser")
    d.quit()


# ---------- Screenshots on failure + attach to pytest-html ----------
@pytest.hookimpl(hookwrapper=False)
def pytest_runtest_makereport(item, call):
    if call.when != "call":
        return

    rep = item._store.get("rep_call", None)

    if rep is None:
        return

    if rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            filename = f"{item.name}_{ts}.png"
            path = os.path.join("reports", "screenshots", filename)

            try:
                driver.save_screenshot(path)

                # attach to pytest-html if available
                if hasattr(rep, "extra"):
                    import pytest_html
                    rep.extra.append(pytest_html.extras.png(path))

            except Exception:
                pass
def pytest_runtest_call(item):
    item._store = getattr(item, "_store", {})
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    item._store["rep_" + rep.when] = rep



def pytest_configure(config):
    # add environment info into HTML report (pytest-html)
    if not hasattr(config, "_metadata") or config._metadata is None:
        config._metadata = {}

    config._metadata["System Under Test"] = "SauceDemo (https://www.saucedemo.com)"
    config._metadata["Framework"] = "PyTest + Selenium"
    config._metadata["Logs"] = "logs/automation.log"
