# Assignment 5 (PyTest, Python) – SauceDemo UI Automation

**System under test:** https://www.saucedemo.com (Approved list)

## Requirements Coverage
1) **Test lifecycle management**: setup/teardown implemented with PyTest fixtures (`tests/conftest.py`)
2) **Logging**: Python `logging` framework with file output (`logs/automation.log`)
3) **HTML report**: `pytest-html` (`reports/report.html`)
4) **Minimum 3 test cases**: 4 automated test cases included

## Project Structure
```
Assignment_5_PyTest_SauceDemo/
├── requirements.txt
├── pytest.ini
├── README.md
├── logs/                 (generated)
├── reports/              (generated)
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_pages.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_login.py
    └── test_checkout.py
```

## Install
```bash
python -m pip install -r requirements.txt
```

## Run tests + generate HTML report
```bash
python -m pytest
```

## Outputs
- HTML report: `reports/report.html`
- Log file: `logs/automation.log`
