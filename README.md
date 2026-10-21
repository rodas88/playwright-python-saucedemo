# SauceDemo QA Automation with Playwright

A hands-on QA Automation portfolio project built with Python, Playwright, and Pytest using the SauceDemo web application.

This repository documents my practical learning journey in QA Automation, progressing from basic browser interactions to a structured and reusable automated testing framework.

## Technologies

- Python
- Playwright
- Pytest
- pytest-html
- Git
- GitHub
- Visual Studio Code

## Concepts Implemented

- Locators
- Assertions
- Waits
- Screenshots
- Page Object Model (POM)
- Pytest
- Shared Fixtures
- Setup and Teardown
- End-to-End Testing
- Positive Testing
- Negative Testing
- HTML Test Reports
- Framework Structure
- Centralized Test Configuration
- Git Version Control

## Framework Structure

```text
playwright-python-saucedemo/
│
├── automation/
│   └── Learning modules and historical exercises
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_login_negative.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── utils/
│   └── config.py
│
├── screenshots/
│   ├── backpack.png
│   └── inventory_page.png
│
├── reports/
│   └── report.html
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Automated Test Scenarios

### 1. Valid Login

Validates that a user with valid credentials can successfully log in and access the SauceDemo inventory page.

Flow:

1. Open SauceDemo.
2. Enter valid credentials.
3. Perform login.
4. Validate navigation to the inventory page.

### 2. Invalid Login

Validates that SauceDemo correctly rejects an invalid password and displays the expected error message.

Flow:

1. Open SauceDemo.
2. Enter a valid username.
3. Enter an invalid password.
4. Attempt to log in.
5. Validate the login error message.

### 3. Add Product to Cart

Validates that a logged-in user can add Sauce Labs Backpack to the shopping cart.

Flow:

1. Open SauceDemo.
2. Perform login.
3. Validate the inventory page.
4. Add Sauce Labs Backpack to the cart.
5. Open the shopping cart.
6. Validate that Sauce Labs Backpack is visible in the cart.

### 4. Complete Checkout

Validates the complete purchase flow from login to successful order confirmation.

Flow:

1. Open SauceDemo.
2. Perform login.
3. Add Sauce Labs Backpack to the cart.
4. Open the shopping cart.
5. Validate the product.
6. Start checkout.
7. Complete customer information.
8. Continue to checkout overview.
9. Finish the order.
10. Validate the successful order confirmation.

Expected final message:

```text
Thank you for your order!
```

## Page Object Model

The framework separates page-specific locators and actions from test logic.

Current Page Objects:

```text
LoginPage
InventoryPage
CartPage
CheckoutPage
```

This improves code readability, reusability, and maintainability.

## Shared Test Setup

The project uses `tests/conftest.py` to provide a shared Playwright `page` fixture.

The fixture handles:

1. Starting Playwright.
2. Launching Chromium.
3. Creating a browser context.
4. Creating a new page.
5. Providing the page to each test.
6. Closing the context and browser after the test finishes.

This prevents browser setup and teardown code from being duplicated across test files.

## Centralized Configuration

Reusable configuration is stored in:

```text
utils/config.py
```

This includes values such as:

```text
BASE_URL
USERNAME
PASSWORD
```

Tests can reuse the same configuration instead of duplicating these values.

## Run the Complete Test Suite

Activate the virtual environment and run:

```bash
python -m pytest tests -s
```

Current expected result:

```text
4 passed
```

## Run Individual Tests

Valid Login:

```bash
python -m pytest tests/test_login.py -s
```

Negative Login:

```bash
python -m pytest tests/test_login_negative.py -s
```

Cart:

```bash
python -m pytest tests/test_cart.py -s
```

Checkout:

```bash
python -m pytest tests/test_checkout.py -s
```

## Generate HTML Test Report

Run:

```bash
python -m pytest tests -s --html=reports/report.html
```

The generated HTML report provides information such as:

- Test results
- Passed and failed tests
- Execution duration
- Environment information
- Captured test output

## Current Test Suite

```text
test_login.py           ✅ Passed
test_login_negative.py  ✅ Passed
test_cart.py            ✅ Passed
test_checkout.py        ✅ Passed
```

Latest full execution:

```text
4 passed
```

## Learning Progress

- Module 1 - Locators ✅
- Module 2 - Assertions ✅
- Module 3 - Waits ✅
- Module 4 - Screenshots ✅
- Module 5 - Page Object Model ✅
- Module 6 - Pytest ✅
- Module 7 - Fixtures ✅
- Module 8 - End-to-End Testing ✅
- Module 9 - Test Reports ✅
- Module 10 - Framework Structure ✅
- Git and GitHub Workflow ✅

## Project Status

The main learning objectives for this QA Automation project have been completed.

The project now includes:

- Positive and negative automated testing
- End-to-end purchase automation
- Page Object Model
- Shared Pytest fixtures
- Centralized configuration
- HTML execution reports
- Git version control
- GitHub documentation
- Professional framework structure

This repository serves as a practical QA Automation portfolio project and as a foundation for future improvements.