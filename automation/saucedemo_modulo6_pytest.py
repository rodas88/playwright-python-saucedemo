from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

from login_page import LoginPage

# ==========================
# CREDENCIALES
# ==========================

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# ==========================
# TEST LOGIN
# ==========================

def test_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        context = browser.new_context()

        page = context.new_page()

        page.goto(
            "https://www.saucedemo.com/"
        )

        print("✅ Página abierta")

        login_page = LoginPage(page)

        login_page.login(
            USERNAME,
            PASSWORD
        )

        print(
            "✅ Login ejecutado"
        )

        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

        print(
            "✅ Login validado"
        )

        browser.close()