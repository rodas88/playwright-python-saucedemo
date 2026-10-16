import pytest

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

from login_page import LoginPage

# ==========================
# CREDENCIALES SAUCEDEMO
# ==========================

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# ==========================
# FIXTURE PAGE
# ==========================

@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        context = browser.new_context()

        page = context.new_page()

        # ==========================
        # ENTREGAR PAGE AL TEST
        # ==========================

        yield page

        # ==========================
        # LIMPIEZA
        # ==========================

        context.close()

        browser.close()


# ==========================
# TEST LOGIN
# ==========================

def test_login(page):

    # ==========================
    # ABRIR SAUCEDEMO
    # ==========================

    page.goto(
        "https://www.saucedemo.com/"
    )

    print("✅ Página abierta")

    # ==========================
    # CREAR PAGE OBJECT
    # ==========================

    login_page = LoginPage(page)

    # ==========================
    # LOGIN
    # ==========================

    login_page.login(
        USERNAME,
        PASSWORD
    )

    print("✅ Login ejecutado")

    # ==========================
    # ASSERTION
    # ==========================

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    print("✅ Login validado")