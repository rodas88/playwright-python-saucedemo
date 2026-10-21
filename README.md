# SauceDemo QA Automation with Playwright

A hands-on QA automation project built with Python, Playwright, and Pytest using the SauceDemo web application.

This repository documents my practical learning journey in QA Automation, progressing from basic browser interactions to a structured and reusable automation framework.

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
- Fixtures
- Setup and teardown
- Shared fixtures with conftest.py
- End-to-End Testing
- HTML Test Reports
- Framework Structure
- Centralized test configuration

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

## Framework Structure

```text
playwright-python-saucedemo/
│
├── automation/
│   └── Learning modules and historical exercises
│
├── pages/
│   └── login_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_cart.py
│   └── test_login.py
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

### Valid Login

The login test validates that a user with valid credentials can successfully access the SauceDemo inventory page.

Flow:

1. Open SauceDemo.
2. Enter valid credentials.
3. Perform login.
4. Validate navigation to the inventory page.

### Add Product to Cart

The cart test validates that a logged-in user can add a product and find it inside the shopping cart.

Flow:

1. Open SauceDemo.
2. Perform login.
3. Validate the inventory page.
4. Add Sauce Labs Backpack to the cart.
5. Open the shopping cart.
6. Validate that Sauce Labs Backpack is visible in the cart.

## Shared Test Setup

The project uses `conftest.py` to provide a shared Playwright `page` fixture for the automated tests.

The fixture is responsible for:

1. Starting Playwright.
2. Launching Chromium.
3. Creating a browser context.
4. Creating a new page.
5. Providing the page to the test.
6. Closing the context and browser after the test finishes.

This avoids duplicating browser setup and teardown code across multiple test files.

## Run All Tests

```bash
python -m pytest tests -s
```

Current expected result:

```text
2 passed
```

## Generate HTML Report

```bash
python -m pytest tests -s --html=reports/report.html
```

The HTML report includes test execution results such as passed tests, failed tests, execution duration, and environment information.

## Project Status

This project is actively being expanded as a QA Automation portfolio project.

The current framework includes reusable Page Objects, centralized configuration, shared Pytest fixtures, automated login and cart scenarios, HTML test reports, Git version control, and GitHub documentation.

Additional test scenarios and framework improvements will continue to be added progressively.