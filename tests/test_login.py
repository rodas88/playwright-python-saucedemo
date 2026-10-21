from playwright.sync_api import expect

from pages.login_page import LoginPage

from utils.config import (
    BASE_URL,
    USERNAME,
    PASSWORD
)

# ==========================
# TEST LOGIN EXITOSO
# ==========================

def test_valid_login(page):

    # ==========================
    # ABRIR SAUCEDEMO
    # ==========================

    page.goto(
        BASE_URL
    )

    print("✅ Página abierta")

    # ==========================
    # CREAR PAGE OBJECT
    # ==========================

    login_page = LoginPage(page)

    # ==========================
    # EJECUTAR LOGIN
    # ==========================

    login_page.login(
        USERNAME,
        PASSWORD
    )

    print("✅ Login ejecutado")

    # ==========================
    # VALIDAR LOGIN EXITOSO
    # ==========================

    expect(page).to_have_url(
        BASE_URL + "inventory.html"
    )

    print("✅ Login validado correctamente")